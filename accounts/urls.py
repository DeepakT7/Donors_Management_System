from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('donations/', views.donations, name = "donations"),
    path('donor/<str:pk_test>/', views.donor, name = "donor"),
]
