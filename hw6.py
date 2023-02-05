# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

# n = input('Введите ваше число:\n')
# print(int(n)+int(n*2)+int(n*3))


# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

# import random


# list1 = list(random.randint(0, 10) for x in range(15))
# print(list1)
# number = input('Введите ваше число:\n')
# print(number)
# list1 = str(list1).replace(", ","")
# if number in list1:
#     print("да")
# else:
#     print('нет')


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

# def gcd(a,b):
#     while(b>0):
#         a, b = b, a % b
#     return a
    
# def simplify(pair):
#     g = gcd(pair[0], pair[1])
#     return (pair[0]//g, pair[1]//g)
    
# result = []
# for i in range(1, 12):
#     for j in range(i+1, 12):
#         pair = simplify((i, j))
#         result.append(pair)
# result = list(set(result))
# for q in sorted(result, key = lambda x: x[0]/x[1]): 
#     print(str(q[0]) + "/" + str(q[1]))