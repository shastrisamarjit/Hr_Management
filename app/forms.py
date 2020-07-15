from django import forms
from app.models import Admintable
from django.forms import PasswordInput

class Adminform(forms.ModelForm):
    class Meta:
        model=Admintable
        fields="__all__"
        labels={"name":"Name","pas":"Password"}
        widgets={"pas":PasswordInput}
