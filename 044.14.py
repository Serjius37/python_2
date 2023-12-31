#!/usr/bin/python3
'''
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Элементы диагоналей не учитываются.
'''

n = int(input())
matrix = []
for k in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            sum1 += matrix[i][j]
        elif i < j and i > n - 1 - j:
            sum2 += matrix[i][j] 
        elif i > j and i > n - 1 - j:
            sum3 += matrix[i][j]  
        elif i > j and i < n - 1 - j:
            sum4 += matrix[i][j]  
print(f"Верхняя четверть: {sum1}")
print(f"Правая четверть: {sum2}")
print(f"Нижняя четверть: {sum3}")
print(f"Левая четверть: {sum4}")