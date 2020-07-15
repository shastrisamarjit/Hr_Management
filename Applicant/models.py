from django.db import models

class Applicanttable(models.Model):
    name=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)

class Applicantregister(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField(max_length=40)
    gen=models.CharField(max_length=10)
    con=models.IntegerField(primary_key=True)
    addr=models.CharField(max_length=60)
    usrname=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)