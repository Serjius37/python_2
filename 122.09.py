#!/usr/bin/python3
'''
Напишите программу, которая с помощью модуля random генерирует 100100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

    номер не может начинаться с нулей;
    номер лотерейного билета должен состоять из 77 цифр;
    все 100100 лотерейных билетов должны быть различными.

'''

import random 

my_set = set()

while len(my_set) != 100:
    my_set.add(random.randint(1800800, 9999999))

print(*my_set, sep='\n')
