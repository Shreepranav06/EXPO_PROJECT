from django.db import models


class Email(models.Model):
    register_number=models.BigIntegerField()
    student_name=models.CharField(max_length=100)
    email=models.EmailField()
    attendance_status=models.BooleanField(default=True)
    password_student=models.CharField(max_length=100, default='password')




