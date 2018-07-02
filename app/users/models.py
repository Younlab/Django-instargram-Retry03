from django.contrib.auth.models import AbstractUser
from django.db import models

from users.exceptions import RelationNotExist, DuplicateRelationException

class User(AbstractUser):
    CHOICES_GENDER = (
        ('m', '남성'),
        ('f', '여자'),
        ('x', '당신이 괜찮다면 설정해주세요.'),
    )
    profile_image = models.ImageField(upload_to='profile_image', blank=True ,help_text='사진을 넣어주세요', )
    site_url = models.URLField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)
    to_relation_users = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
        blank=True,
        related_name='from_relation_users',
        related_query_name='from_relation_user',
    )

    def __str__(self):
        return self.username

    def follow(self, to_user):
        if self.relations_by_from_user.filter(to_user=to_user).exists():
            raise DuplicateRelationException(from_user=self, to_user=to_user, relation_type='follow')


    def unfollow(self, to_user):
        q = self.relations_by_from_user.filter(
            to_user=to_user,
            relation_type=Relation.RELATION_TYPE_FOLLOW,
        )
        if q:
            q.delete()
        else:
            raise RelationNotExist(
                from_user=self,
                to_user=to_user,
                relation_type='Follow',
            )

    @property
    def following_relations(self):
        # 내가 follow중인 relation query리턴
        return self.relations_by_from_user.filter(
            relation_type=Relation.RELATION_TYPE_FOLLOW,
        )

    @property
    def follower_relations(self):
        # 나를 follow중인 relation query리턴
        return self.relations_by_to_user.filter(
            relation_type=Relation.RELATION_TYPE_FOLLOW,
        )

    @property
    def block_relations(self):
        return self.relations_by_from_user.filter(
            relation_type=Relation.RELATION_TYPE_BLOCK,
        )

    @property
    def following(self):
        return User.objects.filter(
            relations_by_to_user__from_user=self,
            relations_by_to_user__relation_type=Relation.RELATION_TYPE_FOLLOW,
        )

    @property
    def followers(self):
        return User.objects.filter(
            relations_by_to_from_user__to_user=self,
            relations_by_to_from__relation_typr=Relation.RELATION_TYPE_FOLLOW,
        )

    @property
    def block_user(self):
        return User.objects.filter(
            pk__in=self.block_relations.values('to_user')
        )

class Relation(models.Model):
    """
    User 간의 MTM 연결 중개테이블

    """
    RELATION_TYPE_BLOCK ='b'
    RELATION_TYPE_FOLLOW='f'
    CHOICES_RELATION_TYPE = (
        (RELATION_TYPE_FOLLOW, 'Follow'),
        (RELATION_TYPE_BLOCK, 'Block'),
    )

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )

    to_user =models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )

    relation_type = models.CharField(max_length=1, choices=CHOICES_RELATION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'From {from_user} to {to_user} ({type})'.format(
            from_user=self.from_user.username,
            to_user=self.to_user.username,
            type=self.get_relation_type_display(),
        )

    class Meta:
        unique_together=(
            ('from_user', 'to_user'),
        )