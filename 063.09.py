#!/usr/bin/python3
'''
Напишите программу, которая выводит список хорошистов и отличников в классе.
Формат входных данных
На вход программе подается натуральное число nn, далее следует nn строк с фамилией школьника и его оценкой на каждой из них.
Формат выходных данных
Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).
Примечание 1. Оценка ученика – это натуральное число от 11 до 55.
Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист – обладатель оценки 44, или отличник – получивший 55.
'''

s = [tuple(input().split()) for i in range(int(input()))]

for i in s:
    print(*i)
print()
    
for i in s:
    if int(i[1]) >= 4:
        print(*i)