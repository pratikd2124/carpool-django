
# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname=models.CharField(max_length=25)
    phonenumber=models.CharField(max_length=12)

    add= models.TextField()
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=7)
    active = models.BooleanField(default=False)
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_set', blank=True,null=True
    # )

    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_set',blank=True,null=True
    # )

    def __str__(self):
        return str(self.id)



        
    