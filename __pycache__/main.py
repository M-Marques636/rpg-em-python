from items.item_factory import create_item
from entities.player import Player
from entities.enemy import Enemy
from systems.combat import attack
from systems.combat import battle
from ui.combat_logs import show_damage
from ui.combat_logs import show_death
from data.enemy_types import Elf 
from data.enemy_types import Orc
from data.enemy_types import Bear
from data.enemy_types import Goblin

player = Player("Hero")

sword = create_item("iron_sword")

armor = create_item("iron_armor")

player.inventory.append(sword)

player.inventory.append(armor)

player.equip(armor)
player.equip(sword)

elf = Elf
orc = Orc
goblin = Goblin
bear = Bear

print(player.exp)
print(player.exp_max)
print(player.level)

battle(player, orc)


battle(player, orc)

