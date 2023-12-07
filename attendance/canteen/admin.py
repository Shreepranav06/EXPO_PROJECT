from django.contrib import admin

from .models import Food

from .models import Canteen

admin.site.register(Canteen)

admin.site.register(Food)


# Register your models here.
