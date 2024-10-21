import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Метод 1: Использование random.randint()
def my_rand1(n, low=3, high=9):
    return [random.randint(low, high) for _ in range(n)]

# Метод 2: Использование random.sample()
def my_rand2(n, start=1, end=50):
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
    """Генерирует список из n случайных целых чисел в заданном диапазоне [low, high)."""
    return np.random.randint(low, high, size=n).tolist()

# Метод 6: Генерация списка случайных плавающих значений с помощью numpy.random.random
def my_rand6(n):
    """Генерирует список из n случайных плавающих чисел в диапазоне [0.0, 1.0)."""
    return np.random.random(n).tolist()  # Преобразование в список

# Примеры использования функций
print("Метод 1:", my_rand1(10))
print("Метод 2:", my_rand2(7))
print("Метод 3:", my_rand3(7))
print("Метод 4:", my_rand4(10))
print("Метод 5 (numpy):", my_rand5(10))
print("Метод 6 (numpy float):", my_rand6(4))




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
    # Добавляем отсутствующие значения
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

# Параметры для бросков
num_rolls = [100, 1000, 10000, 1000000]
results = {}

# Выполнение бросков и сбор данных
for n in num_rolls:
    rolls = kubik(n)
    counts = count_rate(rolls)
    results[n] = counts

# Создание DataFrame для удобного отображения
df_results = pd.DataFrame(results).fillna(0).astype(int).T
df_results.columns = ['1', '2', '3', '4', '5', '6']
print(df_results)  # Выводим DataFrame для проверки

# Построение гистограмм
plt.figure(figsize=(15, 10))
for i, n in enumerate(num_rolls):
    plt.subplot(2, 2, i + 1)
    df_results.loc[n].plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
    plt.title(f'Количество бросков: {n}')
    plt.xlabel('Грань кубика')
    plt.ylabel('Количество выпадений')

plt.tight_layout()
plt.savefig('cube_rolls_histograms.png')  # Сохраняем график
plt.show()
