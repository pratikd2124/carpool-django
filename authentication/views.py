
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  ,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from carpooling import settings
from .models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from docverify.models import *
from django.contrib.auth import logout
from mainride.models import *
import geocoder
from django.contrib import messages
from mainride.models import  *


# Create your views here.

def index(request):
    user = User.objects.first
    return render(request, 'index.html',{'user':user}) 
 
def riderhome(request):
    return render(request, 'ridehome.html')  


def logout_view(request):
    logout(request)
    return redirect('userlogin')

def profilereview(request):
    return render(request, 'profilereview.html')  

def postview(request):
    rides = createRideLoc.objects.order_by('-id').all()

    return render(request, 'posts.html',{'rides':rides}) 

def chatview(request):
    if request.user.is_authenticated:
        return render(request, 'chat.html') 
    else:
        return redirect('userlogin')
def mapview(request):
        if request.user.is_authenticated:
            user = request.user
            try:
                drivinglic = drivingmodel.objects.get(did=user.id)
                if drivinglic.verified :
                    if request.method == 'POST':
                
                                from_address = request.POST.get('from_add')
                                to_address = request.POST.get('to_add')
                                date = request.POST.get('date')
                                Time = request.POST.get('time')
                                access_token = settings.MAPBOX_ACCESS_TOKEN
                                g = geocoder.mapbox(from_address,key=access_token)
                                g =g.latlng
                                from_lat = g[0]
                                from_long = g[1]

                                g = geocoder.mapbox(to_address,key=access_token)
                                g =g.latlng
                                to_lat = g[0]
                                to_long = g[1]
                                print(date,Time)
                                request.session['createride'] = {
                                    'from_address':from_address,
                                    'to_address':to_address,
                                    'date':date,
                                    'time':Time,
                                    'from_lat':from_lat,
                                    'from_long':from_long,
                                    
                                    'to_lat':to_lat,
                                    'to_long':to_long,

                                }
                                coordinates={
                                    'from_lat':from_lat,
                                    'from_long':from_long,
                                    
                                    'to_lat':to_lat,
                                    'to_long':to_long,
                                }    

                                context = {'coordinates': coordinates, 'access_token': access_token}
                                return render(request, 'map.html', context)

                    return render(request, 'map.html')
                else:
                    messages.error(request,"Your Driving Licence is not Verified!!")
                    return redirect('home')
            except:
                    messages.error(request,"Your Driving Licence is not Verified!!")
                    return redirect('home')
        else:
            
            return redirect('userlogin')

def signup(request): 
    
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        full_name = request.POST.get("fname")
        email = request.POST.get("email")
        phone_no= request.POST.get('phonenumber')
        add = request.POST.get('add')

        state = request.POST.get('state')
        city = request.POST.get('city')
        zip = request.POST.get('zipcode')

        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        # Fields Cannot be None or Empty #
        
        if pass1 == None or pass1 == "":
            messages.warning(request, f'Please Fill Password.')
            return redirect('signup')
        if pass1 != pass2:
            messages.warning(request, f'Password Not Match.')
            return redirect('signup')

      


        if User.objects.filter(username=email).exists():
            messages.warning(request, f'This Email Already Exists.')
            return redirect('signup')

        # Create User #
        user = User.objects.create(
                fname = full_name,
                email = email,
                username = email,
                add =add,
                state = state,
                city = city,
                zipcode =zip,

                phonenumber = phone_no,
                )
        user.set_password(pass1)
        user.save()
        return redirect('userlogin')


    return render(request, 'signup.html')  

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('pass')
            print(email,password)
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('userprofile'))
            else:
                return HttpResponse('Invalid login credentials.')
        else:
            return render(request, 'login.html')


def userprofile(request):
    
    if request.user.is_authenticated:
        user = request.user
        if aadharmodel.objects.filter(did=user).exists():
            aadhar = aadharmodel.objects.get(did = user)
        else:
            aadhar =None
        if drivingmodel.objects.filter(did=user).exists():
            drivinglic=drivingmodel.objects.get(did = user)
        else:
            drivinglic=None
        if panmodel.objects.filter(did=user).exists():
            pan = panmodel.objects.get(did = user)
        else:
            pan= None

        print(aadhar,pan,drivinglic)
        param={
                'aadhar': aadhar,
                'pan' :pan,
                'drivinglic':drivinglic

            }
        return render(request,'profile.html',param)
    else:
        messages.warning(request,"Please Login ")

        return redirect('userlogin')


def rideDtails(request):
    user = request.user
    prevridedetail= request_ride_data.objects.order_by('-id').filter(did=user.id).first()
    print(prevridedetail)
    prevride = createRideLoc.objects.get(id=prevridedetail.ride_id.id)

    allprevdetails = request_ride_data.objects.order_by('-id').filter(did=user.id)
    allprevrides = []
    for i in allprevdetails:
            prevride = createRideLoc.objects.get(id=i.ride_id.id)
            allprevrides.append(prevride)


    data = {
        'prevride':prevride,
        'prevridedetail':prevridedetail,
        'allprevdetails':allprevrides
    }
    return render(request,'prevridedetails.html',data)