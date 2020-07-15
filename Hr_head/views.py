from django.shortcuts import render,redirect
from Hr_head.forms import Hr_headforms

def hr_headpage(request):
    return render(request,"Hr_head/hr_headpage.html",{"hrhead":Hr_headforms})