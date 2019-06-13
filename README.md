# fedresurs task

Для сайта "Федресурс" (https://fedresurs.ru) реализовать сбор всех сообщений по заданной ключевой фразе с оставлением среди всех сообщений только упоминаний о банкротстве.

## Simple API

Добавлена работа как простого веб-сервиса.

Есть следующие варианты запросов:

1. /create_task/taskname - создать задачу поиска по фразе "taskname"

2. /tasks/taskname - получить результаты поиска для фразы "taskname"

## Docker build and execute

Для билда выполнить

    docker build -t=fedres .

и далее для запуска контейнера
    
    docker run --net=host -it -p 8081:8081 fedres:latest
