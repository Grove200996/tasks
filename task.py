
# my_list = [i ** 3 for i in range(1, 1000, 2)]
# # print(my_list)
# summ = 0
# for number in my_list:
#     number_2 = str(number)
#     digits_summ = 0
#     for inner_number in number_2:
#         digits_summ += int(inner_number)
#     if digits_summ % 7 == 0:
#         summ += number
# print(summ)

""" 0. Вывести квадрат числа."""
# quad = lambda x: x**2
# print(quad(5))

"""1. По двум заданным числам проверять является ли первое квадратом второго"""
# def is_quad_1(x,y)
#    if x ** 2 == y:
#         return print('it is')
#    else:
#         return print("no, it's not")
"""2. Даны два числа. Показать большее и меньшее число"""
# num_1 = int(input())
# num_2 = int(input())
# max_num = 0
# min_num = 0
# if num_1 > num_2:
#     max_num = num_1
#     min_num = num_2
# if num_2 > num_1:
#     max_num = num_2
#     min_num = num_1
# print(f'Максимальное - {max_num}\nМинимальное - {min_num}')
###########################
# numbers = []
# numbers.append(int(input('Введите первое число: ')))
# numbers.append(int(input('Введите второе число: ')))
# print(f'Максимальное - {max(numbers)} \nМинимальное - {min(numbers)}')
""" 3. По заданному номеру дня недели вывести его название"""
# days = ['Воскресенье','Понедельник','Вторник','Среда','Четверг',"Пятница","Суббота"]
# number = int(input('Введите номер дня недели: '))
# if number == 0:
#     print('Такого дня не бывает')
# else:
#     print(days[number-1])

""" 4. Найти максимальное из трех чисел"""
# numbers = []
# numbers.append(int(input('enter a number: ')))
# question = input('do you want to add more?: y/n ')
# for i in numbers:
#     if question == 'y':
#         numbers.append(int(input('enter a number: ')))
#         question = input('more?: ')
#     elif question == 'n':
#         print(max(numbers))
""" 5. Написать программу вычисления значения функции y = f(a)"""
# x = (int(input('Задайте значение x: ')))
# y = 0
# if x == 0:
#     y = 0
# elif x < 0:
#     y = x * (-1)
# else:
#     y = x - 2
# print(y)
""" 6. Выяснить является ли число чётным """
# num = int(input('enter a number: '))
# if num % 2 == 0:
#     print(f'{num} является чётным')
# else:
#     print(f'{num} не является чётным')
""" 7. Показать числа от -N до N """
# n = int(input('enter a number: '))
# a = (-n)
# while a <= n:
#     print(a)
#     a += 1
""" 8. Показать четные числа от 1 до N """
# num = int(input('enter a number: '))
# even = []
# for i in range(1,num+1):
#     if i % 2 == 0:
#         even.append(i)
# print(even)
""" 9. Показать последнюю цифру трёхзначного числа """
# n = int(input('enter a three digit number: '))
# print(n%10)
""" 10. Показать вторую цифру трёхзначного числа """
# n = int(input('enter a three digit number: '))
# print((n % 100) // 10)
""" 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа """
# n = int(input('enter a number between 10 and 99: '))
# a = n % 10
# b = n // 10
# if a > b:
#     print(a)
# if a < b:
#     print(b)
""" 12. Удалить вторую цифру трёхзначного числа """
# n = int(input('enter a three digit number: '))
# a = n // 100
# b = n % 10
# a = a * 10
# print(a + b)
###########################################
# number = ''
# for i in str(n):
#     number += i
# new_number = number.replace(number[1],'')
# print(int(new_number))

""" 13. Выяснить, кратно ли число заданному, если нет, вывести остаток. """
# num = int(input())
# x = int(input())
# left = 0

# if num % x == 0:
#     print(f'число {num} кратно {x}')

# else:
#     left = num % x
#     print(f'число {num} не кратно {x}. Остаток от деления - {left}')
""" 14. Найти третью цифру числа или сообщить, что её нет """
# def number(x):
#     if x < 99:
#         return f'number has no third digit'
#     elif x > 999:
#         while x > 999:
#             x //= 10
#         return x % 10
#     else:
#         return x % 10
# print(number(93))
""" ## Почувствуй себя джуном*

15. Дано число. Проверить кратно ли оно 7 и 23 """
# number = int(input())
# if number % 7 == 0 and number % 23 == 0:
#     print('number is')
# else:
#     print('number is not')
# 1288
""" 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным """
# days = ['Воскресенье','Понедельник','Вторник','Среда','Четверг',"Пятница","Суббота"]
# number = int(input('Введите номер дня недели: '))
# if number == 0:
#     print('Такого дня не бывает')
# elif number == 7:
#     print(f'{days[-1]} - выходной день.')
# elif number == 1:
#     print(f'{days[0]} - выходной день.')
# else:
#     print(days[number-1])
""" 17. По двум заданным числам проверять является ли одно квадратом другого """

