from rest_framework.relations import (
    StringRelatedField,
)
from rest_framework.serializers import (
    ModelSerializer,
)

from menu.models import (
    Food,
    FoodCategory,
)


class FoodSerializer(ModelSerializer):
    toppings = StringRelatedField(many=True)

    class Meta:
        fields = (
            'name',
            'description',
            'price',
            'is_vegan',
            'is_special',
            'toppings'
        )
        model = Food


class FoodCategorySerializer(ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'foods')
        model = FoodCategory
