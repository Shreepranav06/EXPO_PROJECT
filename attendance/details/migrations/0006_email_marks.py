# Generated by Django 4.2.1 on 2023-06-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_email_period_one_email_period_three_email_period_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='marks',
            field=models.IntegerField(default=100),
        ),
    ]
