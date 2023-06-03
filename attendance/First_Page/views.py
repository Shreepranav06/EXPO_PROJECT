from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate,login
from embed_video.fields import EmbedVideoField




def first(request):
    #video_url = 'https://youtu.be/AYcM_x0BJfA'
    #context = {'video_url': video_url}
    return render(request, 'Front_Page.html')

def about(request):
    return render(request, 'about.html')
