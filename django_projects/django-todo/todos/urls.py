from django.urls import path

from .views import todos

app_name = 'todos'
urlpatterns = [
    path('', todos, name='todos')
]