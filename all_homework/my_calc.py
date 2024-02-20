# Определяем функцию для сложения двух чисел
def add(x, y):
    return x + y

# Определяем функцию для вычитания двух чисел
def subtract(x, y):
    return x - y

# Определяем функцию для умножения двух чисел
def multiply(x, y):
    return x * y

# Определяем функцию для деления двух чисел
def divide(x, y):
    # Проверяем, что делитель не равен нулю
    if y != 0:
        return x / y
    else:
        # Выводим сообщение об ошибке
        print("Деление на ноль невозможно")