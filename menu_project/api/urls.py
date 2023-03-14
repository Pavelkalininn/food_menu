from django.urls import (
    include,
    path,
)
from rest_framework import (
    routers,
)

from .views import (
    FoodCategoryViewSet,
)

router = routers.DefaultRouter()

router.register(
    'food_categories',
    FoodCategoryViewSet,
    basename='food_category'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
