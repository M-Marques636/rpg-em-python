from ui.combat_logs import show_damage
from ui.combat_logs import show_death
import time

def battle(player, enemy):
    if not player.alive():
            show_death(player)
    while player.alive() and enemy.alive():
        #time.sleep(2)
        player_turn(player, enemy)

        if not enemy.alive():
            show_death(enemy)
            player.level_up(enemy)
            break
        if not player.alive():
            show_death(player)
            break
        #time.sleep(2)
        enemy_turn(player, enemy)

def player_turn(player, enemy):
    damage = attack(player, enemy)
    show_damage(player, enemy, damage)

def enemy_turn(player, enemy):
    damage = attack(enemy, player)
    show_damage(enemy, player, damage)

def attack(attacker, target):

    weapon_damage = 0
    
    armor_defense = 0

    if target.armor:
        armor_defense = target.armor.stats["defense"]

    if attacker.weapon:
        weapon_damage = attacker.weapon.stats["damage"]

    damage = attacker.attack() + weapon_damage - armor_defense
    if damage < 0:
        damage = 0
    target.receive_damage(damage)
    return damage

