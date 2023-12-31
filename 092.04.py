#!/usr/bin/python3
'''
Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур,
 однако к концу игры ввиду своего возраста забывают, какие города уже называли.
Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.
Формат входных данных
На вход программе в первой строке подаётся натуральное число nn – количество названных городов,
 в последующих nn строках вводятся названные города и ещё одна строка с новым, только что названым городом.
Формат выходных данных
Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT, если город уже был назван.
'''

s = [input() for _ in range(int(input()) + 1)]

if len(s) == len(set(s)):
    print('OK')
else:
    print('REPEAT')