# 1. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# или

# lst = list(map(lambda x: float(x), input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# 2. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# float_num = input('введите число: ')
# print(type(float_num))
# sum = 0
# for i in float_num:
#       if i != '.':
#           sum += int(i)
# print(sum)

# или

# num=input('введите число: ')
# sum=sum([int(digit) for digit in num if digit.isdigit()])
# print(sum)

# 3. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# или
# def get_list_lenght(my_list):
#     if len(my_list) % 2 == 0:
#         a=len(my_list) // 2
#     else:
#         a=len(my_list) // 2+1
#     return a 
                      

# input_list=list(map(int, input('введите список чисел, разделенных пробелом: ').split()))
# list_2=[(input_list[i])*(input_list[len(input_list)-1-i]) for i in range(get_list_lenght(input_list))]
# print(input_list, list_2)


# 4. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")
# lst = [2, 4, 5, 9, 3]
# print(sum_odd_index(lst))

# или

input_list=input('введите список чисел, разделенных пробелом: ').split()
print(sum([int(input_list[i]) for i in range(1, len(input_list), 2) if input_list[i].isdigit()]))