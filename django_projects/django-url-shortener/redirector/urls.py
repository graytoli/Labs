from django.urls import path

from .views import index, redirect

app_name = 'redirector'
urlpatterns = [
    path('', index, name='index'),
    path('<str:code>', redirect, name='redirect'),
]