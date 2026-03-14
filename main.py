import random
import os
import mouse
import keyboard
class Jogador():
    def __init__(self, nome, level, vida, ataque, inventario):
        self.nome = nome
        self.level = level
        self.vida = vida
        self.ataque = ataque
        self.inventario = inventario
        
        def atacar(self):
            return random.randit(*self.ataque)
        
        def receber_dano(self, dano):
            self.vida -= dano
        pass


armas = [
    {"nome": "graveto", "dano": (3), "chance": (2.0, 3.0), "drop": (2.0, 5.0)},
    {"nome": "faca de cozinha", "dano": (7), "chance": (2.0, 3.0), "drop": (6.0, 10.0)},
    {"nome": "cutelo", "dano": (12), "chance": (2.0, 3.0), "drop": (11.0, 20.0)},
    {"nome": "katana", "dano": (20), "chance": (2.0, 3.0), "drop": (21.0, 35.0)}
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

espaco = "\n===============================================================\n" 


nome = input("Digite o nome de seu personagem: ")
level = 0
inventario = []
m_ou_t = ""

jogador = {
    "nome": nome,
    "level": (level),
    "vida": 100 + (5* level),
    "ataque": (10, 20),
    "inventario": (inventario)
}
print(jogador)

inimigos = [
    {"nome": "goblin", "vida": 30, "ataque": (5, 10), "exp": (5), "loot": (0.5)},
    {"nome": "urso", "vida": 60, "ataque": (13, 26), "exp": (15), "loot": (1.5)},
    {"nome": "orc", "vida": 50, "ataque": (15, 20), "exp": (13), "loot": (3.0)},
    {"nome": "Deus", "vida": 10000, "ataque": (100, 1000), "exp": (9999)} 
]
print("Você quer jogar com mouse ou teclado?\n")
while m_ou_t not in ["mouse", "teclado", "m" , "t"]:
    m_ou_t = input("Digite mouse (m) ou teclado (t): ").lower().strip()
    
if m_ou_t in ["mouse", "m"]:
    clique = "\nClique na tela para avançar turno."
else:
    clique = "\nAperte enter para avançar turno."
        
    



def batalha(jogador, inimigo):
    limpar_tela()
    
    print(espaco)
    print(f"Você encontrou um {inimigo['nome']}!")
    print(clique)
    print(espaco)  
    
    if m_ou_t in ["mouse", "m"]:
        mouse.wait(button='left', target_types=['down'])
    else:
        keyboard.wait('enter')
    limpar_tela()
    
    
    while jogador['vida'] > 0 and inimigo['vida'] > 0:
        
        print(espaco)
        print(f"Você avança e ataca {inimigo['nome']}!")
        print(clique)
        print(espaco)
        
        if m_ou_t in ["mouse", "m"]:
            mouse.wait(button='left', target_types=['down'])
        else:
            keyboard.wait('enter')
        limpar_tela()

        dano = random.randint(*jogador["ataque"])
        inimigo["vida"] -= dano
        
        print(espaco) 
        print(f"{jogador['nome']} atacou e causou {dano} de dano. Vida do inimigo: {inimigo['vida']}")
        print(clique)
        print(espaco)   
        
        if m_ou_t in ["mouse", "m"]:
            mouse.wait(button='left', target_types=['down'])
        else:
            keyboard.wait('enter')

        if inimigo['vida'] <= 0:
            break
        
        print(espaco)  
        print(f"{inimigo['nome']} se prepara para atacar de volta!")
        print(clique)
        print(espaco)  
        
        if m_ou_t in ["mouse", "m"]:
            mouse.wait(button='left', target_types=['down'])
        else:
            keyboard.wait('enter') 
        limpar_tela()

        dano = random.randint(*inimigo["ataque"])
        jogador["vida"] -= dano
        
        print(espaco)   
        print(f"{inimigo['nome']} atacou e causou {dano} de dano. Sua vida restante: {jogador['vida']}")
        print(clique)
        print(espaco)  
         
        if m_ou_t in ["mouse", "m"]:
            mouse.wait(button='left', target_types=['down'])
        else:
            keyboard.wait('enter')
        limpar_tela()
        
    if jogador['vida'] <= 0:
        
        print(espaco)
        print("Game over")
        print(espaco)   
        
        exit(True)

    if inimigo['vida'] <= 0:
          
        print(espaco) 
        print(f"Você derrotou {inimigo['nome']} e recebeu {inimigo['exp']} pontos de experiencia!")
        print(clique)
        print(espaco)   
        
        if m_ou_t in ["mouse", "m"]:
            mouse.wait(button='left', target_types=['down'])
        else:
            keyboard.wait('enter')
        
 
# Testando contra o primeiro inimigo
for inimigo in inimigos:
    batalha(jogador, inimigo)