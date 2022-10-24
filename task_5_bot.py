# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. 
# Тема чат-бота любая
from random import *
import json
def print_students(book):
    for x, y in book.items():
        print(x, y)
def save():
    with open('students.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(students, ensure_ascii=False))
    print('Список учеников успешно сохранен в файл students.json')
def load():
    with open('students.json', 'r', encoding='utf-8') as fh:
        students = json.load(fh)
        print('Журнал учеников загружен')
try:
    students = {}
    with open('students.json', 'r', encoding='utf-8') as fh:
        students = json.load(fh)
        print('Журнал учеников загружен')
except:
    students = {'Софья': {'class': 10, 'topic': 'Степень с рац показателем', 'time':'пн, пт 19:00'},
                'Ника': {'class': 10, 'topic': 'Параллельные прямые в пр-ве', 'time':'пн 20:30, чт 16:00'},
                'Лиза': {'class': 7, 'topic': 'Метод группировки', 'time':'вт 17:00, пт 14:00'},
                'Алина': {'class': 8, 'topic': 'Иррациональные числа', 'time':'вт 16:00'}}

while True:
    command = input('Введите команду: ')
    if command == '/start':
        print('Список учеников готов к работе')
    elif command == '/stop':
        print('Прекращение работы со списком')
        save()
        break
    elif command == '/all':
        print('Вот текущий список учеников')
        print_students(students)
    elif command == '/add':
        name = input('Введите имя ученика: ')
        class_st = input('Введите класс ученика: ')
        topic = input('Введите тему: ')
        time = input('Введите время занятий: ')
        students[name] = {'class': class_st, 'topic': topic, 'time': time}
        print('Ученик записан')
    elif command == "/save":
        save()
    elif command == "/delete":
        name = input('Введите имя ученика, которого хотите удалить')
        try:
            del students[name]
            print('Ученик удален')
        except:
            print('Такого ученика нет')
    elif command == '/upgrade':
        name = input('Введите имя ученика, данные которого меняете: ')
        key = input('Введите что меняете: class, topic, time: ')
        try:
            students[name][key] = input('Измененные значения: ')
            print('Изменения сохранены')
        except:
            print('Такого ученика нет')
    elif command == '/load':
        load()
    elif command == '/random':
        name_list = []
        for x in students.keys():
            name_list.append(x)
        name = choice(name_list)
        book = students[name]
        print('Случайный ученик: ' + name)
        print(book)
    elif command == '/help':
        print('Доступные команды: /start, /stop, /all, /add, /save, /delete, /upgrade, /load, /random')
    else:
        print('Неопознанная команда. Просьба изучить список команд через /help')