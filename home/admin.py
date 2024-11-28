from django.contrib import admin 

# Register your models here.
from .models import Menu_items,Restaurant,Orders

admin.site.register(Menu_items)
admin.site.register(Orders)
admin.site.register(Restaurant)
