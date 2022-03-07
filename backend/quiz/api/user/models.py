'''
creates the model for user app
'''
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    """
        A class to represent CustomUser.

        ...

        Attributes
        ----------
        username : char
            username of the user for login
        first_name : char
            first name of the user
        last_name : char
            last name of the user
        email : email
            email of the user
        created_at : datetime field
            specifies the date and time when user is created
        updated_at : datetime field
            updates the date and time on updation on data

    """
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    REQUIRED_FIELDS = []

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        A class that defines name of table in DB and in django admin
        '''
        db_table = 'user'
