#!/usr/bin/python3
'''
Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв, слова разделены одним пробелом или несколькими.
Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра. Для первого вхождения слова программа выведет 11, для второго вхождения того же слова — 22 и т. д.
Формат входных данных
Программа получает на вход единственную строку текста, состоящую только из русских букв и символов пробела. 
Формат выходных данных
Для каждого слова исходного текста программа выводит одно целое число — номер вхождения этого слова в текст. Числа необходимо вывести на одной строке через пробел.
Примечание. Количество чисел должно совпадать с количеством слов исходного текста.
'''

s = input().split()
result = {}

for i in s:
    result[i] = result.get(i, 0) + 1
    print(result[i], end = ' ' )