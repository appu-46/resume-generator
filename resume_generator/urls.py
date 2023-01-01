# from importlib.resources import path
from django.urls import path
from . import views

app_name = 'resume_generator'
urlpatterns = [
    path('', views.index, name='index'),
    path('user_creation/', views.user_creation, name='user_creation'),
    path('details/', views.details, name='details'),
    path('preview/', views.preview, name='preview')
]
