from django import forms
from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'Username','id':"inputUsername"}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",'type':'password','placeholder':'Password','id':"inputPassword"}))
    class Meta:
        model = User
        fields = ('username','password')

class ChangePasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(user,*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'