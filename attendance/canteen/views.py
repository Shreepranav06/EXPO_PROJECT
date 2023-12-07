from django.shortcuts import render, redirect
from .models import Canteen

from django import template


from .models import Food






def canteen_login(request):
    if request.method == "POST":
        register_number = request.POST.get('id_canteen')
        password_student = request.POST.get('password_canteen')

        try:
            user = Canteen.objects.get( id_canteen = register_number , password_canteen =password_student )
            if user is not None:
                return redirect('http://127.0.0.1:8000/order')
            else:
                return redirect('http://127.0.0.1:8000/infowrong')
        finally:
            pass


    return render(request,'canteen.html')



def food_order(request):
    food_items = Food.objects.all()

    if request.method == "POST":
        total_price = 0
        for food_item in food_items:
            quantity = request.POST.get(f'quantity_{food_item.sno}')
            if quantity:
                food_item.quanity = int(quantity)
                food_item.save()
                total_price += food_item.price * int(quantity)
                end = food_item.price * food_item.quanity

        return render(request, 'order_summary.html', {'food_items': food_items, 'total_price': total_price, 'end': end})

    return render(request, 'food_order.html', {'food_items': food_items})

def summary(request):
    food_items = Food.objects.all()
    total_price = 0
    for food_item in food_items:
        total_price += food_item.price * food_item.quanity
    return render(request, 'order_summary.html', {'food_items': food_items, 'total_price': total_price})




