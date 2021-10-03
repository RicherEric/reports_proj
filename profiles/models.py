from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')
    avator = models.ImageField(upload_to='avators', default='NIP.png')
    # auto_now_add -> fixed value
    created = models.DateTimeField(auto_now_add=True)
    # auto_now - > updated value
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"