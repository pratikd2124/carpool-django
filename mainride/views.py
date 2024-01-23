import requests
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import *
from carpooling import settings
import uuid
from test import payment
from django.contrib import messages

# Create your views here.
def createride(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'cancel' in request.POST:
                request.session.flush()
                return redirect('mapview')
            
            if 'confirm' in request.POST:
                no_seats= int(request.POST.get('no_seats'))
                price= request.POST.get('price')
                yr= request.POST.get('yr')
                car= request.POST.get('car')
                model= request.POST.get('model')
                fueltype= request.POST.get('fueltype')
                insured= request.POST.get('insured')
                upi = request.POST.get('upi')
                if insured == None:
                    
                    return redirect('mapview')

                user =request.user
                ride = createRideLoc.objects.create(did = user,from_address=request.session['createride']['from_address'],to_address=request.session['createride']['to_address'],from_lat=request.session['createride']['from_lat'],from_long=request.session['createride']['from_long'],to_lat=request.session['createride']['to_lat'],
                                                    upid=upi,to_long=request.session['createride']['to_long'],date=request.session['createride']['date'],time=request.session['createride']['time'],price=price,yr=yr,car=car,model=model,fueltype=fueltype,no_of_seats=no_seats,available_seats=no_seats)

                link = payment(upi,price,ride.id)
                ride.qrlink = link
                ride.save()
                messages.success(request,"Ride Saved Successfully")
                return redirect('postview')
    return redirect('userlogin')


def request_ride(request,pk):
    try:
        ride = get_object_or_404(createRideLoc,id=pk)
        print(ride)
        req = request_ride_data.objects.filter(ride_id=pk,did=request.user).count()
        print(req)
        if req != 0:
            messages.error(request,"You have already requested for this Ride")
            return redirect('postview')
    except Exception as e:
        print(e)

    if request.user.is_authenticated:
        try:
            del request.session['request_ride']
        except:
            pass
        if request.method == "POST":
            pickup_point = request.POST.get('pickup_point')
            drop_point = request.POST.get('drop_point')
            access_token = settings.MAPBOX_ACCESS_TOKEN
            g = geocoder.mapbox(pickup_point,key=access_token)
            g =g.latlng
            pickup_lat = g[0]
            pickup_long = g[1]
            g = geocoder.mapbox(drop_point,key=access_token)
            g =g.latlng
            drop_lat = g[0]
            drop_long = g[1]

            

          
            request.session['request_ride'] = {
                                    'pickup_point':pickup_point,
                                    'drop_point':drop_point,
                                   
                                    'pickup_lat':pickup_lat,
                                    'pickup_long':pickup_long,
                                    
                                    'drop_lat':drop_lat,
                                    'drop_long':drop_long,

                                }
            print("saved!!!!!!!!!!!!!",pickup_lat,pickup_long)
            ride = get_object_or_404(createRideLoc,id=pk)
            request_ride = request_ride_data.objects.create(
                did =request.user,ride_id = ride,pickup = pickup_point,drop = drop_point
            )
            request_ride.save()
            messages.success(request,"Booking request Pending!! You Can Talk with Driver")

            return redirect('postview')
        
        ride = get_object_or_404(createRideLoc,id=pk)
        return render(request,'request_ride.html',{'ride':ride})


    else:
        return redirect('userlogin')    


def dashboard(request):

    user = request.user
    try:
        recent_ride = createRideLoc.objects.order_by('-id').filter(did=user).first()
        all_rides= createRideLoc.objects.all()
        print(recent_ride)
        ride_requests =request_ride_data.objects.filter(ride_id=recent_ride.id)
        users =[]
        for ride in ride_requests:
            user = User.objects.get(id=ride.did.id)
            users.append(user)


        data = {
            'recent_ride':recent_ride,
            'all_rides':all_rides,
        'ride_requests_users': zip(ride_requests, users),
        }

        return render(request,"dashboard.html",data)
    except:
            return render(request,"dashboard.html")


def accept(request,rideid,user):
    user = User.objects.get(id=user)
    ride_request = request_ride_data.objects.get(did =user)
    ride_request.booked = True
    ride_request.save()
    ride=createRideLoc.objects.get(id=rideid)
    ride.available_seats = ride.available_seats-1
    ride.save()
    return redirect('dashboard')


def reject(request,rideid,user):
    user = User.objects.get(id=user)
    ride_request = request_ride_data.objects.get(did =user)
    ride_request.rejected = True
    ride_request.save()
    return redirect('dashboard')

def payD(request,rideid):
    ride = createRideLoc.objects.get(id=rideid)
    return render(request,'pay.html',{'ride':ride})
