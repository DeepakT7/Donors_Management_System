from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
	orders = Order.objects.all()
	donors = Donor.objects.all()

	total_donors = donors.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'donors':donors,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'accounts/dashboard.html', context)

def donations(request):
	donations = Donation.objects.all()

	return render(request, 'accounts/donations.html', {'donations':donations})

def donor(request, pk_test):
	donor = Donor.objects.get(id=pk_test)

	orders = donor.order_set.all()
	order_count = orders.count()

	context = {'donor':donor, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/donor.html',context)