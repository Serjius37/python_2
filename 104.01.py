#!/usr/bin/python3
'''
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.
Формат входных данных
В первой строке задано одно целое число nn — количество слов в словаре. В следующих nn строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число mm — количество поисковых слов, чье определение нужно вывести. В следующих mm строках записаны сами слова, по одному на строке.
Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.
Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.
Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт пробел.
'''

my_dict = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    my_dict[key.lower()] = value
    
for _ in range(int(input())):
    key = input().lower()
    print(my_dict.get(key, "Не найдено"))


    