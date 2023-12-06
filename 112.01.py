#!/usr/bin/python3
'''
Как известно из курса биологии ДНК и РНК – последовательности нуклеотидов.
Четыре нуклеотида в ДНК:

    аденин (A);
    цитозин (C);
    гуанин (G);
    тимин (T).
Четыре нуклеотида в РНК:

    аденин (A);
    цитозин (C);
    гуанин (G);
    урацил (U).
Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:

    G →→ C;
    C →→ G;
    T →→ A;
    A →→ U.
Напишите программу, переводящую цепь ДНК в цепь РНК.
Формат входных данных
На вход программе подается корректная цепь ДНК в верхнем регистре.
Формат выходных данных
Программа должна вывести соответствующую цепь РНК в верхнем регистре.
Примечание. Подробнее прочитать про ДНК и РНК можно тут и тут.
'''

my_dict = {'A' : 'U', 'C' : 'G', 'G' : 'C', 'T': 'A'}

result = [my_dict[i] for i in input()]

print(*result, sep = '')


