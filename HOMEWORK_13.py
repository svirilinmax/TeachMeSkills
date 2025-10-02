# ================================
# TeachMeSkills.by — Домашнее задание
# ================================
from abc import ABC, abstractmethod
"""
Здесь задания на генераторы и паттерны проектирования:
- Строитель
- Фабричный метод
- Стратегия

Заполняйте TODO, читайте комментарии и запускайте тесты.
"""

# ================================
# ЗАДАНИЕ 1: Генератор чисел Фибоначчи
# ================================

def fibonacci_generator(n: int):
    """Генераторная функция, возвращает n чисел Фибоначчи."""
    f1, f2 = 0, 1
    for _ in range(n):
        yield f1
        f1, f2 = f2, f1 + f2


# Тест:
print("\n--- Задание 1 ---")
n = int(input("Сколько чисел Фибоначчи вывести? "))
for num in fibonacci_generator(n):
    print(num, end=' ')
print()


# ================================
# ЗАДАНИЕ 2: Бесконечная циклическая последовательность
# ================================

def cycle_123():
    """Генераторная функция, бесконечно выдаёт 1-2-3"""
    num_1, num_2, num_3 = 1, 2, 3
    while True:
        yield num_1
        yield num_2
        yield num_3


# Тест:
print("\n--- Задание 2 ---")
count = int(input("Сколько чисел вывести из бесконечного цикла? "))
gen = cycle_123()
result = [str(next(gen)) for _ in range(count)]
print('-'.join(result))


# ================================
# ЗАДАНИЕ 3: Паттерн «Строитель»
# ================================

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return (f"Pizza (size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni},"
                f"mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})")


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        """Добавляем размер"""
        self.pizza.size = size
        return self

    def add_cheese(self):
        """Добавляем сыр"""
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        """Добавляем пепперони"""
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        """Добавляем грибы"""
        self.pizza.mushrooms = True
        return self

    def add_onion(self):
        """Добавляем лук"""
        self.pizza.onions = True
        return self

    def add_bacon(self):
        """Добавляем бекон"""
        self.pizza.bacon = True
        return self

    def build(self):
        """Создаём пиццу"""
        pizza = self.pizza  # Сохраняем готовую пиццу в pizza
        self.pizza = Pizza()  # Присваиваем первоначальное значение.
        return pizza  # Возвращаем готовую пиццу


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        """Делает стандартную пиццу"""
        return (
            self.builder
            .set_size("Large")
            .add_cheese()
            .add_pepperoni()
            .build()
        )

    def make_pizza_pepperoni(self):
        """Делаем пиццу пепперони"""
        return (
            self.builder
            .set_size("Small")
            .add_cheese()
            .add_pepperoni()
            .add_mushrooms()
            .build()
        )

    def make_pizza_margarita(self):
        """Делаем пиццу маргарита"""
        return (
            self.builder
            .set_size("Medium")
            .add_cheese()
            .build()
        )

    def make_pizza_vegan(self):
        """Делаем пиццу вегетарианскую"""
        return (
            self.builder
            .set_size("Extra Large")
            .add_mushrooms()
            .add_onion()
            .build()
        )


# Тест:
print("\n--- Задание 3 ---")
builder = PizzaBuilder()
director = PizzaDirector(builder)

# Собираем стандартную пиццу
standard_pizza = director.make_pizza()
print("Standard:", standard_pizza)

vegan_pizza = director.make_pizza_vegan()
print("Vegan:", vegan_pizza)

# Собираем пиццу пепперони
pepperoni = director.make_pizza_pepperoni()
print("Pepperoni:", pepperoni)

# Собираем пиццу "Маргарита"
margarita = director.make_pizza_margarita()
print("Margarita:", margarita)

# ================================
# ЗАДАНИЕ 4: Паттерн «Фабричный метод»
# ================================

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    """Язык собаки"""

    def speak(self):
        """Собака говорит"""
        return "Dog is speak: Wof-wof"


class Cat(Animal):
    """Язык кота"""

    def speak(self):
        """Кот говорит"""
        return "Cat is speak: Meow-meow"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        """Возвращает Dog или Cat в зависимости от animal_type"""
        DOG = "dog"
        CAT = "cat"
        if animal_type == DOG:
            return Dog()
        elif animal_type == CAT:
            return Cat()
        else:
            raise ValueError(f"Нет такого животного {animal_type}")


# Тест:
print("\n--- Задание 4 ---")
factory = AnimalFactory
animal = factory.create_animal("dog")
print(animal.speak())
animal = factory.create_animal("cat")
print(animal.speak())


# ================================
# ЗАДАНИЕ 5: Паттерн «Стратегия»
# ================================

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(OperationStrategy):
    def execute(self, a, b):
        """Реализуется метод сложения"""
        return a + b


class Subtraction(OperationStrategy):
    def execute(self, a, b):
        """Реализуется метод вычитания"""
        return a - b


class Multiplication(OperationStrategy):
    def execute(self, a, b):
        """Реализуется метод умножения"""
        return a * b


class Division(OperationStrategy):
    def execute(self, a, b):
        """Реализуется метод деления"""
        if b == 0:
            raise ZeroDivisionError(f"b = {b}. Деление на {b} запрещено")
        return a / b


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: OperationStrategy):
        """Выбирается метод (стратегия)"""
        self.strategy = strategy

    def calculate(self, a, b):
        """Выполняется операция через текущую стратегию"""
        if self.strategy is None:
            raise ValueError("Strategy not set!")
        return self.strategy.execute(a, b)


# Тест:
print("\n--- Задание 5 ---")
calc = Calculator()
calc.set_strategy(Addition())
print("5 + 3 =", calc.calculate(5, 3))
calc.set_strategy(Subtraction())
print("5 - 3 =", calc.calculate(5, 3))
calc.set_strategy(Multiplication())
print("5 * 3 =", calc.calculate(5, 3))
calc.set_strategy(Division())
print("5 / 3 =", calc.calculate(5, 3))

# ================================
# УДАЧИ! 🚀
# ================================
