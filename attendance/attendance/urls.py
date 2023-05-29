"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

#from django.conf.urls import url

from django.urls import path, include


from First_Page.views import first

from teacher.views import teachers

from details.views import email

from details.views import student

from details.views import info

from details.views import infowrong

from details.views import update_attendance







urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first),
    path('teacher', teachers),
    path('email',email),
    path('student',student),
    path('info', info),
    path('infowrong', infowrong),
    path('update_attendance/', update_attendance, name='update_attendance')
]