from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate,login
from embed_video.fields import EmbedVideoField




def first(request):
    return render(request, 'Front_Page.html')

def about(request):
    return render(request, 'about.html')
#right: -120%;
#    bottom:100%;
 #   height:100%;
  #  width:345%;
