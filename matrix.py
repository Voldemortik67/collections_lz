import random
import numpy as np  
# Вводим размеры
n = int(input("Введите N: "))
m = int(input("Введите M: "))
# Делаем первую матрицу
matr1 = []
for i in range(n):
    stroka = []
    for j in range(m):
        num = random.randint(1, 9)
        stroka.append(num)
    matr1.append(stroka)
print("Матрица 1:")
for r in matr1:
    print(r)
# Транспонируем с помощью numpy.transpose
matr2 = np.transpose(matr1)
print("Транспонированная матрица:")
for r in matr2:
    print(r)
# Проверка на квадратную матрицу
if n != m:
    print("Матрица не квадратная, определитель посчитать нельзя")
else:
    # Считаем определитель для ЛЮБОГО размера через np.linalg.det
    o1 = round(np.linalg.det(matr1))
    o2 = round(np.linalg.det(matr2))
    print("Определитель 1:", o1)
    print("Определитель 2:", o2)
    if o1 == o2:
        print("Они равны")
    else:
        print("Не равны")