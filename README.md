# Telegraph Clone

# Свой телеграф

Приложение [Anonymous](https://shielded-anchorage-43765.herokuapp.com/)
представляет собой аналог сайта **Telegraph**
[http://telegra.ph/](http://telegra.ph/).

Оно позволяет любому пользователю разместить статью и получить для нее
уникальный URL. Реализованная авторизация по cookie позволяет автору статьи
вносить в нее необходимые правки после публикации. Все записи хранятся в базе
данных SQLite.

Для корректоной работы необходимо установить следующие модули:
* **flask**
* **Flask-SQLAlchemy**
* **gunicorn**

Пакеты устанавливаются командой `pip install -r requirements.txt`.

Для запуска приложения необходимо выполнить команду:
```
gunicorn server:app
```
Приложение будет находиться по адресу 
[http://127.0.0.1:8000](http://127.0.0.1:8000).

# Project Goals

The code is written for educational purposes. Training course for 
web-developers - [DEVMAN.org](https://devman.org)
