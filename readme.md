Что сделал:
===========

Бэкенд: Django, Channels, тикеры создаются в файле миграций 
(tickers/migrations), сбрасывать значения тикеров можно
из админки (action erase_values)

Фронт: Vue, vue-charts

Как запустить:
==============

`cd back`

`pip install -r requirements.txt`

`python manage.py migrate`

`python mangage.py runserver`

then

`cd front`

`npm install`

`npm run dev`