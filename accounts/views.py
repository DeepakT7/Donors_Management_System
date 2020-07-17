from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    return render(request, 'accounts/dashboard.html')


def donations(request):
    return render(request, 'accounts/donations.html')

def donor(request, pk_test):
    donor = Donor.objects.get(id = pk_test)

    orders = donor.order_set.all()
    order_count = orders.count()
    context = {'donor' : donor, 'orders' : orders, 'order_count':order_count }
    return render(request, 'accounts/donor.html', context)

# Create your views here.
