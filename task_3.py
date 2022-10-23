# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
def write_polynom(k, list_rat):
    str_pol = ''
    for i in range(1, k):           # заполняем "середину" многочлена
        ratio = list_rat.pop(list_rat.index(random.choice(list_rat)))
        str = f'{ratio}x^{i}'
        if ratio == 0: str = ''
        else: str_pol = str + ' + ' + str_pol
    ratio = list_rat.pop(list_rat.index(random.choice(list_rat)))
    if ratio != 0: str_pol = f'{ratio}x^{k} + ' + str_pol # обязательно смотрим чтобы коэффициент первого эл-та не был 0
    else:
        ratio = list_rat.pop(list_rat.index(random.choice(list_rat)))
        str_pol = f'{ratio}x^{k} + ' + str_pol
    ratio = list_rat.pop(list_rat.index(random.choice(list_rat))) # если последний коэффициент 0, его не пишем
    if ratio != 0: str_pol = str_pol + f'{ratio}' + ' = 0'
    else: str_pol = str_pol[:-2] + ' = 0'
    return str_pol
def list_ratio():   #заполняем список коэффициентов
    list_ratio = []
    for i in range(101):
        list_ratio.append(i)
    return list_ratio
try:
    k = int(input('Введите степень многочлена: '))
    str_pol = write_polynom(k, list_ratio())
    data = open('file.txt', 'w')
    data.writelines(str_pol)
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close
except: print('Введите натуральное число!!!')