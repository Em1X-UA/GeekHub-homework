from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_products/', views.add_products, name='add_products'),
    path('my_products/', views.my_products, name='my_products'),
    path('scraper/', views.scraper, name='scraper'),
    path('my_products/<int:pk>/', views.product_data, name="product_data"),
]