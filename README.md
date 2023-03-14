# Эндпоинт для просмотра блюд.

## Требования

Требуется реализовать эндпоинт, который вернёт все блюда, у которых is_publish=True сгруппированными по категориям, добавить возможность фильтрации по: is_vegan, is_special, [topping.name, …]

## Дополнительно
Код покрыт тестами на основе TestCase-ов из rest_framework.test
Добавлена конфигурация докера с docker-compose для запуска приложения в докере


## Technology

    Django==4.1.7
    djangorestframework==3.14.0
    psycopg2-binary==2.9.5
    python-dotenv==1.0.0
    uvicorn==0.21.0

## Образец заполнения env файла доступен по ссылке: 

[infra_menu/example.env](./infra_menu/example.env)


## Для запуска тестов необходимо в папке infra_menu выполнить:

    docker-compose exec backend python manage.py test

## Запуск проекта:

### Для запуска проекта с использованием docker-compose необходимо в папке infra_menu выполнить следующие команды:
    
    docker-compose up -d --build
    docker-compose exec backend python manage.py migrate

Для установки фикстур в БД необходимо выполнить:


    docker-compose exec backend python manage.py loaddata db.json
    docker-compose exec backend python manage.py createsuperuser
    docker-compose exec backend python manage.py collectstatic --no-input


Для остановки контейнера выполните:

     docker-compose stop


Доступен только просмотр меню, блюда сгруппированы по категориям (только GET запрос на адрес, указанный ниже).

    /api/v1/food_categories/

или с фильтрами:

    /api/v1/food_categories/?is_special=True
    /api/v1/food_categories/?is_vegan=True
    /api/v1/food_categories/?is_vegan=False
    /api/v1/food_categories/?name=Straw
    /api/v1/food_categories/?category_name=lun
    /api/v1/food_categories/?topping_name=kiwi
    /api/v1/food_categories/?category_name=lunch&topping_name=blue
    /api/v1/food_categories/?category_name=siesta&topping_name=blue

Получаем ответ, например:

    [
          {
             "id":1,
             "name":"Напитки",
             "foods":[
                {
                   "name": "Смузи",
                   "description": "Смузи 400 мл",
        “price”: 200,
                   "is_vegan": true,
                   "is_special": false,
                   "toppings": [ “Киви”, ”Манго” ]
                },
                {...}
             ]
          },
          {
             "id":2, 
             "name":"Выпечка",
             "foods":[...]
          },
    ]


Author: [__Pavel Kalinin__](https://github.com/Pavelkalininn)
