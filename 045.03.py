#!/usr/bin/python3
'''
Напишите программу, которая меняет местами столбцы в матрице.
Формат входных данных
На вход программе на разных строках подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа ii и jj — номера столбцов, подлежащих обмену.
Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.
'''

n, m = int(input()), int(input())
matrix = []
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
x, y = [int(i) for i in input().split()]
        
for i in range(n):
    matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
    
for q in range(n):
    print(*matrix[q])