from django.contrib import admin 

# Register your models here.
from .models import UserProfile, menu


admin.site.register(UserProfile)
admin.site.register(menu)
