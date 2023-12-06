#!/usr/bin/python3
'''
Ученики 1010 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

    "Что такое математика?";
    "Математическая составляющая";
    "100 гениальных идей по математике".

Оказалось, что nn учеников прочитали первую книгу, mm учеников — вторую, kk учеников — третью. Также известно, что xx учеников прочли первую или вторую, или обе эти книги, yy учеников — вторую или третью, или обе, zz учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только tt учеников. Всего в 1010 классе учится aa учеников. Напишите программу, которая выводит сколько учеников:

    прочитали только одну книгу;
    прочитали две книги;
    не прочитали ни одной из рекомендованных книг.
Формат входных данных
На вход программе подаются числа n,m,k,x,y,z,t,an,m,k,x,y,z,t,a, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.
'''

n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
s1 = n + m - x - t
s2 = m + k - y - t
s3 = n + k - z - t
s = (n - s1 - s3 - t) + (m - s1 - s2 - t) + (k - s2 - s3 - t)
print(s) 
print(s1 + s2 + s3)
print(a - s - s1 - s2 - s3 - t)