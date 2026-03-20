from factory.enemy_factory import create_enemy
from systems.combat import battle
from entities.player import Player

def fight(player, enemy_id):
    enemy = create_enemy(enemy_id)
    battle(player, enemy)