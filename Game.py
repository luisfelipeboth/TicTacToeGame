from os import system,name
import random

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

def display(row1,row2,row3,dict,data):
    keys = list(dict.keys())
    values = list(dict.values())
    names = list(data.keys())
    markers = list(data.values())
    clear_screen()
    print("The score of the game is:")
    print(f"{keys[0]}: {values[0]}")
    print(f"{keys[1]}: {values[1]}")
    print(f"The player {names[0]} is the marker: {markers[0]}")
    print(f"The player {names[1]} is the marker: {markers[1]}")
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

def replacement_choice(game_matrix, intern_matrix, position, data):
    if position in range(7,10):
        row_index = 0
    elif position in range(4,7):
        row_index = 1
    else:
        row_index = 2

    column_index = check_column_index(position)
    intern_matrix[row_index][column_index] = data
    if position == 7 or position == 4 or position == 1:
        data = "  " + data
    game_matrix[row_index][column_index] = data
    return game_matrix, intern_matrix

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

def check_winner(game_matrix, marker, dict):
    winner_name = ""
    winner = False

    # Check if there is a winner
    if game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] == "X" or game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] == "O":
        winner = True
    elif game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] == "X" or game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] == "O":
        winner = True
    elif game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] == "X" or game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] == "O":
        winner = True
    elif game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] == "X" or game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] == "O":
        winner = True
    elif game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] == "X" or game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] == "O":
        winner = True
    elif game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] == "X" or game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] == "O":
        winner = True
    elif game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] == "X" or game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] == "O":
        winner = True
    elif game_matrix[2][0] == game_matrix[1][1] == game_matrix[0][2] == "X" or game_matrix[2][0] == game_matrix[1][1] == game_matrix[0][2] == "O":
        winner = True
    else:
        winner = False
    
    # Check winner name
    winner_name = list(dict.keys())[list(dict.values()).index(marker)]
    print(game_matrix)
    return winner, winner_name

def update_score(player, dict):
    if player == 1:
        dict[player] = dict[player] + 1
    else:
        dict[player] = dict[player] + 1

    return dict

def winner_screen(dict,winner_name):
    clear_screen()
    keys = list(dict.keys())
    values = list(dict.values())
    print("---------------------------------------")
    print(f"The player {winner_name} was the winner!")
    print("---------------------------------------\n")
    print("---------------------------------------")
    print("The final score is:")
    print(f"{keys[0]}: {values[0]}")
    print(f"{keys[1]}: {values[1]}")
    print("---------------------------------------\n")
    return keep_playing()

def not_winner_screen():
    # there is no winner, ask for keep playing
    clear_screen()
    print("----------------------")
    print("There wasn't a winner!")
    print("----------------------\n")
    return keep_playing()

def randomize_player(playerOneName,playerTwoName):
    rand_number = random.randint(1,100)
    if rand_number%2 == 0:
        first_player = playerOneName
        second_player = playerTwoName
    else:
        first_player = playerTwoName
        second_player = playerOneName
    return first_player,second_player

def main_game():
    # Initialize variables
    clear_screen()
    playerOneName = "1"
    playerTwoName = "2"
    player_playing = 1
    score = {playerOneName:0,playerTwoName:0}
    game_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
    intern_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
    rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]
    valid_inputs = [1,2,3,4,5,6,7,8,9]
    keep_playing_flag = True
    game_on = True
    winner = False
    
    # Starter tasks
    playerOneName, playerTwoName = ask_names()
    score[playerOneName] = score["1"]
    score[playerTwoName] = score["2"]
    del score["1"]
    del score["2"]

    first, second = randomize_player(playerOneName,playerTwoName)
    data = {first:"X",second:"O"}

    # Repeat tasks
    while keep_playing_flag:
        while game_on:
            display(rows[0],rows[1],rows[2],score,data)
            choice = player_input(valid_inputs)
            #check player plaing
            if player_playing == 1:
                marker = data[first]
            else:
                marker = data[second]
            game_matrix, intern_matrix = replacement_choice(game_matrix,intern_matrix,choice,marker)
            rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]
            display(rows[0],rows[1],rows[2],score,data)
            valid_inputs.remove(choice)
            winner, winner_name = check_winner(intern_matrix, marker, data)
            
            # Change player playing
            player_playing = (player_playing + 1) % 2   
            if winner:
                game_on = False
                score = update_score(winner_name, score)
                keep_playing_flag = winner_screen(score, winner_name)
                first, second = randomize_player(playerOneName,playerTwoName)
                if keep_playing_flag:
                    # Re-Initialize the matrix and some variables
                    game_on = True
                    first, second = randomize_player(playerOneName,playerTwoName)
                    data = {first:"X",second:"O"}
                    player_playing = 1
                    valid_inputs = [1,2,3,4,5,6,7,8,9]
                    game_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
                    intern_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
                    rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]

            if len(valid_inputs) == 0 and not winner:
                game_on = False
                keep_playing_flag = not_winner_screen()
                first, second = randomize_player(playerOneName,playerTwoName)
                if keep_playing_flag:
                    # Re-Initialize the matrix and some variables
                    game_on = True
                    first, second = randomize_player(playerOneName,playerTwoName)
                    data = {first:"X",second:"O"}
                    player_playing = 1
                    valid_inputs = [1,2,3,4,5,6,7,8,9]
                    game_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
                    intern_matrix = [["   "," "," "],["   "," "," "],["   "," "," "]]
                    rows = ["  |  ".join(game_matrix[0]),"  |  ".join(game_matrix[1]),"  |  ".join(game_matrix[2])]



### RUN THE HOLE PROGRAM
main_game()