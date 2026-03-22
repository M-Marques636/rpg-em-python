import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self, rolls):
        for i in range(rolls):
            print(f"Roll {i+1}: {random.randint(1, self.sides)}")
 