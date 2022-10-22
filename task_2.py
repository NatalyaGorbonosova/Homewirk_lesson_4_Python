# задача 2 . Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
def unic_elements(array):
    unic_array = []
    for e in array:
        if e not in unic_array: unic_array.append(e)
    return unic_array
try:
    list = list(map(int, input('Введите числа последовательности через пробел: ').split()))
    print(list)
    unic_list = unic_elements(list)
    print(unic_list)
except: print('Вводите числа!!!')