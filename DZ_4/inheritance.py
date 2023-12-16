class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f'Животное {self.name} издаёт такой звук: {self.species}')

