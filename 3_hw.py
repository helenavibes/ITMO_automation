# Задача 2: Наибольшее из двух чисел
def task_2(num1: float, num2: float) -> None:
    print(max(num1, num2))


# Задача 3: Проверка разницы чисел
def task_3(num1: float, num2: float) -> None:
    print("yes" if abs(num1 - num2) == 135 else "no")


# Задача 4: Определение сезона по месяцу
def task_4(month: int) -> None:
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Неверный номер месяца")


# Задача 5: Проверка трех чисел
def task_5(a: float, b: float, c: float) -> None:
    print("yes" if a > 10 and b > 10 and c > 10 else "no")


# Задача 6: Количество положительных чисел в списке
def task_6(numbers: list) -> None:
    count = sum(1 for num in numbers if num > 0)
    print(count)


# Задача 7: Расчет количества дней
def task_7(years: int, months: int) -> None:
    total_days = (years * 12 + months) * 29
    print(total_days)


# Вызовы функций для демонстрации работы
if __name__ == "__main__":
    print("\nЗадача 2:")
    task_2(5.7, 3.2)

    print("\nЗадача 3:")
    task_3(150, 15)

    print("\nЗадача 4:")
    task_4(7)

    print("\nЗадача 5:")
    task_5(12, 15, 9)

    print("\nЗадача 6:")
    task_6([5, -2, 10, -8, 3])

    print("\nЗадача 7:")
    task_7(2, 5)