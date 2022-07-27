# Что сделал:

### Бэкенд: 

Использовал `Django`, `Channels`. 
Тикеры и истории по ним создаются в файле миграций 
(`tickers/migrations/0001_initial.py`), сбрасывать значения тикеров можно
из админки путем удаления объектов `TickerHistory`.

Тесты лежат в `back/tickers/tests`.

Запустить тесты: `python manage.py test`

Какие есть ендпоинты тут:

`http://localhost:8000/` - эндпоинт для тестирование работы бэкенда,
выводит изменения цен тикеров, чтобы мониторить, что происходит на бэке.

`ws://localhost:8000/ws/` - эндпоинт для передачи данных через WS на фронт

`http://localhost:8000/ticker_names/` - эндпоинт для заполнения селекта на фронте

В качестве базы данных использую дефолтную для `django` `sqlite3`
 
### Фронт: 

Использовал `Vue3`, `vue-charts`. Здесь код разбит на компоненты.

# Как запустить:

`cd back`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

потом:

`cd front`

`npm install`

`npm run dev`

потом переходим на:

`http://localhost:5173/`