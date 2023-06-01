
import random
n = int(input("Введите кол-во слов "))
res = " "
while n > 0:
    word = input("Введите слово ")
    res +=  word + " "
    n = n-1
print (res)

def z2():
    a = input ("Введите слово ")
    res = a
    while a != "stop":
        a = input("Введите слово ")
        res += a + " "
    print(res)

def z3():
    a = input("Введите слово ")
    if "ф" in a or "Ф" in a:
        print ("Ого! Это редкое слово")
    else:
        print("Эх, это не очень редкое слово...")

def z4():
    miss = 3
    score = 0
    while miss > 0:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(input (str(a) + " + " + str(b) + " = ?"))
        if answer == (a + b):
            score += 1
            print("Ответ правильный")
        else:
            miss -= 1
            print("Ответ Неправильный")
    print(f"Игра окончена. Правильных ответов {score}")

z2()
z3()
z4()
