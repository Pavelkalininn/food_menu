from api.tests.const import (
    CATEGORY_NAME_RESPONSE,
    COUNT_CATEGORY_NAME,
    COUNT_FOOD_NAME,
    COUNT_IS_NOT_VEGAN,
    COUNT_IS_SPECIAL,
    COUNT_IS_VEGAN,
    COUNT_TOPPING_NAME,
    COUNT_WITHOUT_FILTER,
    FOOD_NAME_RESPONSE,
    IS_NOT_VEGAN_RESPONSE,
    IS_SPECIAL_RESPONSE,
    IS_VEGAN_RESPONSE,
    TOPPING_NAME_RESPONSE,
    WITHOUT_FILTER_RESPONSE,
)
from rest_framework import (
    status,
)
from rest_framework.test import (
    APIClient,
    APITestCase,
)

from menu.models import (
    Food,
    FoodCategory,
    Topping,
)


class AccountTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.topping_raspberry = Topping.objects.create(name='raspberry')
        cls.topping_kiwi = Topping.objects.create(name='kiwi')
        cls.topping_blueberry = Topping.objects.create(name='blueberry')
        cls.category_breakfast = FoodCategory.objects.create(
            name='breakfast',
            is_publish=True
        )
        cls.category_lunch = FoodCategory.objects.create(
            name='lunch',
            is_publish=True
        )
        cls.category_diner = FoodCategory.objects.create(
            name='diner',
            is_publish=True
        )
        cls.category_non_publish = FoodCategory.objects.create(
            name='non_publish',
            is_publish=False
        )
        cls.PANCAKE_DATA = {
            'name': 'Pancake',
            'description': 'Блины с вареньем',
            'price': 95,
            'is_vegan': True,
            'is_special': False,
            'is_publish': True,
            'category': cls.category_breakfast,
        }
        cls.SPAGHETTI_DATA = {
            'name': 'Spaghetti',
            'description': 'Спагетти с мясом',
            'price': 240,
            'is_vegan': False,
            'is_special': True,
            'is_publish': False,
            'category': cls.category_diner,
        }
        cls.POTATO_DATA = {
            'name': 'Potato soup',
            'description': 'Суп с наваристым бульоном',
            'price': 120,
            'is_vegan': False,
            'is_special': True,
            'is_publish': True,
            'category': cls.category_lunch
        }
        cls.STRAWBERRY_DATA = {
            'name': 'Strawberry',
            'description': 'STRAWBERRY',
            'price': 300,
            'is_vegan': True,
            'is_special': False,
            'is_publish': True,
            'category': cls.category_lunch
        }
        cls.potato = Food.objects.create(**cls.POTATO_DATA)
        cls.potato.toppings.set((cls.topping_kiwi, cls.topping_blueberry))
        cls.spaghetti = Food.objects.create(**cls.SPAGHETTI_DATA)
        cls.pancake = Food.objects.create(**cls.PANCAKE_DATA)
        cls.pancake.toppings.add(cls.topping_raspberry)
        cls.strawberry = Food.objects.create(**cls.STRAWBERRY_DATA)

    def setUp(self):
        self.client = APIClient()

    def test_url_without_filter(self):
        """
        Ensure we get correct data by request to without_filter url.
        """
        response = self.client.get('/api/v1/food_categories/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_WITHOUT_FILTER)
        self.assertEqual(response.json(), WITHOUT_FILTER_RESPONSE)

    def test_url_is_special_filter(self):
        """
        Ensure we get correct data by request to is_special_filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?is_special=True',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_IS_SPECIAL)
        self.assertEqual(response.json(), IS_SPECIAL_RESPONSE)

    def test_url_is_vegan_filter(self):
        """
        Ensure we get correct data by request to is_vegan_filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?is_vegan=True',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_IS_VEGAN)
        self.assertEqual(response.json(), IS_VEGAN_RESPONSE)

    def test_url_is_not_vegan_filter(self):
        """
        Ensure we get correct data by request to is_vegan_filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?is_vegan=False',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_IS_NOT_VEGAN)
        self.assertEqual(response.json(), IS_NOT_VEGAN_RESPONSE)

    def test_url_food_name_filter(self):
        """
        Ensure we get correct data by request to food name filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?name=Straw',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_FOOD_NAME)
        self.assertEqual(response.json(), FOOD_NAME_RESPONSE)

    def test_url_category_name_filter(self):
        """
        Ensure we get correct data by request to category name filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?category_name=lun',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_CATEGORY_NAME)
        self.assertEqual(response.json(), CATEGORY_NAME_RESPONSE)

    def test_url_toppings_name_filter(self):
        """
        Ensure we get correct data by request to toppings name filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?topping_name=kiwi',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_TOPPING_NAME)
        self.assertEqual(response.json(), TOPPING_NAME_RESPONSE)

    def test_url_category_name_and_topping_name_filter(self):
        """
        Ensure we get correct data by request to category_name_and_topping_name
         filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?category_name=lunch&topping_name=blue',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), COUNT_TOPPING_NAME)
        self.assertEqual(response.json(), TOPPING_NAME_RESPONSE)

    def test_url_wrong_filter(self):
        """
        Ensure we get correct data by request to wrong filter url.
        """
        response = self.client.get(
            '/api/v1/food_categories/?category_name=siesta&topping_name=blue',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.json(), [])

    def test_post_request(self):
        """
        Ensure method "POST" not allowed.
        """
        response = self.client.post(
            '/api/v1/food_categories/',
            format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
