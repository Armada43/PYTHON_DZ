# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# float_num = input('input float number: ')
# print(type(float_num))
# sum = 0
# for i in float_num:
#      if i != '.':
#          sum += int(i)
# print(sum)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n - 1)


# num = int(input("Введите число: "))

# list = []
# for i in range(1, num + 1):
#     list.append(mult(i))

# print(list)

# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('введите n: '))
# lst = [round((1+1/i)**i, 2)
#  for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 2)}')

#4.Реализуйте алгоритм перемешивания списка.

list = ['Веселый пианист', 250, 3.14, 'True ']
print(list) 
import random
random.shuffle(list)
print('->', list) 
