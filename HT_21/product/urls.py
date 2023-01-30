from django.urls import path

from . import views as pr


urlpatterns = [
    path('add_products/', pr.add_products, name='add_products'),
    path('', pr.my_products, name='my_products'),
    path('scraper/', pr.scraper, name='scraper'),
    path('my_products/<int:pk>/', pr.product_data, name="product_data"),
    path('my_products/<int:pk>/edit', pr.edit_product, name="edit_product"),
    path('my_products/edit_confirm', pr.edit_confirm, name="edit_confirm"),
    path('my_products/del', pr.delete_product, name="delete_product"),
    path('category/<int:pk>/', pr.category_products, name='category_products'),
]
