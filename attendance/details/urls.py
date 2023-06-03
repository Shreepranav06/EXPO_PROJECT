from . import views
from django.urls import path


urlpatterns=[
    path("update_attendance", views.update_attendance, name='details'),
    path("update_attendance_p1", views.update_attendance, name='details'),
    path("update_attendance_p2", views.update_attendance, name='details'),
]