# Generated by Django 4.2.1 on 2023-06-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0011_email_math_mark_email_physics_mark_email_python_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(default='projectdjango23@gmail.com', max_length=254),
        ),
    ]
