#!/usr/bin/python3
'''
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.
Формат входных данных
На вход программе подается одно число n  (n≤100)n (n≤100) – количество членов последовательности.
Формат выходных данных
Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.
Примечание. Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:
1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …
1,1,1,3,5,9,17,31,57,105 …
'''

n = int(input())
x1, x2 ,x3 = 1, 1, 1
for i in range(n):
    print(x1, end = ' ')
    x1 ,x2, x3 = x2, x3, x1 + x2 +x3
