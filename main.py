from items.item_factory import create_item
from entities.player import Player

player = Player("Hero")

sword = create_item("iron_sword")

player.inventory.append(sword)

player.equip(sword)