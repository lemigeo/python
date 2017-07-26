from django.db import models

class User(models.Model):
    idx = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    create_dt = models.DateTimeField(auto_now=True)
    update_dt = models.DateTimeField(auto_now=True)