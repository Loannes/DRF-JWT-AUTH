from django.db import models
from django.conf import settings
from account.models import User

class Post(models.Model):
    id         = models.AutoField(primary_key=True, null=False, blank=False) 
    user       = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title      = models.CharField(max_length=100)
    body       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    