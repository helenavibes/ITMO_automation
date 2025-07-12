# Задача 1
def task_1() -> None:
    var_int: int = 42
    var_float: float = 3.14
    var_str: str = "Hello, Python!"
    var_list: list = [1, 2, 3, 5, 8]
    var_bool: bool = True

    print(type(var_int))
    print(type(var_float))
    print(type(var_str))
    print(type(var_list))
    print(type(var_bool))

# Задача 2
def task_2() -> None:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    print(a[0], a[1], a[2])  # Первые три значения списка
    # Последовательность называется "Числа Фибоначчи"

# Задача 3
def task_3(num: float) -> float:
    return num ** 2

# Вызовы функций
task_1()
task_2()
print(task_3(5))  # Пример с числом 5