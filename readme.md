# Что сделал:

### Бэкенд: 

Django, Channels, тикеры и истории по ним создаются в файле миграций 
(`tickers/migrations`), сбрасывать значения тикеров можно
из админки путем удаления объектов `TickerHistory`.

Тесты лежат в `back/tickers/tests`.

Запустить тесты: `python manage.py test`

Какие есть ендпоинты тут:

`http://localhost:8000/` - эндпоинт для тестирование работы бэкенда,
выводит изменения цен тикеров, чтобы мониторить, что происходит на бэке.

`ws://localhost:8000/ws/` - эндпоинт для передачи данных через WS на фронт

`http://localhost:8000/ticker_names/` - эндпоинт для заполнения селекта на фронте
 
### Фронт: 

Vue3, vue-charts

# Как запустить:

`cd back`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

`python mangage.py runserver`

потом:

`cd front`

`npm install`

`npm run dev`

потом переходим на:

`http://localhost:5173/`