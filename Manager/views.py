from django.shortcuts import render,redirect
from Manager.forms import Mangerform
from Manager.models import Managertable
from django.contrib import messages

def managerpage(request):
    return render(request, 'Manager/managerpage.html', {"Manager":Mangerform})
def managerhome(request):
    x=request.POST.get("name")
    y=request.POST.get("pas")
    try:
        Managertable.objects.get(name=x,pas=y)
        return render(request,'Manager/managerhome.html')
    except Managertable.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect("managerpage")
