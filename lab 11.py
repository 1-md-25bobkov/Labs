from random import randint
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана - {self.restaurant_name}")
        print(f"Тип кухни - {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт")

def z1():
    new_restaurant = Restaurant("Japan", "Японская")
    print(new_restaurant.restaurant_name)
    print(new_restaurant.cuisine_type)
    print()

    new_restaurant.describe_restaurant()
    new_restaurant.open_restaurant()

# Задание 2
def z2():
    restaurant1 = Restaurant("KFC", "Фастфуд")
    restaurant2 = Restaurant("Теремок", "Русская")
    restaurant3 = Restaurant("Бухара", "Восточная")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z3():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = randint(1,5)

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name}")
            print(f"Тип кухни - {self.cuisine_type}")
            print(f"Рейтинг ресторана - {self.rating}")

        def new_rating(self):
            new_rating = int(input("Введите новый рейтинг ресторана(от 1 до 5): "))
            self.rating = new_rating
            print(f"Название ресторана - {self.restaurant_name}")
            print(f"Тип кухни - {self.cuisine_type}")
            print(f"Рейтинг ресторана - {self.rating}")

    new_restaurant = Restaurant("Japan", "Японская")
    new_restaurant.describe_restaurant()
    new_restaurant.new_rating()


