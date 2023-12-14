#!/usr/bin/python3
'''
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (маленькая и большая буквы);
    «0» (цифра).
Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с условием задачи, каждый на отдельной строке.
Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые пароли сгенерировать возможно.
Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре.
Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:
    функция generate_password(length) – возвращает случайный пароль длиной length символов;
    функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.
'''

import random
import string


def generate_password(length):
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
    symbols = ''.join([symbol for symbol in symbols if symbol not in 'IloO'])
    return ''.join(random.sample(symbols, length))

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')