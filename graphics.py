import matplotlib.pyplot as plt
import numpy as np
# Для генерации графиков используем numpy и matplotlib
# Делаем список иксов от 0.1 до 4 (для ln)
x = np.linspace(0.1, 4, 100)
x_points = np.array([1, 2, 3, 4])
# Создаем список из названий функций
# и складываем настройки в обычные кортежи
functions = ['x^2', 'e^x', 'ln(x)', 'x^3']
# Перебираем функции в цикле for
for name in functions:
    # Выбираем расчеты, цвета и маркеры
    if name == 'x^2':
        y = x ** 2
        y_pts = x_points ** 2
        col = 'blue'
        mrk = 'o'  # Круг
    elif name == 'e^x':
        y = np.exp(x)
        y_pts = np.exp(x_points)
        col = 'green'
        mrk = 'x'  # Крестик
    elif name == 'ln(x)':
        y = np.log(x)
        y_pts = np.log(x_points)
        col = 'red'
        mrk = 's'  # Квадрат
    else:
        y = x ** 3
        y_pts = x_points ** 3
        col = 'cyan'
        mrk = '^'  # Треугольник
    # Отрисовка линий и точек (plot и scatter)
    plt.plot(x, y, color=col, label=name)
    plt.scatter(x_points, y_pts, color=col, marker=mrk)
plt.title('Графики функций')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.legend()
# Показываем результат
plt.show()