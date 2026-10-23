import random
# вводим размеры
n = int(input("Введите N: "))
m = int(input("Введите M: "))
# делаем первую матрицу
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
# делаем транспонированную матрицу
matr2 = []
for i in range(m):
    stroka = []
    for j in range(n):
        stroka.append(matr1[j][i])
    matr2.append(stroka)
print("Транспонированная матрица:")
for r in matr2:
    print(r)
# проверка на квадратную матрицу
if n != m:
    print("Матрица не квадратная, определитель посчитать нельзя")
else:
    # если размер 2х2
    if n == 2:
        o1 = matr1 * matr1 - matr1 * matr1
        o2 = matr2 * matr2 - matr2 * matr2
        print("Определитель 1:", o1)
        print("Определитель 2:", o2)
        
        if o1 == o2:
            print("Они равны")
        else:
            print("Не равны")   
        # если размер 3х3 (считаем по формуле Саррюса)
    elif n == 3:
        # для первой матрицы
        plus1 = matr1[0][0] * matr1[1][1] * matr1[2][2] + matr1[0][1] * matr1[1][2] * matr1[2][0] + matr1[0][2] * matr1[1][0] * matr1[2][1]
        minus1 = matr1[0][2] * matr1[1][1] * matr1[2][0] + matr1[0][0] * matr1[1][2] * matr1[2][1] + matr1[0][1] * matr1[1][0] * matr1[2][2]
        o1 = plus1 - minus1
        
        # для второй матрицы
        plus2 = matr2[0][0] * matr2[1][1] * matr2[2][2] + matr2[0][1] * matr2[1][2] * matr2[2][0] + matr2[0][2] * matr2[1][0] * matr2[2][1]
        minus2 = matr2[0][2] * matr2[1][1] * matr2[2][0] + matr2[0][0] * matr2[1][2] * matr2[2][1] + matr2[0][1] * matr2[1][0] * matr2[2][2]
        o2 = plus2 - minus2
        
        print("Определитель 1:", o1)
        print("Определитель 2:", o2)
        
        if o1 == o2:
            print("Они равны")
        else:
            print("Не равны")
    else:
        print("Ошибка, матрица должна быть 2х2 или 3х3")