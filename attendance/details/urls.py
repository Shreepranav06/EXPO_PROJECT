from . import views
from django.urls import path


urlpatterns=[
    path("update_attendance", views.update_attendance, name='details'),
]