from django.db import models

class User(models.Model):
    idx = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    create_dt = models.DateTimeField(auto_now=True)
    update_dt = models.DateTimeField(auto_now=True)