from factory.item_factory import create_item
from factory.enemy_factory import create_enemy
from entities.player import Player
from entities.enemy import Enemy
from systems.combat import attack, battle
from systems.encounter import fight
from ui.combat_logs import show_damage, show_death
from systems.level import level_up, update_stats
from systems.inventory import add_item
from ui.inventory_ui import show_inventory
from ui.status_ui import show_status
from scenes.forest import forest

def start_game():
    print("Um dia você acorda no meio do nada, tudo que vê em sua volta é uma floresta que parece ser infinita de todos os lados.")
    
    name = input("Você não se lembra de nada...  absolutamente nada, tirando seu nome, que é: ")
    return name

player_name = start_game()
player = Player(player_name)
forest(player)