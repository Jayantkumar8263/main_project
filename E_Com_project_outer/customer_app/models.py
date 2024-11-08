from django.db import models
from django.contrib.auth.models import AbstractUser
from customer_app.manager import custom_userManager
from django.utils.translation import gettext_lazy

# Create your models here.
# dhawal
class custom_user(AbstractUser):
    username = None  # Remove username field
    name = models.CharField(max_length=50, unique=True)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=250)
    
    objects = custom_userManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email','mobile']
    
    def __str__(self):
        return self.name
       
class bank_details(models.Model):
     account = models.CharField(max_length=50)
     bank_name = models.CharField(max_length=50)
     IFSC = models.CharField(max_length=50)