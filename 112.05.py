#!/usr/bin/python3
'''
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей переданного списка.
Примечание 1. Следующий программный код:
result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
создает словарь:
result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
Примечание 2. Вызывать функцию merge() не нужно, требуется только реализовать. 
Примечание 3. Слияниепустых словарей должно быть пустым словарем.
'''

def merge(values):      # values - это список словарей
    result = {}
    for d in values:
        for key in d:
            result.setdefault(key, set()).add(d[key])
    return result