# def is_quad(x,y):
#      if x ** 2 == y or y ** 2 == x:
#           return print('it is')
#      else:
#           return print("no, it's not")
# is_quad(4,2)

""" 19-20. Определить номер четверти плоскости
    в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0 """

# def quarter(x, y):
#     a = 'it belongs to I quarter\nЕсли у точки обе координаты (x и y) положительны, то она принадлежит первой четверти.'
#     b = 'it belongs to II quarter\nЕсли координата x отрицательна, а y положительна, то точка находится во второй четверти.'
#     c = 'it belongs to III quarter\nЕсли обе координаты отрицательны, то точка принадлежит третьей координатной четверти.'
#     d = 'it belongs to IV quarter\nЕсли x положительна, а y отрицательна, то точка находится в IV четверти.'
#     if x < 0 and y > 0:
#         return b
#     elif x > 0 and y > 0:
#         return a
#     elif x < 0 and y < 0:
#         return c
#     elif y < 0 < x:
#         return d
#     else:
#         return f'X ≠ 0 и Y ≠ 0'
# print(quarter(-3,2))
""" 21. Программа проверяет пятизначное число на палиндромом."""
# num = (int(input('enter a number: ')))
# num = str(num)
# if num == num[::-1]:
#     print('Является палиндромом')
# else:
#     print('Не является')
#########
# def is_palindrom(string):
#     reversed_string = ''
#     for i in range(len(string),0,-1):
#         reversed_string += string[i-1]
#         if string == reversed_string:
#             print('Является палиндромом')
#         else:
#             print('Не является')
# is_palindrom('racecar')

"""## Почувствуй себя мидлом*

23. Показать таблицу квадратов чисел от 1 до N """
# def quads(number):
#     return print([i**2 for i in range(1, number + 1)])

# quads(10)

""" 24. Найти кубы чисел от 1 до N """
# def cubes(number):
#     return print([i**3 for i in range(1, number + 1)])
# cubes(10)
""" 25. Найти сумму чисел от 1 до А """
# def summ_finder(number):
#     summ = 0
#     for i in range(1,number+1):
#         summ += i
#     return print(summ)
# summ_finder(3)
""" 26. Возведите число А в натуральную степень B используя цикл """
# def exponentiation(a,b):
#     summ = 1
#     i = 0
#     while i < b:
#         summ = summ * a
#         i += 1
#     return print(summ)
# exponentiation(2,4)

""" 27. Определить количество цифр в числе """
# def number_of_digits(number):
#     count = 0
#     for i in str(number):
#         count += 1
#     return print(count)
# number_of_digits(21323)
##########
# def number_of_digits(number):
#     count = 1
#     while number > 10:
#         number = number// 10
#         count += 1
#     return print(count)
# number_of_digits(23)

""" 28. Подсчитать сумму цифр в числе """
# def summ_of_digits(number):
#     summ = 0
#     while number > 0:
#         summ += number % 10
#         number = number // 10
#     return (print(summ))
#######
# def summ_of_digits(number):
#     summ = 0
#     number = str(number)
#     for i in number:
#         summ += int(i)
#     return print(summ)
# summ_of_digits(12345)
""" 29. Написать программу вычисления произведения чисел от 1 до N """
# def product_of_numbers(number):
#     summ = 1
#     for i in range(1,number+1):
#         summ = summ * i
#     return print(summ)
# product_of_numbers(6)
########
# def product_of_numbers(n):
#     summ = 1
#     while n > 1:
#         summ = summ * n
#         n = n - 1
#     return print(summ)
# product_of_numbers(6)
""" 30. Показать кубы чисел, заканчивающихся на четную цифру """
# print([i**3 for i in range(2,100,2)])

""" 31. Задать массив из 8 элементов и вывести их на экран  """
# print([i for i in range(2**3)])

""" 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран """
# mylist = []
# for i in range(4):
#     mylist.append(0)
#     for j in range(1):
#         mylist.append(1)
# print(mylist)
"""  Задать массив из 12 элементов, заполненных числами
     из [0,9]. Найти сумму положительных/отрицательных элементов массива """
