"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from first_app import views



#TEMPLATE TAGGING


urlpatterns = [
    re_path('',(include('first_app.url'))),
    re_path('^help/',(include('first_app.url2'))),
    path('formpage/', views.form_name_view, name='form_name'),
    path('user/',views.users, name='users'),
    path('register/',include('first_app.url')),
 path('special/', views.special,name='special'),
    path('first_app/',include('first_app.url')),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('coffee/',views.coffee, name='coffee'),
]
