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
            body = f'Your ward has been absent for the current session.'

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




                #return render(request,'details.html')


            else:
                messages.error(request, 'User not found')
        finally:
            pass





    return render(request, 'student.html')


def info(request):
    return render(request,'info.html')


def infowrong(request):
    return render(request,'infowrong.html')


def update_attendance(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')

        try:
            student = Email.objects.get(student_name=student_name)
            student.attendance_status = False
            student.save()
            user = Email.objects.filter(student_name=student_name).values()
            for s in user:
                c = s['email']
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()  # establishes connection with the SMTP server
                smtp.starttls()  # data encryption
                smtp.ehlo()

                smtp.login('alumni.management.sys@gmail.com', 'iyovwrjpfkxgajiu')
                # logs in the mail ID with SMTP server

                subject = f'Attendance Info'
                body = f'Your ward has been absent for the current session.'

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail('alumni.management.sys@gmail.com', c, msg)
                print('Password reset information sent to admin mail successfully\n\n')
                Email.objects.filter(student_name=student_name).update(attendance_status=False)

            return redirect('http://127.0.0.1:8000/info')  # Redirect to a success page
        except Email.DoesNotExist:
            return redirect('http://127.0.0.1:8000/infowrong')  # Redirect to an error page if student is not found

        # Fetch the student names from the database
    form = Email.objects.values_list('student_name', flat=True)

    context = {
        'form': form
    }



    return render(request, 'button.html', context)



