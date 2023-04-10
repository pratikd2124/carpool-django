from django.db import models
from authentication.models import User
# Create your models here.
class aadharmodel(models.Model):
    def upload_to(instance,filename):
            
        return 'aadhar/%s.jpg' %(instance.did.id)
    did = models.ForeignKey(User,on_delete=models.CASCADE)
    aadharimg = models.ImageField(upload_to=upload_to,null=True,blank=True)
    aadharno = models.CharField(max_length=12,null=True,blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.did.id)
    
class panmodel(models.Model):
    def upload_to(instance,filename):
            
        return 'pan/%s.jpg' %(instance.did.id)
    did = models.OneToOneField(User,on_delete=models.CASCADE)
    panimg = models.ImageField(upload_to=upload_to,null=True,blank=True)
    panno = models.CharField(max_length=12,null=True,blank=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return str(self.did.id)
    
class drivingmodel(models.Model):
    def upload_to(instance,filename):
            
        return 'drivinglic/%s.jpg' %(instance.did.id)
    did = models.OneToOneField(User,on_delete=models.CASCADE)
    drivinglicimg = models.ImageField(upload_to=upload_to,null=True,blank=True)
    drivinglicno = models.CharField(max_length=12,null=True,blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.did.id)

