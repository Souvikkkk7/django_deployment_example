from django.urls import path
from django.urls import re_path
from . import views

#TEMPLATE TAGGING
app_name='first_app'

urlpatterns = [
    path('', views.index, name='index'),
path('relative/', views.relative, name='relative'),
    path('others/', views.other, name='other'),
path('register/',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),

    ]