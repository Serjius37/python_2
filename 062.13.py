#!/usr/bin/python3
'''
Дополните приведенный код, используя операторы конкатенации (+) и умножения кортежа на число (*), чтобы он вывел кортеж:
 (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13).
'''

numbers1 = ((1, 2, 3) * 2)
numbers2 = ((6,) * 9)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
print(numbers1 + numbers2 + numbers3)
