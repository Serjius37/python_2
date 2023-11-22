#!/usr/bin/python3
'''
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×mn×m, заполнив её "диагоналями" в соответствии с образцом.
Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.
Примечание. Для вывода элементов матрицы как в примерах отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
'''

x = input().split()
n, m = int(x[0]), int(x[1])
matrix = []
for _ in range(n):
    tmp = [c for c in range(m)]
    matrix.append(tmp)

count = 1
for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = count
                count += 1
            
for i in range(n):
    for q in range(m):
        print(str(matrix[i][q]).ljust(3), end = " ")
    print()


y, x = [ int(_) for _ in input().split()]
table = []
for _ in range(y):
    table.append([''] * x )
count = 0
max = x + y - 1
for k in range(max):
    for i in range(k + 1):
        if i >= y or k - i >= x: continue
        count = count + 1
        #print(f"i = {i}, k = {k}, table[{i}][{k-i}] = {count}")
        table[i][k-i] = count
    
for i in range(y):
    print(*table[i])
