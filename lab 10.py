import json

def z1():
    with open("products.json") as file:
         data = json.load(file)
         print(data["products"])
         for product in data["products"]:
             print(f"Название: {product['name']} \nЦена: {product['price']} \nВес: {product['weight']} \n{'В наличии' if product['available'] else 'Не в наличии'}\n")
    answer = input("Хотите ввести новые данные? ")
    while answer == "Да":
        data["products"].append({
        "name": input("Введите название товара: "),
        "price": int(input("Введите цену товара: ")),
        "available": "true" if input("Введите, в наличии ли товар: ") == "Да" else "false",
        "weight": int(input("Введите вес товара: "))
        })
        with open("products.json", "w") as outfile:
            json.dump(data, outfile, ensure_ascii=False)
        answer = input("Данные записаны, хотите ещё что-нибудь добавить? ")

data = {}
with open("en-ru.txt", "r") as file:
    for line in file:
        en_w = line.split(" - ")[0].strip()
        ru_w = line.split(" - ")[1].strip().split(", ")
        for i in ru_w:
            i = i.strip()
            if i in data.keys():
                data[i] = data[i] + "," + en_w
            else:
                data[i] = en_w
with open("ru-en.txt", "w") as file:
    for i in sorted(data.keys()):
        file.writelines(f"{i} - {data[i]}\n")