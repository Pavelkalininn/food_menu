from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    ForeignKey,
    ManyToManyField,
    Model,
    PositiveSmallIntegerField,
)


class Topping(Model):
    name = CharField(
        'Наименование',
        max_length=150,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.name


class FoodCategory(Model):
    name = CharField(
        'Наименование',
        max_length=150
    )
    is_publish = BooleanField(
        'Опубликована',
        default=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Food(Model):
    category = ForeignKey(
        FoodCategory,
        verbose_name='Блюдо',
        related_name='foods',
        on_delete=CASCADE,
        null=True,
        blank=True
    )
    name = CharField(
        'Наименование',
        max_length=150
    )
    description = CharField(
        'Описание',
        max_length=150
    )
    price = PositiveSmallIntegerField(
        'Стоимость'
    )
    toppings = ManyToManyField(
        Topping,
        verbose_name='Топпинги',
        related_name='foods',
    )
    is_publish = BooleanField(
        'Опубликовано',
        default=False
    )
    is_vegan = BooleanField(
        'Вегетарианское',
        default=False
    )
    is_special = BooleanField(
        'Специальное',
        default=False
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
