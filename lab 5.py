def z1():
    numbers = [1,3,5,7,9]
    a = int(input("Угадайте число"))
    if a in numbers:
        print (numbers,"Поздравляю, Вы угадали число!")
    else:
        print(numbers, "Нет такого числа!")

def z2():
    numbers = [1,1,5,7,9]
    for i in range(len(numbers)):
        if numbers[i] in numbers[i+1:5]:
            print(numbers[i])

def z3():
    days = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    a = int(input("Сколько дней вы хотите отдыхать ? (1-7)"))
    reverse = days[::-1]
    print(f"Ваши выходные дни {reverse[0:a]}")
    print(f"Ваши рабочие дни {days[0:len(days)-a]}")

def z4():
    group1 = ["Бадминов","Давлетов","Насонов","Лащев","Бобков","Хавалиц","Чедырян","Выдровский","Костюков","Сергеев"]
    group2 = ["Смирнов","Иванов","Кузнецов","Соколов","Попов","Попов","Козлов","Новиков","Морозов","Петров"]
    team = (group1[0:5] + group2[0:5])
    team.sort()
    print(f"изначальные списки студентов")
    print(group1,group2)
    print("Спортивная команда")
    print(f"{team} {len(team)}")
    if "Иванов" in team:
        print("В спортивную команду входит Иванов")

