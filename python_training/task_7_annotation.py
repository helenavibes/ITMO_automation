a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s
print(indent('69', 69))

def min_list(a: list, b: list) -> int:
    return max(len(a), len(b))

def string_length(s: str = '') -> int:
    return len(s)

def append_list(my_list:list) -> list:
    my_list.append('test')
    return my_list
print(append_list(['один', 2, 3]))

def sum_list(my_list:list) -> list:
    result = 0
    for elem in my_list:
        result = result + elem
    return result