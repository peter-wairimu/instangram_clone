from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.helper import Submit,Layout,Field



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']





class PostForm(forms.ModelForm):
    helper = FormHelper
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'Post'))

    class Meta:
        model = Post
        fields = [
            'image'
            'caption'
        ]
