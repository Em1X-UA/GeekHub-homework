from django.urls import path, include
from rest_framework import routers

from api.views import CategoryListAPI, ProductViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register('', ProductViewSet, 'api_prod')

urlpatterns = [
    path('products/', include(router.urls)),
    path('categories/', CategoryListAPI.as_view(), name='api_categories'),

]
