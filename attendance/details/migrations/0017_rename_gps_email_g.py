# Generated by Django 4.2.1 on 2023-06-09 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0016_alter_email_gps'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='gps',
            new_name='g',
        ),
    ]
