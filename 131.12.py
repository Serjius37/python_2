#!/usr/bin/python3
'''
Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.
'''

from decimal import *
num = Decimal(input())

num_tuple = num.as_tuple().digits

print(max(num_tuple) + min(num_tuple) * (abs(num) >= 1))