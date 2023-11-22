#!/usr/bin/python3
'''
Таблица умножения
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n×mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
Формат входных данных
На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 33 символа (для этого используйте строковый метод ljust()).
'''

n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    matrix.append([0] * m)
#for k in range(n):
#    matrix.append([x for x in range(m)])

    
for i in range(n):
    for q in range(m):
        matrix[i][q] = i * q
        
for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end = ' ')
    print()