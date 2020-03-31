def display_initial_message():
    print("\n#################")
    print("Welcome to Pivit!")
    print("#################\n")
    print("Made by Bernardo Ramalho and Pedro Pereira for IART 2020.\n")
    print("Before we start here are some general rules of the game:")
    print("1.Player 1 has the blue pieces and Player 2 has the red pieces.")
    print("2.The point of the game is it to have more evolved pieces then your opponent at the end of the game.")
    print("3.The game ends when there are no more unenvolved pieces. To evolve a piece you just have to get it to one "
          "of the corners of the board.")
    print("4.Pieces can move in the direction their arrows point to and to a square of different colour then the one "
          "they are in. Unless they are evolved, in which case they can move to any square in that direction.")
    print("5.The last thing in mind is that you cannot jump over pieces but you can eat pieces by moving one of your "
          "pieces to an enemy occupied square.")
    print("\nBasic Commands:")
    print("To move just click on a piece and then click on the square you want to move it to.")
    print("If you select the wrong piece, you can click 'r' to reset.")
    print("If you want to exit the game click 'q'.")
    print("You can also use 'f' to forfeit a match.")
    print("If you want a suggestion from the AI you can click 'd'.")
    print("\nWe give you three game modes for you to enjoy the game:")
    print("1. PvP or Player vs Player. This is where you can battle against your friends.")
    print("2. PvE or Player vs Environment. This is where you can face against our AI in case you don't have any "
          "friends.")
    print("3. EvE or Environment vs Environment. This is a mode for you to sit back and relax while you watch some AI "
          "vs AI action.")
    print("\nWe hope you have fun and enjoy our game!\n")


def display_result_message(winner):
    if winner == 1:
        print("Player 1 has won the game!")
    elif winner == 2:
        print("Player 2 has won the game!")
    else:
        print("We have a drawn!")


def get_game_mode():
    """Asks the user for a game mode"""
    mode = input("Select Game Mode:\n1. PvP\n2. PvE\n3. EvE\nDesired Mode: ")

    if mode != '1' and mode != '2' and mode != '3':
        return ask_game_mode_again()
    else:
        return mode


def ask_game_mode_again():
    mode = input("Please select a valida Game Mode:\n1. PvP\n2. PvE\n3. EvE\nDesired Mode: ")

    if mode != '1' and mode != '2' and mode != '3':
        return ask_game_mode_again()
    else:
        return mode


def get_ai_depth():
    """Asks the user for the depth to be used for the AI"""
    print("Please choose the depth to which the AI should search.")
    print("The bigger the depth the more time it will take for the AI to choose a move. You can choose between 1 and "
          "17.")
    print("We recommend choosing 3 or 4. 3 will take, in average, around 2 seconds and 4 will take , in average,"
          "around 45 seconds.")
    print("In our testing, in depth 5 it took between 3:30 minutes and 2:30 minutes. We couldn't access further then 5"
          " depth so adventure at your own risk.\n")
    print("All those times will vary depends on your computer's power.")
    depth = int(input("Desired Depth: "))

    if depth < 1 or depth > 17:
        return ask_depth_again()
    else:
        return depth


def ask_depth_again():
    print("You inserted an invalid depth.")
    depth = int(input("Please insert a value between 1 and 17: "))

    if depth < 1 or depth > 17:
        return ask_depth_again()
    else:
        return depth


def get_ai_mode():
    print("Please select the ai mode you desire:")
    ai_mode = input("1.Aggressive\n2.Defensive\n3.Neutral\nDesired mode:")

    if ai_mode != '1' and ai_mode != '2' and ai_mode != '3':
        return ask_ai_mode_again()
    else:
        return ai_mode


def ask_ai_mode_again():
    print("Please select a valid ai mode:")
    ai_mode = input("1.Aggressive\n2.Defensive\n3.Neutral\nDesired mode:")

    if ai_mode != '1' and ai_mode != '2' and ai_mode != '3' and ai_mode != '4':
        return ask_ai_mode_again()
    else:
        return ai_mode


def get_two_ai_modes():
    print("Mode for the 1st AI")
    ai_mode1 = get_ai_mode()
    print("Mode for the 2nd AI")
    ai_mode2 = get_ai_mode()

    return ai_mode1, ai_mode2
