from django.db import models

# Create your models here.
class operators(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone=models.TextField(max_length=20)
    profile=models.ImageField(upload_to='profilepics/')

 