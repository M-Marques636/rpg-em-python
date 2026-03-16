import random

class Player():

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp_max = 100 * self.level
        self.max_health = 100
        self.health = self.max_health
        self.damage = (5, 10)
        self.inventory = ["Stick"]
        
    def attack(self):
        return random.randint(*self.damage)

    def receive_damage(self, damage):
        self.health -= damage
        
    def level_up(self, exp):
        if exp > self.exp_max:
            self.level += 1
            self.exp_max = 100 * self.level
    
    def alive(self):
        return self.health > 0
    