# Это проект для стажировки
Задача: Реализовать HTTP-сервер для предоставления информации по географическим объектам

Stack: **Python, FastAPI, poetry, docker**

Для запуска есть два варианта:
* Первый:
    - `pip install poetry`
    - `poetry install`
    - `python script.py`
* Второй:
    - `docker-compose up`

> [!IMPORTANT]
> После вы сможете найти сервис на: **0.0.0.0:8000/docs**

# Описание методов
`/{geonameid}` -- Метод принимает идентификатор geonameid и возвращает информацию о городе.

`/pages/` -- Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией.

`/tow-city/` -- Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах
