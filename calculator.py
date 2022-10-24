""" Калькулятор, способный производить четыре действия!!"""

import time
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiplication(x, y):
        selection()
        print(f'ответ равен: {x*y}')
        selection()

    def subtraction(x, y):
        selection()
        print(f'ответ равен: {x-y}')
        selection()

    def addition(x, y):
        selection()
        print(f'ответ равен: {x+y}')
        selection()

    def division(x, y):
        selection()
        print(f'ответ равен: {x/y}')
        selection()
def selection():
    """Функция для выделения текста"""
    print('-'*40)


number = 0
x = 0
options = {1: 'сложение', 2: 'вычетание', 3: 'умножение',
           4: 'деление', 6: 'выход', 5: 'сбросить сумму'}
print(f'*'*40 + '\nЗдравствуйте! Вы запустили калькулятор.\n' + ('*'*40))


while number != 6:
    time.sleep(1)
    print(f'Выберите одну из предложенных функций:'
          f'\n1) {options[1]}\n2) {options[2]}\n3) {options[3]}\n4)'
          f' {options[4]}\n5) {options[5]}\n6) {options[6]}')

    choice = int(input())
    number = choice
    if number > 6:
        selection()
        print('Некорректный ввод')
        selection()
        continue
    print(f'Вы выбрали {options[choice]}.')
    time.sleep(1)
    if number == 5:
        selection()
        x = 0
        continue

    if number == 6:
        selection()
        print(f'Спасибо что воспользовались моим дебильным калькулятором :)')
        selection()
        time.sleep(2)
        break

    else:
        num = choice
        if x == 0:
            print('Введите числа: ')
            x = int(input())
            y = int(input())
        else:
            print('Введите число: ')
            y = int(input())
        if num == 3:
            Calculator.multiplication(x, y)
            x = x * y
        elif num == 1:
            Calculator.addition(x, y)
            x = x + y
        elif num == 2:
            Calculator.subtraction(x, y)
            x = x - y
        elif num == 4:
            Calculator.division(x, y)
            x = x / y
