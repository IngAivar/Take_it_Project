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
