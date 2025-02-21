game_board = [
    ["-","-","-",],
    ["-","-","-"],
    ["-","-","-"]
]

def print_current_board():
    for row in range(len(game_board)):
        for column in range(len(game_board)):
            print(f"{game_board[row][column]:<5}", end = "")
        print("")

def check_for_winner(game_board):
    if game_board[0][0] == game_board[0][1] and game_board[0][1] == game_board[0][2]:
        print("We have a winner!")


print_current_board()

player_1 = input("Player 1, choose X or O: ")
player_1 = player_1.upper()
while player_1 != "X" and player_1 != "O":
    player_1 = input("Oops, that's not an option! Choose X or O: ")
if player_1 == "X":
    player_2 = "O"
else:
    player_2 = "X"
print(f"Player 1 is {player_1} and Player 2 is {player_2}")

print("The spots on the game board are numbered; 1, 2, 3 are the top row, 4, 5, 6 are the next row, and so on")

while game_board[0][0] == "-" or game_board[0][1] == "-" or game_board[0][2] == "-" or game_board[1][0] == "-" or game_board[1][1] == "-" or game_board[1][2] == "-" or game_board[2][0] == "-" or game_board[2][1] == "-" or game_board[2][2] == "-":
    
    while True:
        player_one_turn = int(input("Player 1, enter the number for the spot do you want to take: "))

        if player_one_turn == 1 or player_one_turn == 2 or player_one_turn == 3:
            p_1_row = 0
        elif player_one_turn == 4 or player_one_turn == 5 or player_one_turn == 6:
            p_1_row = 1
        else:
            p_1_row = 2
        if player_one_turn == 1 or player_one_turn == 4 or player_one_turn == 7:
            p_1_column = 0
        elif player_one_turn == 2 or player_one_turn == 5 or player_one_turn == 8:
            p_1_column = 1
        else:
            p_1_column = 2

        if game_board[p_1_row][p_1_column] == "-":
            game_board[p_1_row][p_1_column] = player_1
            break
        else:
            print("That spot is taken, try again:")
            continue

    print_current_board()


    player_two_turn = int(input("Player 2, enter the number for the spot do you want to take: "))

    if player_two_turn == 1 or player_two_turn == 2 or player_two_turn == 3:
        p_2_row = 0
    elif player_two_turn == 4 or player_two_turn == 5 or player_two_turn == 6:
        p_2_row = 1
    else:
        p_2_row = 2
    if player_two_turn == 1 or player_two_turn == 4 or player_two_turn == 7:
        p_2_column = 0
    elif player_two_turn == 2 or player_two_turn == 5 or player_two_turn == 8:
        p_2_column = 1
    else:
        p_2_column = 2

    if game_board[p_2_row][p_2_column] == "-":
        game_board[p_2_row][p_2_column] = player_2

    print_current_board()
