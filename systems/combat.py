def attack(player, enemy):

    weapon_damage = 0

    if player.weapon:
        weapon_damage = player.weapon.stats["damage"]

    damage = player.attack() + weapon_damage

    enemy.receive_damage(damage)