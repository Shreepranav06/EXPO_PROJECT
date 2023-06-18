from django.shortcuts import render
import mysql.connector as sql
import smtplib
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Email
from .forms import StudentForm
from details.models import Bus

import requests




def email(request):

    if request.method == "POST":
        name = request.POST.get('student_name')
        user = Email.objects.filter(student_name=name).values()
        for s in user:
            c = s['email']
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()  # establishes connection with the SMTP server
            smtp.starttls()  # data encryption
            smtp.ehlo()

            smtp.login('alumni.management.sys@gmail.com','iyovwrjpfkxgajiu')
             # logs in the mail ID with SMTP server

            subject = f'Attendance Info'
            body = f'You have been absent for the current session.'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail('alumni.management.sys@gmail.com', c, msg)
            print('Password reset information sent to admin mail successfully\n\n')
            Email.objects.filter(student_name=name).update(attendance_status=False)

            return render(request, 'teacher.html')


    else:
        pass


    return render(request, 'details.html')

def student(request):
    if request.method == "POST":
        number = request.POST.get('register_number')
        password = request.POST.get('password_student')


        try:
            user = Email.objects.filter(register_number=number, password_student=password).first()
            if user is not None:
                st = Email.objects.filter(register_number=number).values()
                for i in st:
                    q=i
                k=q['attendance_status']

                if k == True:
                    return redirect('http://127.0.0.1:8000/info')
                else:
                    return redirect('http://127.0.0.1:8000/infowrong')





            else:
                return redirect('http://127.0.0.1:8000/infowrong')

        finally:
            pass





    return render(request, 'student.html')


def info(request):
    return render(request,'info.html')


def infowrong(request):
    return render(request,'infowrong.html')


def update_attendance(request):
    if request.method == 'POST':
        selected_names = request.POST.getlist('student_name')

        for selected_name in selected_names:
            try:
                student = Email.objects.get(student_name=selected_name)
                student.attendance_status = False
                c = student.email
                student.save()

                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login('alumni.management.sys@gmail.com', 'iyovwrjpfkxgajiu')

                    subject = f'Attendance Info'
                    body = f'You have been absent for the current math session.'

                    msg = f'Subject: {subject}\n\n{body}'

                    smtp.sendmail('alumni.management.sys@gmail.com', c, msg)
                    print('Password reset information sent to admin mail successfully\n\n')

            except Email.DoesNotExist:
                return redirect('http://127.0.0.1:8000/info')

    student_names = Email.objects.values_list('student_name', flat=True)

    context = {
        'student_names': student_names
    }

    return render(request, 'button.html', context)






def update_attendance_a(request):
    if request.method == 'POST':
        selected_names = request.POST.getlist('student_name')

        for selected_name in selected_names:
            try:
                student = Email.objects.get(student_name=selected_name)
                student.attendance_status_a = False
                c = student.email
                student.save()

                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login('alumni.management.sys@gmail.com', 'iyovwrjpfkxgajiu')

                    subject = f'Attendance Info'
                    body = f'You  have been absent for the current python session.'

                    msg = f'Subject: {subject}\n\n{body}'

                    smtp.sendmail('alumni.management.sys@gmail.com', c, msg)
                    print('Password reset information sent to admin mail successfully\n\n')

            except Email.DoesNotExist:
                return redirect('http://127.0.0.1:8000/info')

    student_names = Email.objects.values_list('student_name', flat=True)

    context = {
        'student_names': student_names
    }

    return render(request, 'button1.html', context)




def update_attendance_b(request):
    if request.method == 'POST':
        selected_names = request.POST.getlist('student_name')

        for selected_name in selected_names:
            try:
                student = Email.objects.get(student_name=selected_name)
                student.attendance_status_b = False
                c = student.email
                student.save()

                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login('alumni.management.sys@gmail.com', 'iyovwrjpfkxgajiu')

                    subject = f'Attendance Info'
                    body = f'You  have been absent for the current physics session..'

                    msg = f'Subject: {subject}\n\n{body}'

                    smtp.sendmail('alumni.management.sys@gmail.com', c, msg)
                    print('Password reset information sent to admin mail successfully\n\n')

            except Email.DoesNotExist:
                return redirect('http://127.0.0.1:8000/info')

    student_names = Email.objects.values_list('student_name', flat=True)

    context = {
        'student_names': student_names
    }

    return render(request, 'button2.html', context)


