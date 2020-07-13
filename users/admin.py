from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

# move to forms
# name = models.CharField(max_length=255)
#     email = models.EmailField                                null=True,
