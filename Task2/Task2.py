# Задача: предложить улучшения кода для уже решённых задач с помощью использования **лямбд,
# filter, map, zip, enumerate, list comprehension.

# 1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# Using list comprehension
list1 = [1, 2, 3, 5, 1, 5, 3, 10]
list2 = [el for el in list1 if list1.count(el) == 1]
print(f'Unique elements are: {list2}.')
print()



# 2. Найти сумму чисел списка стоящих на нечетной позиции
ls1 = [1, 2, 3, 5, 1, 5, 3, 10]
summa = sum([ls1[i] for i in range(len(ls1)) if i % 2 == 1])
print(f'Suuma of elements on even positions {summa}.')
print()

# 3. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Please input a number. '))
result = {el[0] : el[1] for el in list(enumerate([(3*i + 1) for i in range(1, n + 1)], 1))}
print(f'Final dictionary: {result}')