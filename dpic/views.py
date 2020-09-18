from django.shortcuts import render
from django.http import HttpResponse

import instaloader
import shutil
import cv2
import glob
from django.conf import settings
from .models import Instapic
from .serializers import InstapicSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from os import listdir
from os.path import isfile, join

def home(request):
    return render(request,"index.html");


@api_view(['GET', 'POST'])
def addsome(request):
    if request.method == 'GET':
        print('get method')
        print(request.data)
        data = request.data 
        serializer = InstapicSerializer(data=data)
        if serializer.is_valid():
            foldername= 'pics/'+data['pic_user_name']
            root = instaloader.Instaloader(dirname_pattern=foldername,filename_pattern='picvc',save_metadata=False,compress_json =False)
            user_name = data['pic_user_name']
            pr=root.download_profile(user_name,profile_pic_only=True)
            print(pr)
            serializer.save()
            mediapath = settings.MEDIA_ROOT+'/'+data['pic_user_name']+'/'
            myfiles = [ f for f in listdir(mediapath) if isfile(join(mediapath, f))]
            print(myfiles[0])
            user_img= '/pics/'+data['pic_user_name']+'/'+myfiles[0]
            return Response(user_img)
        else:
            return Response('null')
        return Response(serializer.errors, status=200)
            

    if request.method == 'POST':
        print('post method')
        data = request.data 
        serializer = InstapicSerializer(data=data)
        if serializer.is_valid():
            foldername= 'pics/'+data['pic_user_name']
            root = instaloader.Instaloader(dirname_pattern=foldername,filename_pattern='picvc',save_metadata=False,compress_json =False)
            user_name = data['pic_user_name']
            pr=root.download_profile(user_name,profile_pic_only=True)
            print(pr)
            serializer.save()
            mediapath = settings.MEDIA_ROOT+'/'+data['pic_user_name']+'/'
            myfiles = [ f for f in listdir(mediapath) if isfile(join(mediapath, f))]
            print(myfiles[0])
            user_img= '/pics/'+data['pic_user_name']+'/'+myfiles[0]
            return Response(user_img)
        else:
            return Response('null')
        return Response(serializer.errors, status=200)
