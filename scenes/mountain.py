from ui.story.mountain_ui import show_mountain, show_mountain_inside, show_mountain_leave, show_not_ready
from ui.input_handler import ask_action

def mountain(player):
    from scenes.forest import forest
    show_mountain()
    choice = ask_action()
    if choice == "entrar" and player.level >= 50:
        show_mountain_inside()
    elif choice == "entrar" and player.level < 50:
        show_not_ready()
        choice = ask_action()
        while choice != "sair":
            show_not_ready()
            choice = ask_action()
        else:
            forest(player)
    elif choice == "sair":
        forest(player)