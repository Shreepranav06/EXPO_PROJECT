# Generated by Django 4.2.1 on 2023-06-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_email_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='marks',
        ),
        migrations.AddField(
            model_name='email',
            name='CGPA',
            field=models.FloatField(default=10),
        ),
    ]