'''
 display results app  models in the Django admin panel
'''
from django.contrib import admin
from .models import Result
# Register your models here.
admin.site.register(Result)
