# Generated by Django 4.2.1 on 2023-06-01 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_email_bus_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]