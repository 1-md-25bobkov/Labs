
from PIL import Image, ImageOps, ImageFilter

def z1():
    img = Image.open("1.jpg")
    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)


def z2():
    img = Image.open("2.jpg")
    img2 = img.reduce(3)
    img3 = ImageOps.mirror(img2)
    img4 = ImageOps.flip(img2)
    img2.save("small.jpg")
    img3.save("mirror.jpg")
    img4.save("flip.jpg")


def z3():
    img = Image.open("1.jpg")
    img = img.filter(ImageFilter.FIND_EDGES)
    img2 = Image.open("2.jpg")
    img2 = img2.filter(ImageFilter.FIND_EDGES)
    img3 = Image.open("3.jpg")
    img3 = img3.filter(ImageFilter.FIND_EDGES)
    img4 = Image.open("4.jpg")
    img4 = img4.filter(ImageFilter.FIND_EDGES)
    img5 = Image.open("5.jpg")
    img5 = img5.filter(ImageFilter.FIND_EDGES)
    img.save("1filter.jpg")
    img2.save("2filter.jpg")
    img3.save("3filter.jpg")
    img4.save("4filter.jpg")
    img5.save("5filter.jpg")


def z4():
    img = Image.open("3.jpg")
    mark = Image.open("watermark.jpg")
    img.paste(mark)
    img.show()