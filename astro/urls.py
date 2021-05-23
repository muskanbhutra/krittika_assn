from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='astro-home'),
    path('form/', views.form, name='astro-form'),
    path('response/', views.response, name='astro-response'),
]