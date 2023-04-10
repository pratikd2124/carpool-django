from django.db import models
import geocoder
from authentication.models import User
# Create your models here.
token = 'sk.eyJ1IjoiaHJpdGhpazczNzgiLCJhIjoiY2xldjZvNzdqMXd5ajN5cDRiczBtZTc5eiJ9.zTWI4wn4nYSFC07frUmTTA'
class createRideLoc(models.Model):
    did = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    autodate = models.DateTimeField(auto_now=True)
    from_address =  models.TextField()
    from_lat = models.FloatField(blank=True,null=True)
    from_long = models.FloatField(blank=True,null=True)
    to_address =  models.TextField(null=True)
    to_lat = models.FloatField(blank=True,null=True)
    to_long = models.FloatField(blank=True,null=True)
    date =  models.DateField(blank=True,null=True)
    time = models.TimeField(blank=True,null=True)
    no_of_seats = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)

    yr =models.CharField(max_length=100,blank=True,null=True)
    car = models.CharField(max_length=100,blank=True,null=True)
    model =models.CharField(max_length=100,blank=True,null=True)
    fueltype =models.CharField(max_length=100,blank=True,null=True)
    qrlink = models.URLField(null=True, blank=True)
    upid = models.CharField(max_length=1000,null=True, blank=True)

    available_seats = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
    # def save(self,*args, **kwargs):
    #     g = geocoder.mapbox(self.from_address,key=token)
    #     g =g.latlng
    #     self.from_lat = g[0]
    #     self.from_long = g[1]
    #     g = geocoder.mapbox(self.to_address,key=token)
    #     g =g.latlng
    #     self.to_lat = g[0]
    #     self.to_long = g[1]


    #     return super(createRideLoc,self).save(*args, **kwargs)


class request_ride_data(models.Model):
    did = models.ForeignKey(User, on_delete=models.CASCADE)
    ride_id = models.ForeignKey(createRideLoc,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    pickup = models.CharField(max_length=1000)
    drop = models.CharField(max_length=1000)
    booked = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
