#!/usr/bin/python3
'''
Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть. У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.
Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.
Формат входных данных
На вход программе в первой строке подается натуральное число mm — количество книг в домашней библиотеке Руслана. Во второй строке записано натуральное число nn —  количество книг в списке на лето. Далее идут mm строк с названиями книг из домашней библиотеки и nn строк названий из списка на лето.
Формат выходных данных
Программа должна вывести nn строк, в каждой из которых написано слово YES, если книга найдена в библиотеке, и NO, если нет.
'''

a , n = int(input()), int(input())
s = {input() for i in range(a)}

for i in range(n):
    if input() in s:
        print('YES')
    else:
        print('NO')