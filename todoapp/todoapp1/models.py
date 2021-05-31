from django.db import models

# Create your models here.
class Formsayfasi(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField()
    message1=models.TextField(max_length=200)
    message2=models.TextField()
