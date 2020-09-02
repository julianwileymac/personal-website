from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers
# Create your views here.
def default_render(request):
	# TODO: move this token to Django settings from an environment variable
	# found in the mapbox account settings and getting started instructions
	# see https://www.mapbox.com/account under the "Access tokens" section
	return render(request, 'dashboard/dashboard.html',{})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)