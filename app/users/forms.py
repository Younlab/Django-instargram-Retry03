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

    profile_image = forms.ImageField(
        required=True,
    )

    # gender = forms.ChoiceField(
    #     widget=forms.ChoiceField(required=True)
    # )

    email = forms.EmailField(label='E-mail')


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
        username = self.cleaned_data['username']
        password = self.cleaned_data['password2']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        profile_image = self.cleaned_data['profile_image']
        user = User.objects.create_user(
            username=username,
            password=password,
            last_name=name,
            email=email,
            profile_image=profile_image,
            gender=gender,
        )
        return user