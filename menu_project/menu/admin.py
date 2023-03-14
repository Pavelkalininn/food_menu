from django.contrib import (
    admin,
)
from django.contrib.auth import (
    get_user_model,
)

from .models import (
    Food,
    FoodCategory,
    Topping,
)

User = get_user_model()

admin.site.empty_value_display = '-пусто-'

admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Topping)
