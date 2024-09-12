# link_cut_FastAPI

## Описание
Проект link_cut_FastAPI — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, созданную сервисом, и выполнить переадресацию.
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
git clone https://github.com/KonstantinSKS/link_cut_service.git
```
```
cd link_cut_service
```
Cоздать и активировать виртуальное окружение:
```
py -3.9 -m venv venv
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
Создать и заполните файл .env в корневой папке проекта:
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=MY_SECRET_KEY
```
Выполнить миграции:
```
flask db upgrade
```
Запустить проект:
```
flask run
```

## Примеры запросов:
GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору:
```
/api/id/{short_id}/
```
Response:
```
{
  "url": "string"
}
```

POST-запрос на создание новой короткой ссылки:
```
/api/id/
```
Request:
```
{
  "url": "string",
  "custom_id": "string"
}
```
Response:
```
{
  "url": "string",
  "short_link": "string"
}
```

# Автор: 
Стеблев Константин
