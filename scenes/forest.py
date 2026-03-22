from ui.input_handler import ask_directions
from ui.story.forest_ui import show_forest

def forest():
    from scenes.cabin import cabin
    show_forest()
    
    choice = ask_directions().lower()
    if choice == "norte":
        cabin()