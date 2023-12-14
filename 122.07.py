#!/usr/bin/python3
'''
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).
Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.
Примечание 1. Пример правильного (неправильного) индекса Латверии:
AB23_56VG          # правильный
V3F_231GT          # неправильный
Примечание 2. Обратите внимание на символ _ в почтовом индексе.
Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
'''

from random import choice, randint
import string

def generate_index():
    up_letter = string.ascii_uppercase
    s1, s2, s3, s4 = (choice(up_letter) for _ in range(4))
    num1, num2 = (randint(0, 99) for _ in range(2))
    return f"{s1}{s2}{num1}_{num2}{s3}{s4}"