"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from task1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
    path('main/', views.main_page, name='main_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('blog', include('blog.urls')),
]
