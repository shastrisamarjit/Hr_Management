from django.db import models

class Admintable(models.Model):
    name=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)
