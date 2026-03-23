from ui.story.cabin_ui import (
    show_cabin, 
    show_cabin_inside, 
    show_chest, 
    show_exit_cabin, 
    show_fireplace, 
    show_table, 
    show_back
)
from ui.input_handler import (
    ask_action, 
    ask_cabin)

import time

def cabin(player):
    from scenes.forest import forest

    show_cabin()
    choice = ask_action()

    if choice == "entrar":
        while True:
            show_cabin_inside()
            choice = ask_cabin()

            if choice == "lareira":
                interact_area(show_fireplace)

            elif choice == "bau":
                interact_area(show_chest)

            elif choice == "mesa":
                interact_area(show_table)

            elif choice == "sair":
                show_exit_cabin()
                time.sleep(1)
                forest(player)
                break

    elif choice == "sair":
        forest(player)


def interact_area(show_function):
    show_function()
    
    while True:
        show_back()
        choice = ask_action()

        if choice == "sair":
            break

    
    