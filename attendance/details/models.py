from django.db import models


class Email(models.Model):
    register_number=models.BigIntegerField()
    student_name=models.CharField(max_length=100)
    email=models.EmailField()
    attendance_status=models.BooleanField(default=True)
    attendance_status_a = models.BooleanField(default=True)
    attendance_status_b = models.BooleanField(default=True)
    attendance_status_c = models.BooleanField(default=True)
    attendance_status_d = models.BooleanField(default=True)
    password_student=models.CharField(max_length=100, default='password')
    total = models.FloatField(default=100)
    period_one = models.FloatField(default=100)
    period_two = models.FloatField(default=100)
    period_three = models.FloatField(default=100)
    CGPA = models.FloatField(default=10)
    bus_code= models.IntegerField(default=100)
    img = models.ImageField()







