def show_inventory(player):
    print("Inventory")
    for item in player.inventory:
        print(f"- {item.name}")