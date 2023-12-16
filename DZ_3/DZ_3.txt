# Создаём класс `Car`
class Car:
    # Добавляем атрибуты `make` (марка автомобиля), `model` (модель автомобиля) и `year` (год выпуска).
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Создаём метод `display_info()`, который выводит информацию о машине (марка, модель и год).
    def display_info(self):
        print("Maker: " + self.make, "Model: " + self.model, "Year: " + self.year, sep=' | ')


# Обращаемся к классу записываем атрибуты и через точку обращаемся к методу вывода
Car(make='LADA', model='Priora', year='2018').display_info()
# Тут пользователь сам вводит марку, модель, год выпуска
Car(make=input('Введите марку автомобиля: '), model=input("Введите модель машины: "), year=input("Введите год выпуска автомобиля: ")).display_info()


