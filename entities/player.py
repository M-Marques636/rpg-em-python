import random

class Jogador():

    def __init__(self, nome):
        self.nome = nome
        self.level = 1
        self.vida_max = 100
        self.vida = self.vida_max
        self.ataque = (5, 10)
        self.inventario = []
        
    def atacar(self):
        return random.randint(*self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        