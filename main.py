from factory.item_factory import create_item
from factory.enemy_factory import create_enemy
from entities.player import Player
from entities.enemy import Enemy
from systems.combat import attack
from systems.combat import battle
from systems.encounter import fight
from ui.combat_logs import show_damage
from ui.combat_logs import show_death
from systems.level import level_up
from systems.level import update_stats
from ui.story_logs import start_game

player_name = start_game()

player = Player(player_name)

print(player.name)
print(player.damage)

fight(player, "orc")