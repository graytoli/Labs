from django.urls import path

from .views import find_matches

app_name = 'books'
urlpatterns = [
    path('search', find_matches, name='find_matches')
]