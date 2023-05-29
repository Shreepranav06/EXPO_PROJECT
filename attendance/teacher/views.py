from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Teacher






def teachers(request):

    if request.method == "POST":
        nam = request.POST.get('name')
        passwor = request.POST.get('password')

        try:
            user = Teacher.objects.filter(name=nam, password=passwor).first()
            if user is not None:

                return redirect('http://127.0.0.1:8000/update_attendance/')
                #return render(request,'details.html')


            else:
                messages.error(request, 'User not found')
        finally:
            pass





    return render(request, 'teacher.html')