# def massive_huge_dick(a,b):
#     mylist = []
#     positive = 0
#     negative = 0
#     for i in range(a,b+1):
#         mylist.append(i)
#         if i < 0:
#             negative += i
#         elif i > 0:
#             positive += i
#     return print(f'Массив - {mylist}\nCумма положительных - {positive}\nСумма отрицательных - {negative}')
# massive_huge_dick(-2,9)
""" 34. Написать программу замену элементов массива на противоположные """
# import random
# def exchange(massive):
#     print(massive)
#     for i in range(len(massive)):
#         massive[i] = massive[i] * (-1)
#     return print(f'{massive}')
# exchange([random.randint(-20,20) for i in range(1,10)])
""" 35. Определить, присутствует ли в заданном массиве, некоторое число """
# import random
# mylist = ([random.randint(1,10) for x in range(6)])
# def golden_num(number,massive):
#     qqq = 0
#     for i in massive:
#         if i == number:
#             qqq += i
#     return True if qqq > 0 else False

# print(golden_num(2,mylist))
# print(mylist)
""" 36. Задать массив, заполнить случайными положительными трёхзначными числами.
     Показать количество нечетных\четных чисел """
# import random
# myl = ([random.randint(-999,999) for i in range(10)])
# negative = 0
# positive = 0
# for i in myl:
#     if i > 0:
#         positive += 1
#     else:
#         negative += 1
# print(negative,positive)
""" 37. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99] """
# myl = [i for i in range(1,124)]
# count = 0
# for i in myl:
#     if 10 <= i < 99:
#         count += 1
# print(count)
""" 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции """
# summ = 0
# myl = [i for i in range(1, 10+1)]
# for index in myl:
#     if index % 2 != 0:
#         summ += myl[index]
# print(summ)
""" 39. Найти произведение пар чисел в одномерном массиве.
     Парой считаем первый и последний элемент, второй и предпоследний и т.д. """
# import random
# myl = ([random.randint(1,10) for i in range(11)])
# print(myl)
# i = 0
# summ = 0
# size = len(myl)
# if size % 2 != 0:
#      print('Массив содержит нечетное количество чисел.')
# else:
#      while i < size:
#           summ = summ + (myl[i] * myl[size-1])
#           i += 1
#           size = size-1
#      print(summ)
""" 40. В Указанном массиве вещественных
 чисел найдите разницу между максимальным и минимальным элементом """
# import random
# myl = ([random.randint(10,99)for x in range(1,11)])
# print(myl)
# print(max(myl) - min(myl))

""" Почувствуй себя лидом*
41. Выяснить являются ли три числа сторонами треугольника """
# def triangle_qm(a,b,c):
#      if a+b>c and b+c>a and a+c>b:
#           return True
#      else:
#           return False
# print(triangle_qm(4,3,6))

""" 42. Определить сколько чисел больше 0 введено с клавиатуры """


# def more_than_zero(*numbers):
#     count = 0
#     for i in numbers:
#         if i > 0:
#             count += 1
#     return count


# print(more_than_zero(-2, -3, 1, 3, 4))

""" 43. Написать программу преобразования десятичного числа в двоичное """


# def system(num):
#     number = ''
#     num_1 = 0
#     while num > 0:
#         num_1 += num % 2
#         num = num // 2
#         number += str(num_1)
#         num_1 = 0
#     return number[::-1]


# print(system(156))
""" 45. Показать числа Фибоначчи """


# def fibonacchi(n):
#      f1 = 1
#      f2 = 1
#      lists = []
#      while n > 2:
#           f1, f2 = f2, f2+f1
#           n -= 1
#           lists.append(f2)
#      return lists
# print(fibonacchi(15))

""" 47. Написать программу копирования массива """
# massive = ([i for i in range(-5, 5)])

# massive_copy = []
# for i in massive:
#     massive_copy.append(i)


# class Phone:
#     def __init__(self, phone_model):
#         self.model = phone_model
#         self.loading(self.model)

#     def loading(self, model):
#         print(f'{model} is loading...')

#     def call(self):
#         print('phone is calling')

#     def music_player(self):
#         print('your favorite song is playing')


# phone = Phone('nokia')
# phone.call()


class Person:
    def __init__(self, name, surname, age, wage):
        self.name = name
        self.surname = surname
        self.age = age
        self.wage = wage

    def name(self):
        return name

    def surname(self):
        return surname

    def age(self):
        return age

    def wage(self):

        return wage


class Boss(Person):
    def __init__(self, name, surname, age, wage, car):
        super().__init__(name, surname, age, wage)
        self.car = car

    def car(self):
        return f'boss has {car}'


p = Person('Евгений', "Степанов", 26, 100.000)
b = Boss('Евгений', "Степанов", 26, 100.000, 'lexus')
print(p.age)
print(b.name)
print(b.car)
