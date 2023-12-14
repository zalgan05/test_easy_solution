# Тестовое задание для "Простые решения"


## Локальный запуск приложения в Docker  

Склонировать репозиторий на свой компьютер и перейти в корневую папку:
```python
git clone git@github.com:zalgan05/test_easy_solution.git
cd test_easy_solution
```

Создать в корневой папке файл .env с переменными окружения, необходимыми
для работы приложения.

Пример содержимого файла:
```
TOKEN='fdsgdfgfsdgdsfg'
STRIPE_PUBLIC_KEY = 'pk_test_dfghfghgjhjghj'
STRIPE_SECRET_KEY = 'sk_test_ghjfghjjhj'
```

Из корневой директории запустить сборку контейнеров с помощью
docker-compose:
```python
docker-compose up -d
```

После этого будет создан и запущен в фоновом режиме контейнер.

После этого проект должен стать доступен по адресу http://127.0.0.1:8000/items/.

Для попадания в админ-зону, перейдите по адресу http://127.0.0.1:8000/admin/.

Затем ведите логин и пароль:
- login: admin
- password: admin

У каждого товара есть цена и количество. Значение "stripe_price_id" - это идентификатор Stripe объекта Price. Идентификатор цены можно найти на панели инструментов Stripe в разделе Product catalog.
При создании продукта вы добавляете цену и цене присваевается API ID:

![image](https://github.com/zalgan05/test_easy_solution/assets/119598678/ea914a7a-2dfa-4963-991c-81694d6a09c0)


## Примеры запросов

<details>
<summary><h5><code>GET /items/</code></h5></summary>
Можно получить простейшую HTML страницу, на которой будет информация о всех товарах с описанием и указанием цены.
Можно добавить товар в корзину покупок.
По нажатию на товар будет происходить запрос на /item/{id}

![image](https://github.com/zalgan05/test_easy_solution/assets/119598678/14c44a5b-1fc7-42e7-879b-1d56ade99bd5)


</details>


<details>
<summary><h5><code>GET /item/{id}</code></h5></summary>
Можно получить простейшую HTML страницу, на которой будет информация о выбранном товаре и кнопка Buy.
По нажатию на кнопку Buy происходит запрос на /buy/{id} с учетом выбранной валюты, получение session_id и далее с помощью JS библиотеки Stripe происходит редирект на Checkout форму

![image](https://github.com/zalgan05/test_easy_solution/assets/119598678/f6fa93f3-4c74-4294-bfee-1565f5f28901)

</details>


<details>
<summary><h5><code>GET /order/</code></h5></summary>
Можно получить простейшую HTML страницу, на которой будет информация о добавленных товарах в корзину и кнопка Buy.
По нажатию на кнопку Buy происходит происходит редирект на Checkout форму. Платеж формируется в выбраной валюте и с общей стоимостью всех товаров в корзине

![image](https://github.com/zalgan05/test_easy_solution/assets/119598678/62609f02-4836-4355-9ae2-a4cb8d4d4695)

![image](https://github.com/zalgan05/test_easy_solution/assets/119598678/2faecc24-e5bf-4b20-a006-afd3d59f4f8f)


</details>


### Остановка контейнера

Для остановки работы приложения можно набрать в терминале команду Ctrl+C
либо открыть второй терминал и воспользоваться командой:
```
docker-compose stop
```

Снова запустить контейнер без пересборки можно командой
```
docker-compose start
```

## Технологии

* Python 3.9
* Django 4.2
* Stripe 7.8
* Docker

