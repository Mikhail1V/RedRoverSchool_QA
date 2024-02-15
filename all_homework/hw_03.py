# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
for x in my_list[2]:
    print(x, end=' ')

# Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
sum_of_numbers = sum(x for x in list_1 if isinstance(x, int))
print(sum_of_numbers)

# Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

list_2 = ['cat', 'dog', 'horse', 'cow']
tuple_2 = tuple(list_2)
print(tuple_2)

# Напишите программу, которая определяет, какая семья больше.
#  1) Программа имеет два input() - например, family_1, family_2.
#  2) Членов семьи нужно перечислить через запятую.
#  Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input('Введите имена членов семьи family_1 через запятую: ')
family_2 = input('Введите имена членов семьи family_2 через запятую: ')

family_1_list = family_1.split(',')
family_2_list = family_2.split(',')

family_1_size = len(family_1_list)
family_2_size = len(family_2_list)

if family_1_size > family_2_size:
    print('Семья family_1 больше')
elif family_1_size < family_2_size:
    print('Семья family_2 больше')
else:
    print('Equal')

# Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {
    "title": "Начало",
    "director": "Кристофер Нолан",
    "year": 2010,
    "budget": 160000000,
    "main_actor": "Леонардо Ди Каприо",
    "slogan": "Ваш разум - сцена преступления"
}

print(film.keys())
print(film.values())
print(film.items())

# Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
sum_of_values = sum(my_dictionary.values())
print(sum_of_values)

# Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

my_list = [1, 2, 3, 4, 5, 3, 2, 1]
my_set = set(my_list)
my_list = list(my_set)
print(my_list)

# Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#  - найдите значения, которые встречаются в обоих множествах
#  - найдите значения, которые не встречаются в обоих множествах
#  - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

common_values = set1 & set2
different_values = set1 ^ set2
set1_is_subset_of_set2 = set1.issubset(set2)
set2_is_subset_of_set1 = set2.issubset(set1)

print("Значения, которые встречаются в обоих множествах:", common_values)
print("Значения, которые не встречаются в обоих множествах:", different_values)
print("Является ли set1 подмножеством set2?", set1_is_subset_of_set2)
print("Является ли set2 подмножеством set1?", set2_is_subset_of_set1)