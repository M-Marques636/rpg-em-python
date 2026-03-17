from entities.enemy import Enemy
from items.item_factory import create_item
from data.items import ITEM_DATABASE


Elf = Enemy("Elf", 50, (10, 25), 25, create_item("wooden_bow"), create_item("leather_armor"))
Goblin = Enemy("Goblin", 30, (5, 10), 5, create_item("stick"), None)
Bear = Enemy("Urso", 60, (10, 15), 15, None, None)
Orc = Enemy("Orc", 75, (20, 30), 20, create_item("orc_wooden_club"), None)