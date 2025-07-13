# Файл: car.py
class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.type = car_type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведен")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Установлен год выпуска: {year}")

    def set_type(self, car_type):
        self.type = car_type
        print(f"Установлен тип автомобиля: {car_type}")

    def set_color(self, color):
        self.color = color
        print(f"Установлен цвет: {color}")