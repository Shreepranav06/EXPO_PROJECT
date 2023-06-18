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
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url

from django.urls import path, include


from First_Page.views import first

from teacher.views import teachers

from details.views import email

from details.views import studentview

from details.views import info

from details.views import infowrong

from details.views import update_attendance

from details.views import update_attendance_a

from details.views import update_attendance_b

from details.views import mark

from details.views import bus_view

from First_Page.views import about


from canteen.views import canteen_login

from details.views import mark1

from details.views import mark2

from details.views import mark3

from canteen.views import food_order

from canteen.views import summary


from details.views import  get_current_location









urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first),
    path('teacher', teachers),
    path('email',email),
    path('student',studentview),
    path('info', info),
    path('infowrong', infowrong),
    path('update_attendance/', update_attendance, name='update_attendance'),
    path('update_attendance_a/', update_attendance_a, name='update_attendance_a'),
    path('update_attendance_b/', update_attendance_b, name='update_attendance_b'),
    path('mark/', mark, name='mark'),
    path('bus_view/', bus_view, name='bus_view'),
    path('about/', about, name='about'),
    path('canteen', canteen_login, name='canteen'),
    path('mark1/', mark1, name='mark1'),
    path('mark2/', mark2, name='mark2'),
    path('mark3/', mark3, name='mark3'),
    path('order/', food_order, name='food_order'),
    path('summary/', summary),
    path('map/', get_current_location)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
