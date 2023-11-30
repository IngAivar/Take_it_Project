# Take_it_Project

## Тестовое задание на вакансию: "Middle Python Backend Developer (Django)"

### Цель работы: создат рабучую тестовую систему покупки товаров в магазине.
### В создании приложения использовать `Django` и `Stripe API`.

### Технологический стек

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)](https://stripe.com/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)

### Техническое задание:

```
Создать простой сервер, который общается со Stripe и создает платёжные формы для товаров.
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
  1) Django Модель Item с полями (name, description, price)
  
  2) API с двумя методами:
    2.1) GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item (товара).
    
    2.2) GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item (товаре) и кнопка Buy.

  3) Залить решение на Github, описать запуск в Readme.md
  
  4) Опубликовать свое решение чтобы его можно было быстро и легко протестировать.
  
  5) Бонусные задачи:
    5.1) Запуск используя Docker
    5.2) Использование environment variables
    5.3) Просмотр Django Моделей в Django Admin панели
    5.4) Запуск приложения на удаленном сервере, доступном для тестирования
    5.5) Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
    5.6) Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
    5.7) Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
    5.8) Реализовать не Stripe Session, а Stripe Payment Intent.
```

## Запуск проекта

### 1) Клонирование репозитория

Для клонирования репозитория нужно запустить консоль git и вней пропилать команду:
```bash
git clone https://github.com/IngAivar/Take_it_Project.git
```
___
### 2) Установка зависимостей

Когда вы уже будите в виртуальном окружении команда:
```bash
pip install -r requirements.txt
```
Можно это сделать через консоль, подробно об этом тут: https://docs.python.org/3/tutorial/venv.html

Если вы работаете в IDE и уже зашли в проект просто инсталируйте все библиотеки из файла: `requirements.txt`
___
### 3) Создание Супер-пользователя (Администратора)

Создадим суперпользователя командой:
```bash
python manage.py createsuperuser
```
> Ввод Email необязателен
___
### 4) Запуск миграций

Воспльзуемся команодой `migrate`:
```bash
python manage.py migrate
```
___
### 5) Ввод ключей Stripe

Для того чтобы всё работало правельно, нужно в файле `config/settings.py` поменять занчения в полях `STRIPE_PUBLIC_KEY` и `STRIPE_SECRET_KEY` на свои

Узнать свои ключи можно по ссылке:
```bash
https://dashboard.stripe.com/test/apikeys
```
___
### 6) Создание товара

Вам требуется создать свой товар на сайте `dashboard.stripe.com`

Перейдите по ссылке и на сайте создайте товар под названием `Test Item`, а остальная информация на ваше усмотрение:
```bash
https://dashboard.stripe.com/test/products?active=true
```
Причина по которой мы создаём товар на сайте заключается в том что, `stripe` использует некий код для обозначения цены товара, этот код будет хранится в нашей БД в поле `stripe_price_id`

После того как создадите товар на сайте, его можно будет создать и в нашей БД

Теперь запускаем сайт командой:
```bash
python manage.py runserver
```
После запуска переходим по данной *URL*:
```bash
http://127.0.0.1:8000/admin
```
Вводим свои данные и создаем товар в таблице Item. Поле `stripe_price_id` нужно заполнить кодом с сайта `dashboard.stripe` где был создан товар
___
### 7) Запуск сервера Django

Запускаем проект командой:
```bash
python manage.py runserver
```
Переийти по *URL*:
```bash
http://127.0.0.1:8000/item
```
