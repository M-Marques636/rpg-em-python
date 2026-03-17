def show_damage(attacker, target, damage):
    print(f"{attacker.name} causou {damage} em {target.name}, deixando {target.name} com {target.health} de vida.\n")

def show_death(entity):
    print(f"{entity.name} morreu\n")