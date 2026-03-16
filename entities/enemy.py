import random

class Enemy():
    def __init__(self, name, max_health, damage, exp):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.damage = damage
        self.exp = exp
        
    def attack(self):
        return random.randint(*self.damage)
    
    def receive_damage(self, damage):
        self.health -= damage
        
    def alive(self):
        return self.health > 0
        