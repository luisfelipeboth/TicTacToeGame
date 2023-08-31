'''
    Features in my game:
    -- make a counter of winnings of each player (can use dictionary here)
    -- run a sort to see wich player will be playing first (can use random numbers and check if it is even or not)
    -- assign X to player one and O to player two (always that, show this information to the player (the player Luis will be playing as X!, only for the first player))

    Logic in my game:
    -- Initialize variables and display
    -- Ask for input
    -- check input
    -- Update the board
    -- check keep playing
'''
from os import system,name

def clear_screen():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

def ask_names():
    player1 = input("Player one name: ")
    player2 = input("Player two name: ")
    print("\n")
    return player1, player2

def display(row1,row2,row3,dict):
    keys = list(dict.keys())
    values = list(dict.values())
    clear_screen()
    print("The score of the game is:")
    print(f"{keys[0]}: {values[0]}")
    print(f"{keys[1]}: {values[1]}")
    print("---------------------------------------------")
    print("Use your keyboard design to select the place!")
    print("---------------------------------------------\n")
    print(row1)
    print("-----------------")
    print(row2)
    print("-----------------")
    print(row3)
    print("\n")

def player_input(valid_list):
    choice = "WRONG"
    valid = False

    while not choice.isdigit() or not valid:
        choice = input("Chose a number to put your marker: ")
        if not choice.isdigit():
            print("Sorry, but you didn't choose a number!")
        else:
            if int(choice) not in valid_list:
                print("Sorry, but the number isn't availabe!")
                valid = False
            else:
                valid = True

    return int(choice)

def check_column_index(position):
    if position%3 == 0:
        column_index = 2
    elif position%3 == 2:
        column_index = 1
    else:
        column_index = 0
    return column_index

def replacement_choice(game_matrix, position, data):
    if position in range(7,10):
        row_index = 0
    elif position in range(4,7):
        row_index = 1
    else:
        row_index = 2

    column_index = check_column_index(position)
    if position == 7 or position == 4 or position == 1:
        data = "  " + data
    game_matrix[row_index][column_index] = data
    return game_matrix

def keep_playing():
    choice = "WRONG"

    while choice not in ["Y","N"]:
        choice = input("Would you like to keep playing? (Y or N):")
        if choice not in ["Y", "N"]:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice == "Y":
        return True
    else:
        return False

def check_winner():
    pass

def update_score():
    pass

def winner_screen():
    pass

def not_winner_screen():
    # there is no winner, ask for keep playing
    pass

def main_game():
    # Initialize variables
    clear_screen()
    playerOneName = "1"
    playerTwoName = "2"
    player_playing = 1
    score = {playerOneName:0,playerTwoName:0}
    game_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
    rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]
    valid_inputs = [1,2,3,4,5,6,7,8,9]
    keep_playing_flag = True
    game_on = True
    
    # Starter tasks
    playerOneName, playerTwoName = ask_names()
    score[playerOneName] = score["1"]
    score[playerTwoName] = score["2"]
    del score["1"]
    del score["2"]

    # Repeat tasks
    while keep_playing_flag:
        while game_on:
            display(rows[0],rows[1],rows[2],score)
            choice = player_input(valid_inputs)
            if player_playing == 1:
                data = "X"
            else:
                data = "O"
            game_matrix = replacement_choice(game_matrix,choice,data)
            rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]
            display(rows[0],rows[1],rows[2],score)
            valid_inputs.remove(choice)
            if len(valid_inputs) == 0:
                game_on = False

            # check winner
            # update score
            # if winner, display winner screen
            player_playing = (player_playing + 1) % 2

        # Re-Initialize the matrix and some variables
        print("Game finished!")
        game_on = True
        valid_inputs = [1,2,3,4,5,6,7,8,9]
        game_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
        rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]
        keep_playing_flag = keep_playing() # put inside not_winner_screen function

main_game()