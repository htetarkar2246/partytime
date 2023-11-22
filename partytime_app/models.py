from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone =  models.CharField(max_length=30)
    message = models.TextField(max_length=500,null = True)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000000)
    uploaded_time = models.DateTimeField(default=datetime.now, blank=True)
    
class Service(models.Model):
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'images/')
    service = models.CharField(max_length=100)