from ui.story.mountain_ui import (
    show_mountain,
    show_mountain_inside,
    show_mountain_not_ready
)
from ui.input_handler import ask_action


def mountain(player):
    from scenes.forest import forest

    show_mountain()
    choice = ask_action()

    if choice == "entrar":

        if player.level < 50:
            while True:
                show_mountain_not_ready()
                choice = ask_action()

                if choice == "sair":
                    forest(player)
                    return

        show_mountain_inside()

    elif choice == "sair":
        forest(player)