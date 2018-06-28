from django import forms

from .models import Post


class PostForm(forms.Form):
    photo = forms.ImageField()
    content = forms.CharField()

    def save(self, author):
        return Post.objects.create(
            author=author,
            photo=self.cleaned_data['photo'],
            content=self.cleaned_data['content'],
        )

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'content']