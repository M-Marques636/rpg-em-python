from ui.level_up_logs import choose_attributes



def level_up(player, enemy):
    player.exp += enemy.exp
   

    while player.exp >= player.exp_max:
        player.exp -= player.exp_max
        player.level += 1
        player.exp_max = 100 * player.level

        decision = choose_attributes(player)
        
        attributes(decision, player)
        
        update_stats(player)
            
def update_stats(player):
    player.max_health = 100 + (player.vitality * 15)
    player.health = player.max_health
    player.damage = (10 + (player.strength * 5), 15 + (player.strength * 5))
    
def attributes(choice, player):
    if choice == "1":
        player.vitality += 1
    elif choice == "2":
        player.strength += 1
    elif choice == "3":
        player.dexterity += 1
    elif choice == "4":
        player.luck += 1