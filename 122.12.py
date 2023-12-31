#!/usr/bin/python3
'''
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.
Формат входных данн
На вход программе в первой строке подается число nn – общее количество учеников. Далее идут nn строк, содержащих имена и фамилии учеников.
Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного друга, разделённые дефисом.
Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для нескольких учеников.
Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных друзей.
'''

import random

my_list = [input() for _ in range(int(input()))]

random.shuffle(my_list)

for i in range(len(my_list)):
    print(f'{my_list[i - 1]} - {my_list[i]}')