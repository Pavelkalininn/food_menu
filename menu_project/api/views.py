from api.serializers import (
    FoodCategorySerializer,
)
from django.db.models import (
    Prefetch,
)
from rest_framework.viewsets import (
    ReadOnlyModelViewSet,
)

from menu.models import (
    Food,
    FoodCategory,
)

FILTER_CHOICE = ('True', 'False')
IS_VEGAN = 'is_vegan'
IS_SPECIAL = 'is_special'
TOPPING_NAME = 'topping_name'
FOOD_NAME = 'name'
CATEGORY_NAME = 'category_name'


class FoodCategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        """Такой сложный get_queryset нужен для того, чтобы можно было
        сократить количество запросов к БД через prefetch_related
        """
        query_params = self.request.query_params
        filter_kwargs = {}
        for param, field_name in (
                (IS_VEGAN, 'is_vegan'),
                (IS_SPECIAL, 'is_special'),
                (TOPPING_NAME, 'toppings__name__icontains'),
                (FOOD_NAME, 'name__icontains'),
                (CATEGORY_NAME, 'category__name__icontains')
        ):
            value = query_params.get(param)
            if param in (IS_SPECIAL, IS_VEGAN):
                if value and value in FILTER_CHOICE:
                    filter_kwargs[field_name] = value == 'True'
            elif value:
                filter_kwargs[field_name] = value
        prefetched_foods = Food.objects.prefetch_related('toppings')
        if filter_kwargs:
            prefetched_foods = prefetched_foods.filter(
                **filter_kwargs,
                is_publish=True,
            ).distinct()
        return FoodCategory.objects.filter(
            is_publish=True,
            foods__in=prefetched_foods
        ).prefetch_related(
            Prefetch(
                'foods',
                queryset=prefetched_foods
            )
        ).distinct()
