from django.urls import path
from .views import *
urlpatterns = [
    path('createride/',createride,name="createride"),
    path('bookride/<int:pk>',request_ride,name='request_ride'),
    path('dashboard/',dashboard,name='dashboard'),
    path('accept/<str:rideid>/<str:user>',accept,name='accept'),
    path('reject/<str:rideid>/<str:user>',reject,name='reject'),
    path('payment/<int:rideid>/',payD,name="paymentdetails")

]