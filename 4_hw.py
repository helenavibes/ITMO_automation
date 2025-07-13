class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Создание объектов и вывод результатов
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 2)

print("Прямоугольник 1:")
print(f"Площадь: {rect1.area()}, Периметр: {rect1.perimeter()}")
print("Прямоугольник 2:")
print(f"Площадь: {rect2.area()}, Периметр: {rect2.perimeter()}")
print("Прямоугольник 3:")
print(f"Площадь: {rect3.area()}, Периметр: {rect3.perimeter()}")


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} × {self.b} = {result}")

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} ÷ {self.b} = {result}")
        else:
            print("Ошибка: деление на ноль")

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")


# Пример использования
math_ops = Math(10, 5)
math_ops.addition()
math_ops.multiplication()
math_ops.division()
math_ops.subtraction()


class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


# Создание объектов для кнопок
buttons = [
    "Text Box", "Check Box", "Radio Button", "Web Tables",
    "Buttons", "Links", "Broken Links - Images",
    "Upload and Download", "Dynamic Properties"
]

button_objects = [SidebarButton(btn_text) for btn_text in buttons]

# Вывод текста и клик для каждой кнопки
for button in button_objects:
    print(f"Текст кнопки: {button.text}")
    print(button.click())
    print("-" * 30)