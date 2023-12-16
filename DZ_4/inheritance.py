# Создаём класс "Маму" для всех остальных, называем его 'Animal', и создаём переменные
class Animal:
    def __init__(self, species=None, name=None):
        self.name = name
        self.species = species

    # Вывод переменных
    def make_sound(self):
        print(f'{self.species} {self.name} издаёт такой звук:')


# Создаём подклассы наследующие "Маму"-'Animal'
class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species, name)
        self.make_sound()

    # Вывод проги
    def make_sound(self):
        print(f'{self.species} {self.name} издаёт такой звук: << Гав >>')


# Создаём подклассы наследующие "Маму"-'Animal'
class Cat(Animal):

    def __init__(self, species, name):
        super().__init__(species, name)
        self.make_sound()

    # Вывод проги
    def make_sound(self):
        print(f'{self.species} {self.name} издаёт такой звук: << Мяу >>')


# Ну тут уже всё понятно, выводим всё и играемся с нашими созданными классами
animal = Animal(input("Введите животного <Собака / Кошка> ").lower(), input("Введите имя животного: "))
animal_name = animal.name

# А тут условие, если определённое слово то работает определённый подкласс наследник
if animal.species == 'кошка' or animal.species == 'кот':
    Cat('Кот(шка)', animal_name)
else:
    Dog('Собака', animal_name)
