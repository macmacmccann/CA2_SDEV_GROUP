from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Order


def thanks(request ,order_id):
    if order_id:
        customer_order = get_object_or_404(Order,id = order_id)
    return render(request, 'thanks.html', {'customer_order':customer_order})