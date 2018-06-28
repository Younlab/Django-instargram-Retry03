from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class SignupForm(forms.Form):
    username = forms.CharField(label='ID')

    name = forms.CharField(label='Name')

    password = forms.CharField(label='Password',
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(label='Agein Password',
        widget=forms.PasswordInput()
    )

    profile_image = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(),
    )

    gender = forms.ChoiceField(
        widget=forms.Select(
        ),
        required=False,
        choices=User.CHOICES_GENDER,
    )

    site = forms.URLField(
        widget=forms.URLInput(),
        required=False,
    )

    # gender = forms.ChoiceField(
    #     widget=forms.ChoiceField(required=True)
    # )

    email = forms.EmailField(label='E-mail', required=False)

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            self.add_error('password2', '비밀번호가 일치하지 않습니다.')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user.exists():
            raise ValidationError('이미 중복된 ID 가 존재합니다.')
        else:
            return username

    def sign_up(self):
        field = [
            'username',
            'email',
            'password',
            'gender',
            'site_url',
            'profile_image',
            'last_name',
        ]

        create_user_dict = {}
        # for key, value in self.cleaned_data.items():
        #     if key in field:
        #         create_user_dict[key] = value

        # 딕셔너리 컴프리핸션
        # create_user_dict = {key:value for key, value  in self.cleaned_data.items() if key in field}
        #
        # def in_fields(item):
        #     return item[0] in field

        # result = filter(in_fields, self.cleaned_data.items())
        #
        # for item in result:
        #     create_user_dict[item[0]] = item[1]
        # return

        # filter 결과를 dict함수로 묶어서 새 dict로 생성
        # create_user_dict = dict(filter(in_fields, self.cleaned_data.items()))

        #lamda
        create_user_dict = dict(filter(lambda item: item[0] in field, self.cleaned_data.items()))

        user = User.objects.create_user(**create_user_dict)
        # username = self.cleaned_data['username']
        # password = self.cleaned_data['password2']
        # name = self.cleaned_data['name']
        # email = self.cleaned_data['email']
        # profile_image = self.cleaned_data['profile_image']
        # gender = self.cleaned_data['gender']
        # site = self.cleaned_data['site']
        # user = User.objects.create_user(
        #     username=username,
        #     password=password,
        #     last_name=name,
        #     email=email,
        #     profile_image=profile_image,
        #     gender = gender,
        #     site_url=site,
        #
        # )
        return user