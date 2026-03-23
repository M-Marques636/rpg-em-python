from ui.story.cave_ui import (
    show_cave,
    show_cave_inside,
    show_cave_not_light,
    show_cave_not_ready
)
from ui.input_handler import ask_action


def cave(player):
    from scenes.forest import forest

    show_cave()
    choice = ask_action()

    if choice == "entrar":

        if player.level < 10:
            while True:
                show_cave_not_ready()
                choice = ask_action()
                if choice == "sair":
                    forest(player)
                    return

        if not player.light:
            while True:
                show_cave_not_light()
                choice = ask_action()
                if choice == "sair":
                    forest(player)
                    return
                
        show_cave_inside()

    elif choice == "sair":
        forest(player)