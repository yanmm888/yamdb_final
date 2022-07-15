# Yamdb with Docker and workflows
## База отзывов пользователей о фильмах, музыке и книгах
## Стек технологий: Python 3, Django REST Framework, PostgreSQL, Simple-JWT, NGINX, Docker, flake, pytest
Статус 
![example workflow](https://github.com/yanmm888/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

##### Создание файла с переменными окружения .env
Пример:
- Ключ приложения ```SECRET_KEY='very_strong_secret_key'```
- выбор движка СУБД ```DB_ENGINE=django.db.backends.postgresql```
- название базы ```DB_NAME=postgres```
- имя пользователя базы ```POSTGRES_USER=postgres```
- пароль базы данных ```POSTGRES_PASSWORD=postgres```
- адрес базы ```DB_HOST=db``` 
- порт базы```DB_PORT=5432```


### Запуск приложения:
```docker-compose up```

### Выполнить миграции:
```docker-compose exec web python manage.py makemigrations``` \
```docker-compose exec web python manage.py migrate``` \

### Создать суперпользователя:
```docker-compose exec web python manage.py createsuperuser```\
для windows 
```winpty docker-compose exec web python manage.py createsuperuser```\

### Привязать статические файлы:
```docker-compose exec web python manage.py collectstatic --no-input```\
### Информация об образе на Dockerhub
```nmm888/api_yamdb:v05.07.2022 ```
### Информация об авторе
Malik Nurmagomedov
```https://github.com/yanmm888/```\