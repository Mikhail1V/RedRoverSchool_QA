class Animal:
    def __init__(self, name):
        self._name = name  # Приватный атрибут с уровнем доступа private

    def speak(self):
        return f"{self._name} говорит: 'Привет!'"

class Dog(Animal):
    def bark(self):
        return f"{self._name} лает: 'Гав-гав!'"

class Cat(Animal):
    def meow(self):
        return f"{self._name} мяукает: 'Мяу-мяу!'"

# Создаем экземпляры
my_dog = Dog("Барсик")
my_cat = Cat("Мурзик")

# Вызываем методы
print(my_dog.speak())  # Барсик говорит: 'Привет!'
print(my_dog.bark())   # Барсик лает: 'Гав-гав!'
print(my_cat.speak())  # Мурзик говорит: 'Привет!'
print(my_cat.meow())   # Мурзик мяукает: 'Мяу-мяу!'