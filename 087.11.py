#!/usr/bin/python3
'''
Даны оценки по математике трёх учеников в 1010-балльной шкале. Напишите программу, которая выводит такие оценки, которые встречаются не более, чем у двух учеников.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
'''

s1 = set(int(i) for i in input().split())
s2 = set(int(i) for i in input().split())
s3 = set(int(i) for i in input().split())

print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3)))