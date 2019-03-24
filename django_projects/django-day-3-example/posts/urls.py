from django.urls import path

from posts.views import index, retrieve, create_comment

app_name = 'posts'
urlpatterns = [
    path('', index, name="index"),
    path('<int:id>', retrieve, name="retrieve"),
    path('create_comment/<int:id>', create_comment, name='create_comment'),
]