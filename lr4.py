import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Метод 1: Использование random.randint()
def my_rand1(n, low=3, high=9):
    return [random.randint(low, high) for _ in range(n)]

# Метод 2: Использование random.sample()
def my_rand2(n, start=1, end=50):
    if n > (end - start):
        n = end - start  # Корректируем n, чтобы избежать ошибки
    return random.sample(range(start, end), n)

# Метод 3: Использование списочного понимания + randrange()
def my_rand3(n, start=1, end=50):
    return [random.randrange(start, end) for _ in range(n)]

# Метод 4: Использование цикла + randint()
def my_rand4(n, low=0, high=51):
    rand_list = []
    for _ in range(n):
        rand_list.append(random.randint(low, high))
    return rand_list

# Метод 5: Генерация списка случайных целых чисел с помощью numpy.random.randint
def my_rand5(n, low=3, high=8):
    return np.random.randint(low, high, size=n).tolist()

# Метод 6: Генерация списка случайных плавающих значений с помощью numpy.random.random
def my_rand6(n):
    return np.random.random(n).tolist()

# Функция для выполнения бросков кубика
def kubik(n: int) -> list:
    return [random.randint(1, 6) for _ in range(n)]

# Функция для подсчета вероятностей
def count_rate(kub_data: list) -> dict:
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            kub_rate[i] += 1
        else:
            kub_rate[i] = 1
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

# Параметры для бросков
num_rolls = [100, 1000, 10000, 1000000]
methods = [my_rand1, my_rand2, my_rand3, my_rand4, my_rand5, my_rand6]

# Создание гистограмм
for method_index, method in enumerate(methods):
    plt.figure(figsize=(15, 10))  # создаем новое окно для каждой группы методов

    for i, n in enumerate(num_rolls):
        rolls = kubik(n)
        counts = count_rate(rolls)

        # Печатаем результаты в командной строке
        print(f'Метод {method_index + 1}, Броски: {n}, Частотность: {counts}')

        # Создание графика
        plt.subplot(2, 2, i + 1)
        plt.bar(counts.keys(), counts.values(), color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
        plt.title(f'Метод {method_index + 1}, Броски: {n}')
        plt.xlabel('Грань кубика')
        plt.ylabel('Количество выпадений')

    plt.tight_layout()
    plt.show()  # Показываем графики для данного метода
