class TV:
    def __init__(self):
        self.on = False

    def toggle(self):
        self.on = not self.on


class LivingRoom:
    def __init__(self):
        self.occupied = False

    def occupy(self):
        self.occupied = not self.occupied


class Kitchen:
    def __init__(self):
        self.cooking = False

    def cook(self):
        self.cooking = not self.cooking


class House:
    def __init__(self):
        self.tv = None
        self.number = None
        self.kitchen = None
        self.living_room = None

    def __str__(self):
        str = f'House {self.number}'
        str += ' '
        str += f'kitchen.cooking={self.kitchen.cooking}'
        str += ' '
        str += f'living_room.occupied={self.living_room.occupied}'
        str += ' '
        str += f'tv.on={self.tv.on}'
        return str


class HouseFactory:
    def create(self, number):
        house = House()
        house.number = number
        house.tv = TV()
        house.kitchen = Kitchen()
        house.living_room = LivingRoom()
        return house


if __name__ == '__main__':
    factory = HouseFactory()
    house_a = factory.create(103)
    house_b = factory.create(104)

    house_a.kitchen.cook()
    house_b.living_room.occupy()
    house_a.tv.toggle()
    print(house_a)
    print(house_b)

    house_a.kitchen.cook()
    house_b.living_room.occupy()
    house_a.tv.toggle()
    print(house_a)
    print(house_b)

    # House 103 kitchen.cooking=True living_room.occupied=False tv.on=True
    # House 104 kitchen.cooking=False living_room.occupied=True tv.on=False
    # House 103 kitchen.cooking=False living_room.occupied=False tv.on=False
    # House 104 kitchen.cooking=False living_room.occupied=False tv.on=False
