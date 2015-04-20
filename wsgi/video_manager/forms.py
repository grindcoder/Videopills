from django import forms
from django.contrib.auth.models import User
from video_manager.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    pills_preferiti = forms.ModelChoiceField(VideoContainer.objects.all())

    class Meta:
        model = UserProfile
        fields = ('pills_preferiti',)