#!/usr/bin/python3
'''
Даны по 1010-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
'''

s1 = set(int(i) for i in input().split())
s2 = set(int(i) for i in input().split())
s3 = set(int(i) for i in input().split())

print(*sorted(s3 - s2 - s1, reverse = True))