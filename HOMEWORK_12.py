# =============================
# Домашняя работа: ООП на Python
# TeachMeSkills.by
# =============================
from dataclasses import dataclass, field


# Задание 1. Класс «Товар» и «Склад».
#
# Класс «Товар» содержит закрытые поля:
# - название товара
# - название магазина
# - стоимость в рублях
#
# Класс «Склад» содержит массив товаров.
#
# Обеспечить возможности:
# ✅ Вывод информации о товаре со склада по индексу
# ✅ Вывод информации о товаре со склада по имени
# ✅ Сортировка товаров по названию, по магазину и по цене
# ✅ Перегрузка сложения товаров по цене


# === TODO: реализовать класс Product ===


class Product:
    def __init__(self, name, shop, price):
        # TODO: сохранить значения в закрытые поля
        self.__name = name
        self.__shop = shop
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def shop(self):
        return self.__shop

    @property
    def price(self):
        return self.__price

    def __str__(self):
        # TODO: вернуть читаемую строку с данными товара
        return f"{self.__name} из {self.__shop} стоит {self.__price} руб."

    # TODO: перегрузить оператор сложения (__add__), чтобы возвращалась сумма цен двух товаров
    def __add__(self, other):
        price_sum = self.__price + other.__price
        return price_sum


# === TODO: реализовать класс Warehouse ===

class Warehouse:
    def __init__(self):
        """Создаём список товаров"""
        self.__product_list = list()

    def add_product(self, product):
        """Добавляет товар на склад"""
        self.__product_list.append(product)
        return f"Товар {product} добавлен!"

    def get_by_index(self, index):
        """Возвращает информацию о товаре по индексу"""
        return self.__product_list[index]

    def get_by_name(self, name):
        """ Выводит информации о товаре со склада по имени"""
        for prod in self.__product_list:
            if name == prod.name:
                return prod
        return None

    def get_all_products(self):  # Добавим метод для проверки сортировки
        """Проверка сортировки"""
        return self.__product_list

    def sort_name(self):
        """Сортировка по имени товара"""
        self.__product_list.sort(key=lambda p: p.name)

    def sort_shop(self):
        """Сортировка по имени магазина"""
        self.__product_list.sort(key=lambda p: p.shop)

    def sort_price(self):
        """Сортировка по имени ценам"""
        self.__product_list.sort(key=lambda p: p.price)


# === Тесты для задачи 1 ===
print("=== Задача 1: Склад ===")
w = Warehouse()
p1 = Product("Молоко", "Пятерочка", 70)
p2 = Product("Хлеб", "Магнит", 40)
p3 = Product("Сыр", "Пятерочка", 300)

w.add_product(p1)
w.add_product(p2)
w.add_product(p3)
print(w.get_by_index(1))
print(w.get_by_name("Сыр"))

# TODO: протестировать сортировку и сложение p1 + p2
print("Тестируем сложение p1 + p2 =", p1 + p2)
# Тестируем сортировку по магазину
print("\nДо сортировки:")
for product in w.get_all_products():
    print(product)

w.sort_shop()
print("\nПосле сортировки по магазину:")
for product in w.get_all_products():
    print(product)


# =============================
# Задание 2. Класс «ПчёлоСлон».
#
# Инициализируется двумя числами:
# - часть пчелы
# - часть слона
#
# Методы:
# ✅ Fly() – True, если часть пчелы >= части слона
# ✅ Trumpet() – "tu-tu-doo-doo", если часть слона >= пчелы, иначе "wzzzz"
# ✅ Eat(meal, value) – meal только "nectar" или "grass".
#   - если nectar: у слона уменьшается, у пчелы увеличивается
#   - если grass: наоборот
#   - нельзя выйти за пределы 0–100


# === TODO: реализовать класс BeeElephant ===
class BeeElephant:

    def __init__(self, bee_part, elephant_part):
        """Сохранить bee_part и elephant_part"""
        self.__bee_part = bee_part
        self.__elephant_part = elephant_part

    def __str__(self):
        return f"Значение пчелы - {self.__bee_part}. Значение слона - {self.__elephant_part}"

    def fly(self):
        """ Реализовывает логику Fly"""
        return self.__bee_part >= self.__elephant_part

    def trumpet(self):
        """Реализовывает логику Trumpet"""
        if self.__bee_part >= self.__elephant_part:
            return "wzzzz"
        return "tu-tu-doo-doo"

    def eat(self, meal, value):
        """Реализовывает логику Eat"""
        if value < 0:
            raise ValueError(f"передаваемое число не может быть меньше 0")

        if meal == "nectar":
            self.__bee_part = min(self.__bee_part + value, 100)  # Если > 100, то присвоит 100
            self.__elephant_part = max(self.__elephant_part - value, 0)  # Если < 0, то присвоит 0
        elif meal == "grass":
            self.__bee_part = max(self.__bee_part - value, 0)  # Если < 0, то присвоит 0
            self.__elephant_part = min(self.__elephant_part + value, 100)  # Если > 100, то присвоит 100
        else:
            raise ValueError("meal должно быть только \"nectar\" или \"grass\"")


