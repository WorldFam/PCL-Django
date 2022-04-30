from django.urls import path
from casework.views import PlaceOrder

urlpatterns = [
    path('', PlaceOrder.as_view(), name='order'),
]