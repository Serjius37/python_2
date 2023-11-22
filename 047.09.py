#!/usr/bin/python3
'''
Напишите программу для вычисления суммы двух матриц.
Формат входных данных
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''

x = input().split()
n, m = int(x[0]), int(x[1])
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
z = input()
matrix2 = [[int(x) for x in input().split()] for _ in range(n)]
matrix3 = [[int(x) for x in range(m)] for _ in range(n)]

for i in range(n):
    for q in range(m):
        matrix3[i][q] = matrix1[i][q] + matrix2[i][q]
        
for i in range(n):
    print(*matrix3[i])