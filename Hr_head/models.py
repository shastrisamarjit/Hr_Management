from django.db import models

class Hr_headtable(models.Model):
    name=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)