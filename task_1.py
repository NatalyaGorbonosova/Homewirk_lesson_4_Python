# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from operator import truediv
def divisors(n):
    list = []
    for i in range(1, n+1):
        if not n%i:
            list.append(i)
    return list
def simple_divisors(n, list_div):
    list_simple = [1, n]
    if list_simple == list_div: return True
    else: return False
try:
    N = int(input('Введите натуральное число: '))
    col = divisors(N)
    list_simple_div = []
    for e in col:
        if simple_divisors(e, divisors(e)): list_simple_div.append(e)
    print(list_simple_div)
except: print('Введите натуральное положительное число!!!')