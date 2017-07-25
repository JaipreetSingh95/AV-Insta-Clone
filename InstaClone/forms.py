from django import forms
from models import UserModel, PostModel, LikeModel, CommentModel, DislikeModel
from django.contrib.auth import authenticate, login, logout, get_user_model


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','username','name','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['name','image', 'review']


class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']

class DislikeForm(forms.ModelForm):

    class Meta:
        model = DislikeModel
        fields=['post']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']