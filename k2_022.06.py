#!/usr/bin/python3
'''
Напишите программу для определения, является ли число произведением двух чисел из данного набора. Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
Формат входных данных
В первой строке подаётся число n (0<n<1000)n(0<n<1000) – количество чисел в наборе. В последующих nn строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.
Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.
Примечание 1. Само на себя число из набора умножиться не может. Другими словами, два множителя должны иметь разные индексы в наборе.
Примечание 2. Для решения задачи используйте вложенные циклы.
'''

s = [int(input())for _ in range(int(input()))]
k = int(input())
flag = False
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] * s[j] == k and i != j:
            flag = True
            break
if flag:
    print("ДА")
else:
    print("НЕТ")