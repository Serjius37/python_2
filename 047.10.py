#!/usr/bin/python3
'''
Напишите программу, которая перемножает две матрицы.
Формат входных данных
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''

n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for j in range(n)]
input()
n2, m2 = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for j in range(n2)]
matrix3 = [[0] * m2 for _ in range(n)]

for i in range(n):
    for q in range(m2): 
        for k in range(m):
            matrix3[i][q] += matrix1[i][k] * matrix2[k][q]
            
for x in matrix3:
    print(*x)
    