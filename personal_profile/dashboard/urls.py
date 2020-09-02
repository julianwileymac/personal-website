from django.urls import path
from .views import default_render, pivot_data

urlpatterns = [
    path('', default_render, name='dashboard'),
    path('data', pivot_data, name='pivot_data'),
]