# Generated by Django 4.2.1 on 2023-06-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0019_alter_email_g'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g', models.BigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='email',
            name='g',
        ),
    ]