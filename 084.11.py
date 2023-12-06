#!/usr/bin/python3
'''
Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию (в обратном лексикографическом порядке).
Примечание. Выводите каждый элемент множества на отдельной строке.
'''

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
fruits2 = sorted(fruits, reverse = True)

for x in fruits2:
    print(x)