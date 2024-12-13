from django import forms
from .models import Users

class login_form(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username','password',)


class regist_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    email = forms.EmailField()
    retype_password = forms.CharField(max_length=20)
