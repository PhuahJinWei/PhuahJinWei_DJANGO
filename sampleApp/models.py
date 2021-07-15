from django.db import models

class user(models.Model):
    email = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    role = models.CharField(max_length = 10)