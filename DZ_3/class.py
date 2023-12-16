# Создаём класс `Car`
class Car:
    # Добавляем атрибуты `make` (марка автомобиля), `model` (модель автомобиля) и `year` (год выпуска).
    def __init__(self, make=None, model=None, year=None):
        self.make = make
        self.model = model
        self.year = year

        # Выводим результат
        self.display_info()

    # Создаём метод `display_info()`, который выводит информацию о машине (марка, модель и год).
    def display_info(self):
        print("Maker: " + self.make, "Model: " + self.model, "Year: " + self.year, sep=' | ')


# Обращаемся к классу записываем атрибуты и через точку обращаемся к методу вывода
Car(make='LADA', model='Priora', year='2018')
# Тут пользователь сам вводит марку, модель, год выпуска
Car(make=input('Введите марку автомобиля: '), model=input("Введите модель машины: "),
    year=input("Введите год выпуска автомобиля: "))
