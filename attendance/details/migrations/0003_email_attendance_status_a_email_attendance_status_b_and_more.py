# Generated by Django 4.2.1 on 2023-05-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_email_password_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='attendance_status_a',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='email',
            name='attendance_status_b',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='email',
            name='attendance_status_c',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='email',
            name='attendance_status_d',
            field=models.BooleanField(default=True),
        ),
    ]
