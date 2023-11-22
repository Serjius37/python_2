#!/usr/bin/python3
'''
Магическим квадратом порядка nn называется квадратная таблица размера n×nn×n, составленная из всех чисел 1,2,3,…,n21,2,3,…,n2 (то есть все числа разные) так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.
Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
'''

n = int(input())
matrix = []
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
digits = [i for i in range(1, n**2 + 1)]

d1, d2 = 0, 0
for i in range(n):
    stolbsum, strokasum = 0, 0
    for j in range(n):
        stolbsum += matrix[j][i]
        strokasum += matrix[i][j]
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    d1 += matrix[i][i]
    d2 += matrix[i][n - i - 1]
    if stolbsum != strokasum:
        break
if stolbsum == strokasum == d1 == d2 and digits == []:
    print("YES")
else:
    print("NO")