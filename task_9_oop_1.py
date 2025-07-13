from task_9_checks import Checks

class ButtonOne(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class ButtonTwo(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Title(Checks):
    def __init__(self, loc):
        super().__init__(loc)

# Создание объектов и вызов метода
elements = [
    ButtonOne("Локатор_1"),
    ButtonTwo("Локатор_2"),
    Input("Локатор_3"),
    Title("Локатор_4")
]

for element in elements:
    print(element.check_text())