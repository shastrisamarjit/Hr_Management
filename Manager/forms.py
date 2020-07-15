from django import forms
from Manager.models import Managertable
from django.forms import PasswordInput

class Mangerform(forms.ModelForm):
    class Meta:
        model=Managertable
        fields="__all__"
        labels={"name":"Name","pas":"Password"}
        widgets={"pas":PasswordInput}