def studentview(request):
    if request.method == "POST":
        number = request.POST.get('register_number')
        password = request.POST.get('password_student')
        #mark = request.POST.get('marks')

        try:
            user = Email.objects.get(register_number=number, password_student=password)



            sum = 0
            count = 3
            p1=0
            p2=0
            p3=0

            if user.attendance_status == True:
                p1+=1
                sum += 1
            if user.attendance_status_a == True:
                p2+=1
                sum += 1
            if user.attendance_status_b == True:
                p3+=1
                sum += 1

            per = (sum * 100) / count
            pe=round(per,2)

            user.total = pe
            p4 = p1*100
            p5 = p2*100
            p6 = p3*100
            p7= round(p4,2)
            p8 = round(p5, 2)
            p9 = round(p6, 2)
            user.period_one = p7
            user.period_two = p8
            user.period_three = p9
            a = user.math_mark
            b = user.python_mark
            c = user.physics_mark
            d = (a+b+c)/3
            e = d/10
            user.cgpa=e
            user.save()

            return render(request, 'studentview.html',
                          {'per': pe, 'student_name': user.student_name, 'register_number': user.register_number,'p1': p7,'p2': p8,'p3': p9,'mark': e,'img_url': user.img.url,'mark1':user.math_mark,'mark2':user.python_mark,'mark3':user.physics_mark})

        except Email.DoesNotExist:
            return redirect('http://127.0.0.1:8000/infowrong')

    return render(request, 'student.html')

def mark(request):
    if request.method == 'POST':
        students = Email.objects.all()

        for student in students:
            CGPA = request.POST.get(f"CGPA_{student.id}", None)
            if CGPA is not None:
                student.CGPA = CGPA
                student.save()


        #return redirect('http://127.0.0.1:8000/info')

    students = Email.objects.all()

    context = {
        'students': students
    }

    return render(request, 'marks.html', context)

def bus_view(request):
    if request.method == "POST":
        register_number = request.POST.get('register_number')
        password_student = request.POST.get('password_student')
        bus_code = request.POST.get('bus_code')

        try:
            user = Email.objects.get( register_number = register_number , password_student =password_student )
            if user is not None:
                return redirect('http://127.0.0.1:8000/map')
            else:
                return redirect('http://127.0.0.1:8000/infowrong')








        finally:
            pass

    return render(request, 'bus.html')


def mark1(request):
    if request.method == 'POST':
        students = Email.objects.all()

        for student in students:
            math_mark = request.POST.get(f"math_mark_{student.id}", None)
            if math_mark is not None:
                student.math_mark = math_mark
                student.save()


        #return redirect('http://127.0.0.1:8000/info')

    students = Email.objects.all()

    context = {
        'students': students
    }

    return render(request, 'marks1.html', context)

def mark2(request):
    if request.method == 'POST':
        students = Email.objects.all()

        for student in students:
            python_mark = request.POST.get(f"python_mark_{student.id}", None)
            if python_mark is not None:
                student.python_mark = python_mark
                student.save()


        #return redirect('http://127.0.0.1:8000/info')

    students = Email.objects.all()

    context = {
        'students': students
    }

    return render(request, 'marks2.html', context)

def mark3(request):
    if request.method == 'POST':
        students = Email.objects.all()

        for student in students:
            physics_mark = request.POST.get(f"physics_mark_{student.id}", None)
            if physics_mark is not None:
                student.physics_mark = physics_mark
                student.save()


        #return redirect('http://127.0.0.1:8000/info')

    students = Email.objects.all()

    context = {
        'students': students
    }

    return render(request, 'marks3.html', context)


def get_current_location(request):
    try:

        bus_object = Bus.objects.get(pk=1)


        latitude = bus_object.north
        longitude = bus_object.east

        # Make a request to the Geocoding API
        api_key = 'YOUR_API_KEY'
        url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}'
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()


        if data['status'] == 'OK':
            results = data['results']
            if results:
                current_location = results[0]['formatted_address']
                # Do something with the current_location
                return HttpResponse(current_location)


        error_message = 'Failed to retrieve current location.'
        return redirect("https://www.google.co.in/maps/place/11%C2%B002'24.9%22N+77%C2%B003'20.9%22E/@11.0402553,77.0532307,17z/data=!4m4!3m3!8m2!3d11.04025!4d77.0558056?entry=ttu")

    except Exception as e:

        print(f"An error occurred: {str(e)}")

        return redirect("https://www.google.co.in/maps/place/11%C2%B002'24.9%22N+77%C2%B003'20.9%22E/@11.0402553,77.0532307,17z/data=!4m4!3m3!8m2!3d11.04025!4d77.0558056?entry=ttu")
