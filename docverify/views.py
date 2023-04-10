from django.shortcuts import render,redirect,HttpResponse
from .models import *
import cv2
from pyzbar.pyzbar import decode

from pyaadhaar.utils import Qr_img_to_text, isSecureQr
from pyaadhaar.decode import AadhaarSecureQr
import cv2
from PIL import Image
from pyzbar.pyzbar import decode
# Create your views here.

def verify_aadhaar_from_image(image_path):

    decocdeQR = decode(Image.open(f'media/{image_path}'))
    print(decocdeQR)

    # Extract the Aadhaar number and Name from the decoded data
    # qrData = code[0].data
    # secure_qr = AadhaarSecureQr(int(qrData))
    # decoded_secure_qr_data = secure_qr.decodeddata()
    # aadhaar_number = decoded_secure_qr_data['aadhaar']
    # name = decoded_secure_qr_data['name']

    # # Verify the Aadhaar details using Pyaadhaar
    # print(secure_qr)

def aadhar(request):
    if request.method == 'POST':
        no = request.POST.get('number')
    file = request.FILES.get('file')
    user =request.user
    doc = aadharmodel.objects.create(did=user,aadharimg=file,aadharno=no,verified=True)
    doc.save()
    # verify_aadhaar_from_image(aadharmodel.objects.get(did=user).aadharimg)
    # return HttpResponse("done")
        # if result['success']:
        #     print('Aadhaar verification successful')

        # else:
        #     print('Aadhaar verification failed:', result['message'])

    return redirect('userprofile')

def pan(request):
    if request.method == 'POST':
        print(request.POST)
        no = request.POST.get('number')
        file = request.FILES.get('file')
    
        user =request.user
        doc = panmodel.objects.create(did=user,panimg=file,panno=no,verified=True)
        doc.save()

    return redirect('userprofile')

def drivinglic(request):
    if request.method == 'POST':
        no = request.POST.get('number')
        file = request.FILES.get('file')
    
        user =request.user
        doc = drivingmodel.objects.create(did=user,drivinglicimg=file,drivinglicno=no,verified=True)
        doc.save()
    return redirect('userprofile')

