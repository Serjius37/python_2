#!/usr/bin/python3
'''
На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.
Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
Формат выходных данных
Программа должна вывести множество чисел, встречающихся только в первой строке.
'''

s1, s2 = set(int(i) for i in input().split()), set(int(i) for i in input().split())
print(*sorted(s1 - s2))