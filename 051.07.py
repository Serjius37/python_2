#!/usr/bin/python3
'''
На шахматной доске 8×88×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.
Формат входных данных
На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номер строки (цифра от 11 до 88, снизу вверх)).
Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
'''

x, y = input()
n = 8 
matrix = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97

for i in range(n):
    for q in range(n):
        if i == y or q == x:
            matrix[i][q] = "*"
        elif (i + q == y + x) or (i - q == y - x):
            matrix[i][q] = "*"

matrix[y][x] = "Q"
for x in range(n):
    print(*matrix[x])