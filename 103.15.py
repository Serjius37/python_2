#!/usr/bin/python3
'''
Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
'''

s = input().lower().split()
x = [word.strip('.,!?:;-') for word in s]
my_dict = {}

for i in x:
    my_dict[i] = x.count(i)
    
result = {}
min_count = min(my_dict.values())

for key, value in my_dict.items():
    if value == min_count:
        result[key] = value
        
print(min(result))

