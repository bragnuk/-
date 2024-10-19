import numpy as np

# Визначимо функцію f(x) та її похідну
def f(x):
    return 3*x**4 + 4*x**3 - 12*x**2 - 5

def f_derivative(x):
    return 12*x**3 + 12*x**2 - 24*x

# Функція для відокремлення коренів
def find_segments(f, a, b, step=0.1):
    segments = []
    x = a
    while x < b:
        if f(x) * f(x + step) < 0:
            segments.append((x, x + step))
        x += step
    return segments

# Метод половинного ділення
def bisection_method(f, a, b, eps):
    while abs(a - b) > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Метод хорд
def chord_method(f, a, b, eps):
    x0 = a if f(a) * f_derivative(a) > 0 else b
    x = b if x0 == a else a
    while abs(x - x0) > eps:
        x_new = x - (f(x) * (x - x0)) / (f(x) - f(x0))
        x0 = x
        x = x_new
    return x

# Основна програма
a = -2  # Ліва межа області пошуку коренів
b = 2   # Права межа області пошуку коренів
eps = 0.0001  # Задана точність

# Відокремлюємо корені
segments = find_segments(f, a, b)

# Уточнюємо корені методами
results = []
for seg in segments:
    root_bisection = bisection_method(f, seg[0], seg[1], eps)
    root_chord = chord_method(f, seg[0], seg[1], eps)
    results.append((seg, root_bisection, root_chord))

# Виведемо результати
for seg, root_bisection, root_chord in results:
    print(f"Segment: {seg}, Bisection Root: {root_bisection:.5f}, Chord Root: {root_chord:.5f}")
