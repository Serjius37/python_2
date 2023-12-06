#!/usr/bin/python3
'''
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.
Формат входных данных
На вход программе подается количество пар синонимов nn. Далее следует nn строк, каждая строка содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.
Формат выходных данных
Программа должна вывести одно слово, синоним введенного.
Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.
Примечание 2. Все слова в словаре начинаются с заглавной буквы.
'''

words = {}

for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a 

print(words[input()])
