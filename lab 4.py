def k3(a):
    if a % 3 == 0:
        return print(f"Число {a} делится на 3 без остатка")
    else:
        return print(f"Число {a} НЕ делится на 3 без остатка")

#k3(12)

def del100 (a):
    try:
        b = 100 / a
    except ZeroDivisionError:
        print("На ноль делить НЕЛЬЗЯ!")
    except ValueError:
        print("Это не число")
    else:
        return print(f"при делении 100 на {a} получится {100 / a}")

#del100(123)

def magicdate(day, month, year):
    if day * month == year % 100:
        return print("Магическая дата")
    else:
        return print ("Это не магическая дата")

#magicdate(2,20,1950)

def ticket(ticket):
    a = list(str(ticket))
    a1 = a[:len(a)//2]
    a2 = a[len(a)//2:]
    b = 0
    b1 = 0
    for item in a1:
        b += int(item)
    for item in a2:
        b1 += int(item)
    if b == b1:
        print(f"Это счастливый билет {ticket}")
    else:
        print (f"это не счастливый билет {ticket}")

#ticket(123456)


