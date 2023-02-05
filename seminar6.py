# Задача 0. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.
# [7, 2, 4, 1, 6] –> да
# [7, 2, 4, 2, 6] -> нет

import random


# numbers = list(random.randint(1, 10) for x in range (random.randint(3, 7)))
# print(numbers)
# lenght_numbers = len(numbers)
# numbers = set(numbers)
# print(numbers)
# if len(numbers) == lenght_numbers:
#     print('уникальные эл-ты')
# else:
#     print("есть повторы")


# Задача 1. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.
# 72426, 27624 –> да
# 44444, 44441 -> нет

# number1 = str(random.randint(10000, 99999))
# print(number1)
# number2 = str(random.randint(10000, 99999))
# print(number2)
# number1 = "44444"
# number2 = "44441"
# number1 = list(number1)
# number2 = list(number2)
# count = 0
# for i in range(len(number1)):
#     if number1.count(number1[i]) != number2.count(number1[i]):
#         break
#     else:
#         count += 1
# if count == 5:
#     print('yes')
# else:
#     print('no')

# Задача 2. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких
# действий.
# 2+2 => 4 25 мин
# 1+2*3 => 7

# problem = (input('Введите ваш пример:\n'))
# print(problem)
# elements = None

# if '+' in problem:
#     elements = problem.split('+')
#     answer = int(elements[0]) + int(elements[1])
# elif '*' in problem:
#     elements = problem.split('*')
#     answer = int(elements[0]) * int(elements[1])
# elif '-' in problem:
#     elements = problem.split('-')
#     answer = int(elements[0]) - int(elements[1])
# elif '/' in problem:
#     elements = problem.split('/')
#     answer = int(elements[0]) / int(elements[1])
# print(answer)

# operation = None
# operators = ['-', '+', '/', '*']
# for operator in operators:
#     if operator in problem:
#         operation = operator
#         break
# elements = problem.split(operation)
# number1 = int(elements[0])
# number2 = int(elements[1])
# dict = {"+": number1 + number2,
# "-": number1 - number2,
# "*": number1 * number2,
# "/": number1 / number2}
# print(f'{problem} = {dict[operation]}')


# Задача 3. Имеется 1000 рублей. Бык стоит – 100
# рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все
# эти деньги, если всего надо купить 100 голов
# скота?    
# for b in range (1, 1000//100+1):
#     for k in range(1, 1000//50+1):
#         t = 100-b-k
#         if b*100+k*50+t*5 == 1000:
#             print("быки:", b, "коровы:", k, "телята:", t)

