from django import forms
from . models import Mystery, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class MysteryForm(forms.ModelForm):
    class Meta:
        model = Mystery
        fields = ['title', 'image', 'description', 'answer', 'category']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
        }


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUser(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
