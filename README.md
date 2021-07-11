# API Polls

---

## Задача

Спроектировать и разработать API для системы опросов пользователей

### _Документация API_ (автодокументирование на swagger (drf-yasg) доступно по адресу http://127.0.0.1:8000/swagger/ )

**Для проверки аутентификации пользователя используется JWT.**

---

## Описание ТЗ:

##### _Функционал для администратора системы:_
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##### _Функционал для пользователей системы:_
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

---

## Окружение проекта:
  * python 3.8
  * Django 2.2.10
  * djangorestframework
  * БД PostgreSQL

---

## Запуск

Склонируйте репозиторий с помощью git

    https://github.com/Speccy-Rom/Api_system_of_user_surveys.git
Перейти в папку:
```bash
cd Api_system_of_user_surveys
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **reqs.txt**:
```bash
pip install -r reqs.txt
```

Настройте БД PostgreSQL (по желанию):

```
 https://timeweb.com/ru/community/articles/kak-ispolzovat-postgresql-c-prilozheniem-django-na-ubuntu-16-04
```

После настройки БД выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/
