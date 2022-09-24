# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]


import random

my_list = list(random.randint(1,10) for i in range(10))
print(my_list)

def unique(lst: list) -> list:
    return list(filter(lambda s: lst.count(s) == 1, lst))

print(unique(my_list))