from django import forms
from django.forms import PasswordInput
from Hr_head.models import Hr_headtable

class Hr_headforms(forms.ModelForm):
    class Meta:
        model=Hr_headtable
        fields="__all__"
        labels={"name":"Name","pas":"Password"}
        widgets={"pas":PasswordInput}