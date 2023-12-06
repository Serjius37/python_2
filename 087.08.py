#!/usr/bin/python3
'''
На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
Формат входных данных
На вход программе подаются два натуральных числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.
'''

s1, s2 = set(input()), set(input())

if s1.isdisjoint(s2):
    print('NO')
else:
    print('YES')