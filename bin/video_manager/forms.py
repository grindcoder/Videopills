from django import forms
from django.contrib.auth.models import User
from video_manager.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def is_valid(self):
        if not self.data['password'] == self.data['confirm_password'] :
            self.add_error( 'password' , 'Le password non coincidono' )

        return super(UserForm,self).is_valid()




class UserProfileForm(forms.ModelForm):
    pills_preferiti = forms.ModelChoiceField(VideoContainer.objects.all())

    class Meta:
        model = UserProfile
        fields = ('pills_preferiti',)