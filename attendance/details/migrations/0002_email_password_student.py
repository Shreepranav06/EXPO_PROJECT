# Generated by Django 2.1 on 2023-05-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='password_student',
            field=models.CharField(default='password', max_length=100),
        ),
    ]
