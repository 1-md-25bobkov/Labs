from PIL import Image, ImageDraw, ImageFont


def z1():
    img = Image.open("23f.jpg")
    imgcrop = img.crop((300,600,1100,1400))
    imgcrop.show()


def z2():
    holidays = {"23 Февараля" : "23f.jpg", "8 Марта" : "8m.jpg", "Новый год" : "ny.jpg"}
    a = input(" Введите праздник")
    for key in holidays:
        if key == a:
            img = Image.open(holidays[key])
            img.show()

def z3():
    name = input("Введите имя")
    img = Image.open("1.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial_bold.ttf", 25)
    draw.text(
        (img.width // 2 - 100, 15),
        name + ", поздравляю!",
        font=font,
        fill=('#FAACAC'))
    img.show()
    img.save("открытка.png")
