import random
class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp_max = 100 * self.level

        self.max_health = 100
        self.health = self.max_health

        self.damage = (10, 15)

        self.inventory = []

        self.weapon = None
        self.armor = None

    def attack(self):
        return random.randint(*self.damage)

    def receive_damage(self, damage):
        self.health -= damage

    def alive(self):
        return self.health > 0
    
    def equip(self, item):

        if item.type == "weapon":
         self.weapon = item
         
        elif item.type == "armor":
         self.armor = item