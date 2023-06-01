import os
from PIL import ImageFilter, Image

def z1():
    os.chdir("lab 9")
    directory = os.getcwd() #копируем путь
    if not os.path.isdir("new"): #если папки нет он её создаёт
        os.mkdir("new")
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.jpg'):
            img = Image.open(f)
            newimg = img.filter(ImageFilter.FIND_EDGES)
            os.chdir("new")
            newimg.save("new_" + filename)

def z3():
    import csv
    otvet='Нужно купить:\n'
    summa=0
    with open('data.csv') as per:
        reader = csv.reader(per)
        for row in reader:
            otvet = otvet+row[0]+' - '+row[1]+ ' шт. за '+ row[2] + ' руб.\n'
            summa+=int(row[2])
    print(otvet+'Итоговая сумма = ', summa, ' руб' )

z1()