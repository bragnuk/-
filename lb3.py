import numpy as np
import numdifftools as nd

# Означення функції
def f(x):
    return 3*x**4 + 4*x**3 - 12*x**2 - 5

# Похідна функції
def f_prime(x):
    return nd.Derivative(f)(x)

# Метод Ньютона
def newton_method(a, b, eps):
    if f(a) * nd.Derivative(f, n=2)(a) > 0:
        x = a
    else:
        x = b

    while True:
        x_next = x - f(x) / f_prime(x)
        if abs(x_next - x) < eps:
            break
        x = x_next

    return x

# Комбінований метод
def combined_method(a, b, eps):
    while abs(b - a) > eps:
        a_next = a - f(a) * (b - a) / (f(b) - f(a))
        b_next = b - f(b) / f_prime(b)
        a, b = a_next, b_next

    return (a + b) / 2

# Відокремлення коренів
def find_segments(f, start, end, step):
    segments = []
    x_prev = start
    while x_prev <= end:
        x_next = x_prev + step
        if f(x_prev) * f(x_next) < 0:
            segments.append((x_prev, x_next))
        x_prev = x_next
    return segments

# Основна частина
if __name__ == "__main__":
    segments = find_segments(f, -10, 10, 0.5)
    print("Знайдені сегменти:")
    for a, b in segments:
        print(f"[{a}, {b}]")

    eps = 1e-5
    for a, b in segments:
        print(f"\nРозв'язання на відрізку [{a}, {b}]")
        root_newton = newton_method(a, b, eps)
        print(f"Метод Ньютона: x = {root_newton:.5f}")
        root_combined = combined_method(a, b, eps)
        print(f"Комбінований метод: x = {root_combined:.5f}")
