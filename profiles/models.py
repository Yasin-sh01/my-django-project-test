from django.db import models

class Profile(models.Model):
    Username = models.CharField(max_length=10)
    password = models.TextField()
   # image = models.ImageField()
    created_time = models.DateTimeField()
    
