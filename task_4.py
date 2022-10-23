# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь. 
# например, 6*x^2+5*x+6=0 . 
# Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.
import math
def equation_standart(equat):   #Приводит уравнение к стандартному виду
    standart = equat.replace(" ", '')
    standart1 = standart.replace('*', '')
    return standart1
def equqtion_ratio(equation):   #возвращает список коэффициентов уравнения
    for i in range(len(equation)):  # находит а
        if equation[i] == 'x' and equation[i+1] == '^' and i != 0:
            if equation[0] == '-' and i == 1:
                a = -1
                equation = equation[i + 3: len(equation)]
            else:
                a = int(equation[0:i])
                equation = equation[i + 3: len(equation)]   
            break
        elif equation[i] == 'x' and equation[i+1] == '^' and i == 0:
            a=1
            equation = equation[i + 3: len(equation)]
            break
        else: 
            a = 0
    for e in equation: # находит b
        if e == 'x' and equation.index(e) != 1 and a != 0:
            i = equation.index(e)
            b = int(equation[0: i])
            equation = equation[i+1: len(equation) ]
            break
        elif e == 'x' and equation.index(e) == 1 and equation[0] == '+':
            b = 1
            i = equation.index(e)
            equation = equation[i+1: len(equation) ]
            break
        elif e == 'x' and equation[0] == e:
            b = 1
            i = equation.index(e)
            equation = equation[i+1: len(equation) ]
            break
        elif e == 'x' and equation.index(e) == 1 and equation[0] == '-':
            b = -1
            i = equation.index(e)
            equation = equation[i+1: len(equation) ]
            break
        elif a == 0 and e == 'x' and equation.index(e) != 0:
            i = equation.index(e)
            b = int(equation[0: i])
            equation = equation[i+1: len(equation) ]
            break
        else: b=0
    for e in equation: # находит с
        if e == '=':
            i = equation.index(e)
            c = int(equation[0:i])
            break
        else: c=0
    list_ratio = [a, b, c]
    return list_ratio
def discreminant(a, b, c): # находит дискреминант
    dis = b**2 - 4*a*c 
    return dis
def solution(d, a, b): # решает квадратное уравнение при а не ноль
    if d > 0:
        print('Два корня: ')
        print(f'x1 = {(-b + math.sqrt(d))/(2*a)}')
        print(f'x2 = {(-b - math.sqrt(d))/(2*a)}')
    elif d == 0:
         print('Один корень:')
         print(f'x = {(-b )/(2*a)}')
    else: print('Нет решений')

try:
    equation = input('Запишите уравнение: ')
    equation = equation_standart(equation)
    print(equation)
    list_rat = equqtion_ratio(equation)
    print(list_rat)
    A = list_rat[0]
    B = list_rat[1]
    C = list_rat[2]
    if A != 0:
        D = discreminant(A, B, C)
        solution(D, A, B)
    elif A==0 and B !=0 : print(f'Это линейное уравнение, его решение: {-C/B} ')
    else: print('Решений нет')
except: print('wrong')