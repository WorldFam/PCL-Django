from django.http import HttpResponse

from .models import Drink, Order
from django.shortcuts import render, redirect
from django.views import View

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PlaceOrder(View):
    def get(self, request, *args, **kwargs):

        drinks = Drink.objects.all()
        return render(request, 'casework/order.html',{'drinks' :drinks })
    

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            drink = Drink.objects.get(pk__contains=int(item))
            item_data = {
                'id': drink.pk,
                'name': drink.name,
                'category': drink.category,
                'size': drink.size,
                'price': drink.price
            }

            order_items['items'].append(item_data)

            sum_total_price = 0
            item_ids = []

        for item in order_items['items']:
            sum_total_price += item['price']
            item_ids.append(item['id'])

        order = Order.objects.create(total_price=sum_total_price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': sum_total_price
        }

        return render(request, 'casework/order_confirmation.html', context)
