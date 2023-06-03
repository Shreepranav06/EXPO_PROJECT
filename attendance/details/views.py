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
                    body = f'Your  have been absent for the current python session.'

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
                    body = f'Your  have been absent for the current physic session..'

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
            user.save()

            return render(request, 'studentview.html',
                          {'per': pe, 'student_name': user.student_name, 'register_number': user.register_number,'p1': p7,'p2': p8,'p3': p9,'mark':user.CGPA,'img_url': user.img.url})

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

        # Redirect to a success page or perform further actions
        #return redirect('http://127.0.0.1:8000/info')

    students = Email.objects.all()

    context = {
        'students': students
    }

    return render(request, 'marks.html', context)

def bus(request):
    if request.method == "POST":
        register_number = request.POST.get('register_number')
        password_student = request.POST.get('password_student')
        bus_code = request.POST.get('bus_code')

        try:
            user = Email.objects.get( register_number = register_number , password_student =password_student )
            if user is not None:
                return redirect('http://127.0.0.1:8000/info')
            else:
                return redirect('http://127.0.0.1:8000/infowrong')








        finally:
            pass

    return render(request, 'bus.html')
