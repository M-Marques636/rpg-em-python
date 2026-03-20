def choose_attributes(player):
    
    print(f"{player.name} subiu para o nível {player.level}!")
    
    print("Escolha um atributo:")
    print("1 - Vitalidade (+15 HP)")
    print("2 - Força (+5 dano)")
    print("3 - Destreza (+5)")
    print("4 - Sorte (+5)")

    choice = input("> ")
                  
    while choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid command, please try again.")   
            print("1 - Vitality (+15 HP)")
            print("2 - Strength (+5 damage)")
            print("3 - Dexterity (+5)")
            print("4 - Luck (+5)")

            choice = input("> ")
            
    return choice