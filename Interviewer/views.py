from django.shortcuts import render,redirect
from Interviewer.forms import Interviewerform
from Interviewer.models import Interviewertable
from django.contrib import messages

def interviewerpage(request):
    return render(request, 'Interviewer/interviewerpage.html',{"interviewer":Interviewerform})
def interviewerhome(request):
    x=request.POST.get("name")
    y=request.POST.get("pas")
    try:
        Interviewertable.objects.get(name=x,pas=y)
        return render(request,'Interviewer/interviewerhome.html')
    except Interviewertable.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect("interviewerpage")



