# 1) Напишите и запустите программу. которая выводит строку  "Hello world!"
print("Hello world!")

# 2) Напишите программу, которая на входе получает имя пользователя,
# сохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"

user_name = input()
print(f"Hello {user_name}!")

# 3) Напишите программу, которая на входе получает 2 числа,
# производит с ними арифметическую операцию(на ваше усмотрение),
# и выводит “Результат = {результат}”.

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

sum = num1 + num2
print("Результат =", sum)

# 4) Напишите программу, чтобы вывести:
#
# *********
# *       *
# *       *
# *********

print('*' * 9)
print('*' + ' ' * 7 + '*')
print('*' + ' ' * 7 + '*')
print('*' * 9)

# 5) Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
#
# Пример:
#
# Input: 3498
#
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8

# Вводим четырёхзначное число
number = input("Введите четырёхзначное число: ")

# Проверяем, что число действительно четырёхзначное
if len(number) != 4:
    print("Неверный ввод. Попробуйте ещё раз.")
else:
    # Преобразуем строку в целое число
    number = int(number)

    # Находим тысячи, сотни, десятки и единицы
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    # Выводим результат
    print("Тысячи -", thousands)
    print("Сотни -", hundreds)
    print("Десятки -", tens)
    print("Единицы -", ones)

# 6) 1.4. **
# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы  (a+b)2 и сумму квадратов a2+b2 этих чисел.
#
# Пример:
#
# Input:
# 3
# 2
#
#
# Output:
# Квадрат суммы 3 и 2 равен 25
# Сумма квадратов 3 и 2 равна 13

# Считываем два целых числа a и b
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Вычисляем квадрат суммы (a+b)^2 и сумму квадратов a^2+b^2
square_of_sum = (a + b) ** 2
sum_of_squares = a ** 2 + b ** 2

# Выводим результат на экран
print("Квадрат суммы", a, "и", b, "равен", square_of_sum)
print("Сумма квадратов", a, "и", b, "равна", sum_of_squares)