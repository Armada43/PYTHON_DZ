

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# input_str=input('введите строку: ')
# text1="абв"
# input_list=input_str.split()
# result_list=[]
# for word in input_list:
#     if text1 not in word:
#         result_list.append(word)
# print(' '.join(result_list))     

# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# play1 = input("Введите имя игрока1: ")
# play2 = input("Введите имя игрока2: ")
# value = int(input("Введите количество конфет: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {play1}")
# else:
#     print(f"Первый ходит {play2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(play1)
#         count1 += k
#         value -= k
#         flag = False
#         p_print(play1, k, count1, value)
#     else:
#         k = input_dat(play2)
#         count2 += k
#         value -= k
#         flag = True
#         p_print(play2, k, count2, value)

# if flag:
#     print(f"Выиграл {play1}")
# else:
#     print(f"Выиграл {play2}")


# 4. Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`


def encode(s):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding


def read_data(file):
     with open(str(file),'r') as data:
        input_string=data.read()
     return input_string
 
input_text = "C:\\Users\\Asus\Desktop\\PYTHON\\stroka.txt"   

text1="C:\\Users\\Asus\Desktop\\PYTHON\\stroka1.txt" 
print(read_data(input_text))
print(encode(read_data(input_text))) 
with open(str(text1),'w') as data:
    data.write(encode(read_data(input_text))) 