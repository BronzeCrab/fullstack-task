# Что сделал:

#### Бэкенд: 

Django, Channels, тикеры создаются в файле миграций 
(tickers/migrations), сбрасывать значения тикеров можно
из админки (action erase_values).

Тесты лежат в `back/tickers/tests`.

Запустить тесты `python manage.py test`

Какие есть ендпоинты:

`http://localhost:8000/` - эндпоинт для тестирование работы бэкенда

`ws://localhost:8000/ws/` - эндпоинт для передачи данных через WS на фронт
 
#### Фронт: 

Vue, vue-charts

# Как запустить:

`cd back`

`pip install -r requirements.txt`

`python manage.py migrate`

`python mangage.py runserver`

потом:

`cd front`

`npm install`

`npm run dev`