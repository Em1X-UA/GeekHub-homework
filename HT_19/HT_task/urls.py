"""HT_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from scraper import views


app_name = 'scraper'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add_products/', views.add_products, name='add_products'),
    path('my_products/', views.my_products, name='my_products'),
    path('scraper/', views.scraper, name='scraper'),
    # path('my_products/<int:pk>/', views.product_data, name="product_data"),
    path('<int:pk>/', views.product_data, name="product_data"),
]

