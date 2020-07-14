from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    pass

class Album():
    artistname = models.CharField(max_length=255)
    albumtitle = models.CharField(max_length=255)
    released = models.DateField()
    
    def __str__(self):
        return f"{self.album.title}"