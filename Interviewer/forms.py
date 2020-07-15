from django import forms
from Interviewer.models import Interviewertable
from django.forms import PasswordInput

class Interviewerform(forms.ModelForm):
    class Meta:
        model=Interviewertable
        fields="__all__"
        labels={"name":"Name","pas":"Password"}
        widgets={"pas":PasswordInput}
