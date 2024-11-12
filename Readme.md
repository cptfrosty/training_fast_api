# Документация по тренировочному проекту FastApi
Данный веб-сервис выполнен для ознакомительной работы с FastApi

Использовалась программа PyCharm Community Edition 2024.2.4
Внутри проекта используется SQLite

##Запуск проекта
Шаг 1. Запустите main.py
Шаг 2. Перейдите по адресу http://localhost:8080/docs#/

/Root - возвращает все данные
/{item_id} - возвращает конкретный элемент по id

##Заполнение данных
Внутри database_scripts.py присутствует участок кода:

```
items = [
    (1, 'Вентилятор BINATONE ALPINE 160вт, напольный ,', 1, 0, 'Вентилятор BINATONE ALPINE 160вт, напольный , оконный'),
    (2, 'Вентилятор JIPONIC (Тайв.),', 1, 0, 'Вентилятор JIPONIC (Тайв.), напольный'),
    (3, 'Вентилятор настольный', 1, 0, 'Вентилятор настольный'),
    (4, 'Вентилятор ОРБИТА,STERLING,ЯП.', 1, 0, 'Вентилятор ОРБИТА,STERLING,ЯП.'),
    (5, 'Пылесос "Омега" 1250вт', 1, 0, 'Пылесос "Омега" 1250вт'),
    (6, 'Телевизор "SHARP"', 3, 0, 'Телевизор "SHARP"'),
    (7, 'Набор кухонной мебели (цвет белый)', 4, 0, 'Набор кухонной мебели (цвет белый)'),
]


def insert_testdata():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO items VALUES(?, ?, ?, ?, ?)", items)
    connection.commit()
    connection.close()
```

Для заполнения данных необходимо прописать в консоли Python
```
>>> from database_scripts import insert_testdata
>>> insert_testdata()
```