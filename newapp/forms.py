from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class UserForm(forms.ModelForm):

    password = forms.CharField(max_length=200,widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200,widget=forms.PasswordInput())

    class Meta:

        model = User
        fields = ['first_name','last_name','username','email','password','confirm_password']
       
    def clean(self):   

        cleaned_data = super(UserForm, self).clean()
        get_password = cleaned_data.get('password')
        get_confirm_password = cleaned_data.get('confirm_password')

        if get_password != get_confirm_password:
            raise forms.ValidationError("password and confirmation password dont match")

class AuthForm(forms.Form):

    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200,widget=forms.PasswordInput())

    class Meta:

        fields = ['username','password']

    def clean(self,*args,**kwargs):

        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
            
        user=authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("Incorrect username and password")


