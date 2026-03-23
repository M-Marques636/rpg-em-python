def show_cave():
    print("\nCaminhando em direção ao oeste, você se depara com uma caverna intimidadoramente gigante")
    print("Ruidos e sons estranhos vem de dentro, mas é dificil dizer o que exatamente está fazendo\nesses sons, você vê apenas a entrada escura.")
    print("\nO que deseja fazer?")
    print("[S] Seguir em frente (Min: level 10)")
    print("[V] Voltar")
    
def show_cave_not_ready():
    print("Você ainda não esta pronto para adentrar a caverna.")
    print("[V] Voltar")
    
def show_cave_not_light():
    print("Está muito escuro para entrar, se ao menos você tivesse uma lanterna...")
    print("[V] Voltar")
    
def show_cave_inside():
    print("Batata")