'''
 display user app  models in the Django admin panel
'''
from django.contrib import admin
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser)
