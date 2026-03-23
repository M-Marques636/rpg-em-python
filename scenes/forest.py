from ui.input_handler import ask_directions
from ui.story.forest_ui import show_forest


def forest(player):
    from scenes.cabin import cabin
    from scenes.mountain import mountain
    from scenes.cave import cave
    from scenes.village import village

    while True:
        show_forest()
        choice = ask_directions().lower()

        if choice == "norte":
            mountain(player)

        elif choice == "sul":
            village(player)

        elif choice == "leste":
            cabin(player)

        elif choice == "oeste":
            cave(player)