# === Тесты для задачи 2 ===


print("\n=== Задача 2: ПчёлоСлон ===")
be = BeeElephant(30, 70)
print(be.fly())  # False
print(be.trumpet())  # tu-tu-doo-doo
be.eat("nectar", 20)  # должно изменить пропорции
print(be.fly())  # возможно True


# =============================
# Задание 3. Класс «Автобус».
#
# Свойства:
# ✅ скорость
# ✅ макс. кол-во мест
# ✅ макс. скорость
# ✅ список фамилий пассажиров
# ✅ флаг наличия свободных мест
# ✅ словарь мест (номер: фамилия)
#
# Методы:
# ✅ посадка/высадка одного или нескольких пассажиров
# ✅ увеличение/уменьшение скорости на заданное значение
# ✅ операции:
#   - `in` проверяет фамилию в списке
#   - `+=` посадка
#   - `-=` высадка


# === TODO: реализовать класс Bus ===
class Bus:
    def __init__(self, max_seats, max_speed):
        """Инициализирует поля"""
        self.max_seats = max_seats  # максимальное количество мест
        self.max_speed = max_speed  # максимальная скорость
        self.speed = 0  # скорость (изначально 0)
        self.list_surname = []  # список фамилий пассажиров
        self.has_free_seats = True  # флаг свободных мест (изначально True)
        self.seats = {seat_num: None for seat_num in range(1, max_seats + 1)}  # Cловарь мест

    def update_state(self):
        """Обновляет список фамилий и флаг свободных мест"""
        self.list_surname = [p for p in self.seats.values() if p is not None]  # Обновляем Список фамилий
        self.has_free_seats = any(p is None for p in self.seats.values())  # Обновляем флаг свободных мест

    def board(self, *passengers):
        """Проводит посадку пассажиров"""
        for surname in passengers:
            # Проверка на наличие пассажира в автобусе
            if surname in self.seats.values():
                print(f"Пассажир {surname} уже в автобусе")
                continue
            # Перебираем словарь и добавляет Фамилию в пустое значение
            for seat_num, passenger in self.seats.items():
                if passenger is None:
                    self.seats[seat_num] = surname
                    break
            else:  # если свободных нет
                print("Автобус полон!")

        self.update_state()  # Обновляем список фамилий и флаг свободных мест

    def unboard(self, *passengers):
        """Проводит высадку пассажиров"""
        for surname in passengers:
            # Проверка на наличие пассажира в автобусе
            if surname not in self.seats.values():
                print(f"Пассажира {surname} нет в автобусе")
                continue
            # Перебираем словарь и удаляет Фамилию присваивая (None) пустое значение
            for seat_num, passenger in self.seats.items():
                if passenger == surname:
                    self.seats[seat_num] = None
                    break
            else:  # Автобус пуст
                print("Автобус пуст!")
        self.update_state()  # Обновляем список фамилий и флаг свободных мест

    def change_speed(self, delta):
        """Изменяет скорость на delta"""
        new_speed = self.speed + delta
        # Проверяем скорость по разрешимому диапазону
        if 0 <= new_speed <= self.max_speed:
            self.speed = new_speed
            print(f"Скорость установлена: {self.speed}")
            return self.speed
        else:
            return print(f"Изменение скорости на {delta} недопустимо. Допустимый диапазон: 0 - {self.max_speed}")

    def __contains__(self, surname):
        """Проверяет фамилию пассажира"""
        return surname in self.list_surname

    def __iadd__(self, surname):
        """Проводит посудку пассажира += посадка"""
        self.board(surname)
        return self

    def __isub__(self, surname):
        """Проводит высадку пассажира += посадка"""
        self.unboard(surname)
        return self


# === Тесты для задачи 3 ===
print("\n=== Задача 3: Автобус ===")
bus = Bus(max_seats=3, max_speed=100)
bus.board("Иванов", "Петров")
print(bus.list_surname)
print("Иванов" in bus)  # True
bus += "Сидоров"
print("Сидоров" in bus)  # True
bus -= "Петров"
print("Петров" in bus)  # False
bus.change_speed(20)
