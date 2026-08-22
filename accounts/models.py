from django.db import models

class Accounts(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()
