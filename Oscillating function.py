import numpy as np
import matplotlib.pyplot as plt

def f(x):
# Определение осциллирующей функции
    return np.sin(x*100)/(1+x)

def trapezoidal_rule(f, a, b, n):
# Функция для вычисления интеграла методом трапеций
    h = (b - a) / n # Размер шага
    result = 0.5 * (f(a) + f(b)) # Первое слагаемое 
    for i in range(1, n):
        result += f(a + i * h) # Сумма внутренних слагаемых
    return result * h # Умножаем на шаг

def integrate(f, a, b, e):
# Функция для вычисления интеграла с заданной точностью
    n = 1 # Начальное количество интервалов
    integral_old = trapezoidal_rule(f, a, b, n)
    while True:
        n *= 2 # Удваиваем количество интервалов на каждой итерации
        integral_new = trapezoidal_rule(f, a, b, n)
        if abs(integral_new - integral_old) < e:
# Если достигнута заданная точность, возвращаем результат
            return integral_new
        else:
# В противном случае обновляем значение интеграла
            integral_old = integral_new
# Пределы игнетграла и заданная точность

a = 0
b = 1
e = 10 ** -6

result = integrate(f, a, b, e)
print(f'Значение интеграла = {result}')