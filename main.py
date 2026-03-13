import random
import os
import time
import keyboard
import mouse


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

tempo_dialogo = 1
tempo_combate = 1
espaco = "\n===============================================================\n" 
clique = "\nClique na tela para avançar turno."


nome = input("Digite o nome de seu personagem: ")
level = 0

jogador = {
    "nome": nome,
    "level": (level),
    "vida": 100 + (5* level),
    "ataque": (10, 20),
}
print(jogador)

inimigos = [
    {"nome": "goblin", "vida": 30, "ataque": (5, 10), "exp": (5)},
    {"nome": "urso", "vida": 60, "ataque": (13, 26), "exp": (15)},
    {"nome": "orc", "vida": 50, "ataque": (15, 20), "exp": (13)},
    {"nome": "Miguel", "vida": 10000, "ataque": (100, 1000), "exp": (9999)}
]



def batalha(jogador, inimigo):
    limpar_tela()
    
    print(espaco)
    print(f"Você encontrou um {inimigo['nome']}!")
    print(clique)
    print(espaco)  
    
    mouse.wait(button='left', target_types=['down'])
    limpar_tela()
    
    
    while jogador['vida'] > 0 and inimigo['vida'] > 0:
        
        print(espaco)
        print(f"Você avança e ataca {inimigo['nome']}!")
        print(clique)
        print(espaco)
        
        mouse.wait(button='left', target_types=['down']) 
        limpar_tela()

        dano = random.randint(*jogador["ataque"])
        inimigo["vida"] -= dano
        
        print(espaco) 
        print(f"{jogador['nome']} atacou e causou {dano} de dano. Vida do inimigo: {inimigo['vida']}")
        print(clique)
        print(espaco)   
        
        mouse.wait(button='left', target_types=['down'])  
        limpar_tela()

        if inimigo['vida'] <= 0:
            break
        
        print(espaco)  
        print(f"{inimigo['nome']} se prepara para atacar de volta!")
        print(clique)
        print(espaco)  
        
        mouse.wait(button='left', target_types=['down'])  
        limpar_tela()

        dano = random.randint(*inimigo["ataque"])
        jogador["vida"] -= dano
        
        print(espaco)   
        print(f"{inimigo['nome']} atacou e causou {dano} de dano. Sua vida restante: {jogador['vida']}")
        print(clique)
        print(espaco)  
         
        mouse.wait(button='left', target_types=['down']) 
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
        
        mouse.wait(button='left', target_types=['down']) 
        
            

 
# Testando contra o primeiro inimigo
for inimigo in inimigos:
    batalha(jogador, inimigo)