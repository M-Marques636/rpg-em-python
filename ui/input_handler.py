from data.comands import directions, actions, cabin

def ask_directions():
    choice = input("> ").lower()

    while choice not in directions:
        print("Opção inválida.")
        choice = input("> ").lower()

    choice = directions[choice] 
    return choice

def ask_action():
    choice = input("> ").lower()

    while choice not in actions:
        print("Opção inválida.")
        choice = input("> ").lower()

    choice = actions[choice]
    return choice

def ask_cabin():
    choice = input("> ").lower()

    while choice not in cabin:
        print("Opção inválida.")
        choice = input("> ").lower()

    choice = cabin[choice]
    return choice