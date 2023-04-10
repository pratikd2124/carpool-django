from django.urls import path
from .views import *
urlpatterns = [
    path('aadhar/',aadhar,name='aadhar'),
    path('pan/',pan,name='pan'),
    path('drivinglic/',drivinglic,name='drivinglic')

]