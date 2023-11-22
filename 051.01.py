#!/usr/bin/python3
'''
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список. Напишите программу, которая разделяет список на вложенные подсписки так, что nn последовательных элементов принадлежат разным подспискам.
Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.
Формат выходных данных
Программа должна вывести указанный вложенный список.
Примечание. Графическая иллюстрация для 11 теста:
'''

x = input().split()
n = int(input())
s = [[] * n for _ in range(n)]
     
for i in range(n):
    for q in range(i, len(x), n):
        s[i].append(x[q])
       
print(s)