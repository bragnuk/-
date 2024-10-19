import numpy as np
import matplotlib.pyplot as plt

# Функція з варіанту
def func(x):
    return np.cos(3 * x - 1) + x

# Дані
x = np.array([i * 0.1 for i in range(1, 11)])
y = np.array([func(xi) for xi in x])

# Лінійна регресія
coefficients_line = np.polyfit(x, y, 1)  # 1 - ступінь поліному для лінії
a_line, b_line = coefficients_line
print(f"Лінійна регресія: y = {a_line:.2f}x + {b_line:.2f}")

# Поліном другого порядку
coefficients_poly = np.polyfit(x, y, 2)  # 2 - ступінь поліному
a_poly, b_poly, c_poly = coefficients_poly
print(f"Поліном другого порядку: y = {a_poly:.2f}x^2 + {b_poly:.2f}x + {c_poly:.2f}")

# Графік
plt.scatter(x, y, color='red', label='Дані')
x_line = np.linspace(min(x), max(x), 100)
plt.plot(x_line, np.polyval(coefficients_line, x_line), label='Лінійна регресія')
plt.plot(x_line, np.polyval(coefficients_poly, x_line), label='Поліном другого порядку')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('МНК апроксимація')
plt.show()
