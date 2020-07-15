from django.shortcuts import render,redirect
from app.forms import Adminform
from app.models import Admintable
from django.contrib import messages


def adminpage(request):
    return render(request,'app/adminpage.html',{"Admin":Adminform})
def adminhome(request):
    x=request.POST.get("name")
    y=request.POST.get("pas")
    try:
        Admintable.objects.get(name=x,pas=y)
        return render(request, 'app/adminhome.html')
    except Admintable.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect("adminpage")

