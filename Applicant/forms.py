from django import forms
from Applicant.models import Applicanttable,Applicantregister
from django.forms import PasswordInput,EmailInput,NumberInput

class Applicantform(forms.ModelForm):
    class Meta:
        model=Applicanttable
        fields="__all__"
        labels={"name":"Name","pas":"Password"}
        widgets={"pas":PasswordInput}
class Registrationform(forms.ModelForm):
    class Meta:
        model=Applicantregister
        fields="__all__"
        labels={"name":"Name","dob":"D.O.B","email":"Email","gen":"Gender","con":"ContactNo",
                "addr":"Address","usrname":"UserName","pas":"Password"}
        widgets={"pas":PasswordInput(),"email":EmailInput(),"con":NumberInput()}