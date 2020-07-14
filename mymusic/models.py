from django.db import models



# Create your models here.
# class User(AbstractUser):
#     pass

class Album(models.Model):
    artist_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    released = models.DateField()
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
    
        # return f'{self.release}"
        