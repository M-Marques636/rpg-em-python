def show_status(player):
    print(f"{player.name} status:\n")
    print(f"- Level: {player.level}")
    print(f"- Exp: {player.exp}/{player.exp_max}")
    print(f"- HP: {player.health}/{player.max_health}")
    print(f"- {player.vitality} de Vitalidade")
    print(f"- {player.strength} de Força")
    print(f"- {player.dexterity} de Destreza")
    print(f"- {player.luck} de Sorte")
    
    print(f"\n {player.name} itens equipados:")
    print(f"- {player.weapon}")
    print(f"- {player.armor}")
    
    print(f"\nDano atual: {player.damage} + {player.weapon.stats["damage"]} {player.weapon}")