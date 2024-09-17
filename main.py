# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые
# наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает
# список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о
# животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о
# зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между
# запусками программы.


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f'{self.name} возраст {self.age}: Каркает')


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f'{self.name} возраст {self.age} шерсть {self.fur_color}: Рычит')


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f'{self.name} возраст {self.age}: Шипит')

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

animal_list = [Bird('Ворон', 2), Mammal('Волк', 3, 'Серая'), Reptile('Ящерица', 1)]
animal_sound(animal_list)

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о
# животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)

    def animals_info(self):
        for animal in self.animals:
            print(animal.name)

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

my_zoo = Zoo()
my_zoo.add_animal(Bird("Ворон", 3))
my_zoo.add_staff(ZooKeeper("Вася"))
my_zoo.animals_info()

# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о
# зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между
# запусками программы.

import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)

def load_zoo(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


save_zoo(my_zoo, 'my_zoo.pkl')
loaded_zoo = load_zoo('my_zoo.pkl')















# class Author():
#     def __init__(self, name, nationality):
#         self.name = name
#         self.nationality = nationality
#
#
#
# class Book():
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def get_info(self):
#         print(f'{self.title} - {self.author.name}')
#
#
# author = Author('Лев', 'рус')
# book = Book('война и мир', author)
#
# book.get_info()























# import math
#
# class Shape():
#     def __init__(self):
#     def area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self, a):
#         self.a = a
#
#     def area(self):
#         return self.a ** 2
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return math.pi * self.r ** 2
#
# def print_area(shape):
#     print(f'Площадь - {shape.area}')
#
# circle = Circle(5)
# print_area(circle)




















# class Animal():
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print("мяу")
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print("гав")
#
#
# class Cow(Animal):
#     def make_sound(self):
#         print("Му")
#
#
# cat = Cat()
# dog = Dog()
# cow = Cow()
#
# animal_list = [cat, dog, cow]
#
# for animal in animal_list:
#     animal.make_sound()





