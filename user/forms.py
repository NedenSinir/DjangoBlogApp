from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanici Ad",required=True)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput,label="Parola",required=True)
    passwordConfirm=forms.CharField(max_length=20,widget=forms.PasswordInput,label="Parola Dogrula",required=True)
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        passwordConfirm= self.cleaned_data.get("passwordConfirm")
        if password != passwordConfirm:
            raise ValidationError
        values={
            "username1":username,
            "password":password

        }
        return values
class LoginFrom(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanici Adi:",required=True)
    password = forms.CharField(max_length=20,label="Sifre : ",widget=forms.PasswordInput,required=True)
        