## Задание
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями

1) GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

2) GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

# Ссылка на тестовое 
https://docs.google.com/document/d/1X8yV7jAZWZWhy3NG3m_Yi8lW4Bfa6ZNGDx95pHkE_qc/edit

## Как запустить проект

Клонировать репозиторий и перейти в директорию для развертывания:

```
git clone git@github.com:ragecodemode/sprite_api_fintex_testovoe.git
cd backend
python -m venv venv
source venv/Scripts/activate
```
Установим зависимости requiremets.txt и выполним миграции и создадим суперпользователя:
```
pip install -r -requirements.txt

python manage.py makemigrations

python manage.py createsuperuser
```
Переменные окружения, используемые в проекте(для этого создайте и заполните файл .env)


Чтобы развернуть проект выполните команду:

```
docker-compose up -d
```

Остановка проекта осуществляется командой.

```
docker-compose stop
```
