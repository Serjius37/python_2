#!/usr/bin/python3
'''
Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа ππ.
Примечание 1. Площадь единичного круга, то есть круга с радиусом, равным R=1R=1 равна S=πR2=πS=πR2=π.
Примечание 2. Уравнение единичной окружности имеет вид x2+y2=1x2+y2=1.
'''

import random

n = 10**6       # количество испытаний
k = 0
s0 = 4

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x ** 2 + y ** 2 <= 1:
        k += 1
        
print((k / n) * s0)