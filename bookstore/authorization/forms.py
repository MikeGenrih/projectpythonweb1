from django import forms
from django.contrib.auth.forms import UserCreationForm



from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)




class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password',]






# class CustomUser(UserCreationForm):
#     class  Meta:
#         medel = User
#         fields = ('username', 'password',)
#         widgets = {
#             'username': forms.TextInput(attrs={'class':'form-input'}),
#             'password':forms.PasswordInput(attrs={'class':'form-input'}),
#         }