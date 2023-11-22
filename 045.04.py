#!/usr/bin/python3
'''
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
Формат выходных данны
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
'''

n = int(input())
matrix = []
flag = True
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
        
for i in range(n):
    for q in range(n):
        if matrix[i][q] != matrix[q][i] and i != q:
            flag = False
            break
    if flag == False:
        break
            
if flag:
    print("YES")
else:
    print("NO")