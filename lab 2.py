a = int(input("Введите пароль"))
b = int(input("Подтвердите пароль"))
if a == b:
    print("Пароли совпадают")
else: print("Пароли не совпадают")

def z1():
    a = (input("Введите пароль"))
    if len(a) < 6:
        print("Слишком короткий пароль")
    elif a[0:7] == "qwerty":
        print("Ненадежный пароль")
    else: print("Пароль принят")

def z2():
    a = int(input("Введите номер места"))
    if a > 36 and a < 55:
        print ("Боковое место")
    elif a % 2 == 0:
       print ("Верхнее место")
    elif a % 2 != 0:
        print("Нижнее место")
    else: print ("Такого места в вагоне нет")

def z3():
    a = int(input("Введите год"))
    if a % 4 != 0:
        print("Год не високосный")
    elif a % 100 == 0:
        if a % 400 == 0:
            print("Год високосный")
        else:
            print("Год не високосный")
    else:
        print("Год високосный")

def z4():
    a = input("Введите цвет")
    b = input("Введите цвет")
    if a == "Красный" or a == "Желтый" or a == "Синий" and b == "Красный" or b == "Желтый" or b == "Синий":
        if a == "Красный" and b == "Желтый":
            print ("Оранжевый")
        elif a == "Красный" and b == "Синий":
            print("Фиолетовый")
        elif a == "Синий" and b == "Желтый":
            print ("Зеленый")
        elif b == "Красный" and a == "Желтый":
            print ("Оранжевый")
        elif b == "Красный" and a == "Синий":
            print("Фиолетовый")
        elif b == "Синий" and a == "Желтый":
            print ("Зеленый")
    else: print("Неправельно введены цвета")

z1()
z2()
z3()
z4()