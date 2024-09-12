# link_cut_FastAPI

# English version

## Description
The link_cut_FastAPI project is an asynchronous URL shortening service. Its purpose is to associate a long user-provided URL with a shorter one created by the service and perform redirection. URLs are generated using the choices method from the random library. The service is implemented using a REST API.

## Technologies
- Python 3.11
- FastAPI 0.111
- Pydantic 2.9
- SQLAlchemy 2.0
- Uvicorn 0.30

## Project Setup
Clone the repository and navigate to the project directory:
```
git clone https://github.com/KonstantinSKS/link_cut_FastAPI.git
```
```
cd link_cut_FastAPI
```
Create and activate a virtual environment:
```
py -3.11 -m venv venv
```
### Command for Windows:
```
source venv/Scripts/activate
```
### For Linux and macOS:
```
source venv/bin/activate
```
Install dependencies from the requirements.txt file:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Create and populate the .env file (based on .env.template) in the root project folder.

Run the project:
```
PYTHONPATH=. python app/main.py
```
Once the project is running, the documentation will be available at: http://127.0.0.1:8080/

## The documentation page will feature 2 endpoints:

- POST / Form to input a URL. A shortened URL will be created using random choices. After being saved to the database, it returns HTTPStatus 201 and both the original and shortened URLs.

- GET /{short_url_id} The short URL (app_host/app_port/short_url) is retrieved from the database by its short_url_id. It performs a redirect to the page with the original URL.

# Author:
Konstantin Steblev


# Русская версия

## Описание
Проект link_cut_FastAPI — это асинхронный сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, созданную сервисом, и выполнить переадресацию.
Ссылки создаются методом choices библиотеки random. Сервис реализован с использованием REST API.

## Технолгии
- Python 3.11
- FastAPI 0.111
- Pydantic 2.9
- SQLAlchemy 2.0
- Uvicorn 0.30

## Запуск проекта
Клонировать репозиторий и перейти в директорию проекта:
```
git clone https://github.com/KonstantinSKS/link_cut_FastAPI.git
```
```
cd link_cut_FastAPI
```
Cоздать и активировать виртуальное окружение:
```
py -3.11 -m venv venv
```
### Команда для Windows:
```
source venv/Scripts/activate
```
### Для Linux и macOS:
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Создать и заполните файл .env (по образцу .env.template) в корневой папке проекта.

Запустить проект:
```
PYTHONPATH=. python app/main.py
```
После запуска документация проекта будет доступна по адресу: http://127.0.0.1:8080/

## На странице с документацией будет доступно 2 эндпоинта:

- POST /
Форма для ввода URL.
Будет создан короткий URL с помощью random choices.
После записи в базу данных вернет HTTPStatus 201 и оригинальный и короткий URLs.

- GET /{short_url_id}
По short_url_id будет извлечен из базы данных короткий URL (app_host/app_port/short_url).
Выполнится редирект на страницу c полученным URL.

# Автор: 
Стеблев Константин
