from ui.story.cabin_ui import show_cabin, show_cabin_inside, show_chest, show_exit_cabin, show_fireplace, show_table
from ui.input_handler import ask_action, ask_cabin

def cabin():
    from scenes.forest import forest
    show_cabin()
    choice = ask_action()
    if choice == "entrar":
        show_cabin_inside()
        choice = ask_cabin()
        if choice == "lareira":
            show_fireplace()
        elif choice == "chest":
            show_chest()
        elif choice == "mesa":
            show_table
        elif choice == "sair":
            show_exit_cabin
    elif choice == "sair":
        forest()        
            
            
    
    
    