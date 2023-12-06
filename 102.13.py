#!/usr/bin/python3
'''
Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:

    00 на zero;
    11 на one;
    22 на two;
    33 на three;
    44 на four;
    55 на five;
    66 на six;
    77 на seven;
    88 на eight;
    99 на nine.

Формат входных данных
На вход программе подается натуральное число.
Формат выходных данных
Программа должна вывести строковое представление числа.
Примечание. Используйте словарь вместо условного оператора.
'''

n = input()
d = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

for x in n:
    print(d[x], end = ' ')
    
