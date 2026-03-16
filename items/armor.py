from items.item import Item

class Armor(Item):
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense