from django.db import models

# Create your models here.
# class User(AbstractUser):
#     pass

class Album(models.Model):
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    released = models.DateField()
    
    def __str__(self):
        return f"{self.title} by {self.artist_name}"
    
        # return f'{self.release}"
        