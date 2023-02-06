from django.urls import path, include
from rest_framework import routers

from api.views import ProductListAPI, CategoryListAPI, ProductViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register('', ProductViewSet, 'api_prod')

urlpatterns = [
    path('', ProductListAPI.as_view(), name='api_products'),
    path('categories/', CategoryListAPI.as_view(), name='api_categories'),
    path('admin/', include(router.urls)),

]
