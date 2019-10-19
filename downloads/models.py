from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Codes
code = uuid
active
used_by = user

'''
class subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    end_date = models.DateTimeField()
