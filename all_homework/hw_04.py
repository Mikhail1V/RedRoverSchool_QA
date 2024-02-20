# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
    # Периметр квадрата равен четырехкратному произведению стороны на число пи
    perimeter = 4 * side
    # Площадь квадрата равна квадрату стороны
    area = side ** 2
    # Диагональ квадрата равна произведению стороны на корень из двух
    diagonal = side * (2 ** 0.5)
    # Возвращаем кортеж из трех значений
    return (perimeter, area, diagonal)


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def print_kwargs(**kwargs):
    # Проходим по всем именованным аргументам
    for key, value in kwargs.items():
        # Выводим аргумент и его значение в формате key: value
        print(f"{key}: {value}")



# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# Создаем список my_list
my_list = [20, -3, 15, 2, -1, -21]
# Используем лямбда-выражение для фильтрации положительных чисел
new_list = list(filter(lambda x: x > 0, my_list))
# Выводим новый список
print(new_list)


# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)

# Создаем список my_list
my_list = [20, -3, 15, 2, -1, -21]
# Используем лямбда-выражение для перемножения значений в списке
result = 1
for x in my_list:
    result = result * x
# Выводим результат
print(result)


# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time

# Определяем декоратор
def timer(func):
    # Определяем вложенную функцию, которая будет обернута вокруг декорируемой функции
    def wrapper(*args, **kwargs):
        # Засекаем время начала выполнения функции
        start = time.time()
        # Вызываем декорируемую функцию и сохраняем ее результат
        result = func(*args, **kwargs)
        # Засекаем время окончания выполнения функции
        end = time.time()
        # Вычисляем время работы функции в секундах
        duration = end - start
        # Выводим время работы функции
        print(f"Функция {func.__name__} работала {duration} секунд")
        # Возвращаем результат декорируемой функции
        return result
    # Возвращаем вложенную функцию
    return wrapper

# Декорируем функцию, которая считает сумму квадратов чисел от 1 до n
@timer
def sum_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# Вызываем декорированную функцию
sum_squares(100000)





# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.




#      Примените эти функции в качестве методов в другом файле.