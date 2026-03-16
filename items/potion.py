from items.item import Item

class Potion(Item):
    def __init__(self, name, heal):
        super().__init__(name)
        self.heal = heal