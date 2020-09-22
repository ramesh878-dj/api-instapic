from django.shortcuts import render
from django.http import HttpResponse

import instaloader
import shutil
# import cv2
# import glob
from django.conf import settings
from .models import Instapic
from .serializers import InstapicSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from os import listdir
from os import rmdir
from os.path import isfile, join

def home(request):
    return render(request,"index.html");


@api_view(['GET', 'POST'])
def addsome(request):
    if request.method == 'GET':
        print('get method')
        # user_name = Instapic.objects.all()
        # serializer= InstapicSerializer(user_name, many=True)
        # shutil.rmtree('/ramesh__878')
        # dirpath='pics/ramesh__878pics/*.jpg'
        # mediapath = settings. MEDIA_ROOT+'/ramesh__878pics/'
        # myfiles = [ f for f in listdir(mediapath) if isfile(join(mediapath, f))]
        # print(myfiles[0])
        return Response(status=200)
            

    if request.method == 'POST':
        print('post method')
        data = request.data 
        serializer = InstapicSerializer(data=data)
        if serializer.is_valid():
            foldername= 'pics/'+data['pic_user_name']
            try:
                shutil.rmtree(foldername)
                print('Delete old Profile picture')
            except:
                print("Error when delete old profie picture")
            root = instaloader.Instaloader(dirname_pattern=foldername,filename_pattern='picvc',save_metadata=False,compress_json =False)
            user_name = data['pic_user_name']
            pr=''
            valid=0
            try:
                pr=root.download_profile(user_name,profile_pic_only=True)
                print(pr)
                valid=1
            except:
                print("Username is wrong")
            if pr =='':
                print('wrong username')
            else:
                print('correct username')
            if valid==1:
                mediapath = settings.MEDIA_ROOT+'/'+data['pic_user_name']+'/'
                myfiles = [ f for f in listdir(mediapath) if isfile(join(mediapath, f))]
                print(myfiles[0])
                user_img= '/pics/'+data['pic_user_name']+'/'+myfiles[0]
                return Response(user_img)
            else:
                return Response("wrong")
        else:
            return Response('null')
        return Response(serializer.errors, status=200)
