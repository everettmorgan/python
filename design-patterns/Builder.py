from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def name(self):
        ...

    @abstractmethod
    def packing(self):
        ...

    @abstractmethod
    def price(self):
        ...


class Packing(ABC):
    @abstractmethod
    def pack(self):
        ...


class Wrapper(Packing):
    def pack(self):
        return 'Wrapper'


class Bottle(Packing):
    def pack(self):
        return 'Bottle'


class Burger(Item, ABC):
    def packing(self):
        return Wrapper()

    @abstractmethod
    def price(self):
        ...


class ColdDrink(Item, ABC):
    def packing(self):
        return Bottle()

    @abstractmethod
    def price(self):
        ...


class BeefBurger(Burger):
    def name(self):
        return 'Beef Burger'

    def price(self):
        return 14.99


class VeggieBurger(Burger):
    def name(self):
        return 'Veggie Burger'

    def price(self):
        return 19.99


class Coke(ColdDrink):
    def name(self):
        return 'Coke'

    def price(self):
        return 3.99


class Pepsi(ColdDrink):
    def name(self):
        return 'Pepsi'

    def price(self):
        return 4.99


class Meal:
    items = []
    price = 0

    def __init__(self, name):
        self.name = name

    def add_item(self, item):
        self.items.append(item)
        self.price += item.price() if item is not None else 0

    def display(self):
        print(f'=== {self.name} ===')
        for item in self.items:
            print('Item:', item.name(), item.price(), 'Packing:', item.packing().pack())
        print('Total:', round(self.price, 2), '\n')


class MealBuilder:
    @staticmethod
    def veggie():
        meal = Meal('Veggie Meal')
        meal.add_item(VeggieBurger())
        meal.add_item(Pepsi())
        return meal

    @staticmethod
    def non_veggie():
        meal = Meal('Non-Veggie Meal')
        meal.add_item(BeefBurger())
        meal.add_item(Coke())
        return meal


if __name__ == '__main__':
    veg_meal = MealBuilder.veggie()
    non_veg_meal = MealBuilder.non_veggie()

    veg_meal.display()
    non_veg_meal.display()

    # === Veggie Meal ===
    # Item: Veggie Burger 19.99 Packing: Wrapper
    # Item: Pepsi 4.99 Packing: Bottle
    # Item: Beef Burger 14.99 Packing: Wrapper
    # Item: Coke 3.99 Packing: Bottle
    # Total: 24.98
    #
    # === Non-Veggie Meal ===
    # Item: Veggie Burger 19.99 Packing: Wrapper
    # Item: Pepsi 4.99 Packing: Bottle
    # Item: Beef Burger 14.99 Packing: Wrapper
    # Item: Coke 3.99 Packing: Bottle
    # Total: 18.98
