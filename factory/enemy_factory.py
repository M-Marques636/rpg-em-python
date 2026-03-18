from entities.enemy import Enemy
from factory.item_factory import create_item
from data.enemy_types import ENEMY_DATABASE

def create_enemy(enemy_id):
    data = ENEMY_DATABASE[enemy_id]

    weapon = create_item(data["weapon"]) if data["weapon"] else None
    armor = create_item(data["armor"]) if data["armor"] else None

    return Enemy(
        data["name"],
        data["health"],
        data["damage"],
        data["exp"],
        weapon,
        armor
    )