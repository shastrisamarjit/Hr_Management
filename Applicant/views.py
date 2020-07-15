from django.shortcuts import render,redirect
from Applicant.forms import Applicantform,Applicantregister,Registrationform,Applicanttable
from django.contrib import messages

def applicantpage(request):
    return render(request,'Applicant/applicantpage.html',{"applicant":Applicantform})
def applicantlogin(request):
    x=request.POST.get("name")
    y=request.POST.get("pas")
    try:
        Applicanttable.objects.get(name=x,pas=y)
        return render(request,'Applicant/applicanthome.html')
    except Applicanttable.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect("applicantpage")
def appregister(request):
    return render(request,'Applicant/registrationpage.html',{"register":Registrationform})
def applicantsubmit(request):
    #af=Applicantform(request.POST) af.is_valid() and
    rf=Registrationform(request.POST)
    if rf.is_valid():
        #af.save()
        rf.save()
        messages.success(request,"Registered Successfully")
        return redirect("applicantpage")
    else:
        return render(request,"Applicant/registrationpage.html",{"register":rf})

