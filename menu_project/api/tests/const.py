COUNT_WITHOUT_FILTER = 3
WITHOUT_FILTER_RESPONSE = [{'foods': [{'description': 'Блины с вареньем',
                                       'is_special': False,
                                       'is_vegan': True,
                                       'name': 'Pancake',
                                       'price': 95,
                                       'toppings': ['raspberry']}],
                            'id': 1,
                            'name': 'breakfast'},
                           {'foods': [
                               {'description': 'Суп с наваристым бульоном',
                                'is_special': True,
                                'is_vegan': False,
                                'name': 'Potato soup',
                                'price': 120,
                                'toppings': ['kiwi', 'blueberry']},
                               {'description': 'STRAWBERRY',
                                'is_special': False,
                                'is_vegan': True,
                                'name': 'Strawberry',
                                'price': 300,
                                'toppings': []}],
                               'id': 2,
                               'name': 'lunch'},
                           {'foods': [{'description': 'Спагетти с мясом',
                                       'is_special': True,
                                       'is_vegan': False,
                                       'name': 'Spaghetti',
                                       'price': 240,
                                       'toppings': []}],
                            'id': 3,
                            'name': 'diner'}]

COUNT_IS_SPECIAL = 1
IS_SPECIAL_RESPONSE = [{'foods': [{'description': 'Суп с наваристым бульоном',
                                   'is_special': True,
                                   'is_vegan': False,
                                   'name': 'Potato soup',
                                   'price': 120,
                                   'toppings': ['kiwi', 'blueberry']}],
                        'id': 2,
                        'name': 'lunch'}]

COUNT_IS_VEGAN = 2
IS_VEGAN_RESPONSE = [{'foods': [{'description': 'Блины с вареньем',
                                 'is_special': False,
                                 'is_vegan': True,
                                 'name': 'Pancake',
                                 'price': 95,
                                 'toppings': ['raspberry']}],
                      'id': 1,
                      'name': 'breakfast'},
                     {'foods': [{'description': 'STRAWBERRY',
                                 'is_special': False,
                                 'is_vegan': True,
                                 'name': 'Strawberry',
                                 'price': 300,
                                 'toppings': []}],
                      'id': 2,
                      'name': 'lunch'}]

COUNT_IS_NOT_VEGAN = 1
IS_NOT_VEGAN_RESPONSE = [
    {'foods': [{'description': 'Суп с наваристым бульоном',
                'is_special': True,
                'is_vegan': False,
                'name': 'Potato soup',
                'price': 120,
                'toppings': ['kiwi', 'blueberry']}],
     'id': 2,
     'name': 'lunch'}]

COUNT_FOOD_NAME = 1
FOOD_NAME_RESPONSE = [{'foods': [{'description': 'STRAWBERRY',
                                  'is_special': False,
                                  'is_vegan': True,
                                  'name': 'Strawberry',
                                  'price': 300,
                                  'toppings': []}],
                       'id': 2,
                       'name': 'lunch'}]

COUNT_CATEGORY_NAME = 1
CATEGORY_NAME_RESPONSE = [
    {'foods': [{'description': 'Суп с наваристым бульоном',
                'is_special': True,
                'is_vegan': False,
                'name': 'Potato soup',
                'price': 120,
                'toppings': ['kiwi', 'blueberry']},
               {'description': 'STRAWBERRY',
                'is_special': False,
                'is_vegan': True,
                'name': 'Strawberry',
                'price': 300,
                'toppings': []}],
     'id': 2,
     'name': 'lunch'}]

COUNT_TOPPING_NAME = 1
TOPPING_NAME_RESPONSE = [
    {'foods': [{'description': 'Суп с наваристым бульоном',
                'is_special': True,
                'is_vegan': False,
                'name': 'Potato soup',
                'price': 120,
                'toppings': ['kiwi', 'blueberry']}],
     'id': 2,
     'name': 'lunch'}]
