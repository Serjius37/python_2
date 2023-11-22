#!/usr/bin/python3
'''
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.
Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
'''

n = int(input())
matrix = []
flag = True
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
matrix.reverse()

for i in range(n):
    for q in range(n):
        if matrix[i][q] != matrix[q][i]:
            flag = False
            break
            

if flag:
    print('YES')
else:
    print('NO')