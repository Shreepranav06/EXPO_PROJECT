from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Teacher






def teachers(request):



    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Teacher.objects.get(name = name, password = password)


            return render(request, 'teacherview.html',{'name':user.name})

        except Teacher.DoesNotExist:
            return redirect('http://127.0.0.1:8000/teacher')

    return render(request, 'teacher.html')

