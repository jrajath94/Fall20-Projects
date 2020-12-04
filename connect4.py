
def board_printer(board):
    for row in board:
        print(row)

def create_board(m,n):
    game_board = [["*" for i in range(m)] for j in range(n)]
   # print(game_board)
    board_printer(game_board)
    return game_board

def transpose_matrix(board):
    #print([[row[i] for row in board] for i in range(len(board[0]))])
    return [[row[i] for row in board] for i in range(len(board[0]))]


def check_victory(board, pawn):
    # Check for vertical line
    for i in range(0, len(board) - 3):
        for j in range(0, len(board[0])):
            if (board[i][j] == pawn and board[i + 1][j] == pawn and board[i + 2][j] == pawn and board[i + 3][
                j] == pawn):
                return True

    # Check for horizontal line

    for j in range(0, len(board[0]) - 3):
        for i in range(0, len(board)):
            # print(i,j)
            if (board[i][j] == pawn and board[i][j + 1] == pawn and board[i][j + 2] == pawn and board[i][
                j + 3] == pawn):
                return True

        # Check for Asecending Diagonal line
    for i in range(3, len(board)):
        for j in range(0, len(board[0]) - 3):
            if (board[i][j] == pawn and board[i - 1][j + 1] == pawn and board[i - 2][j + 2] == pawn and board[i - 3][
                j + 3] == pawn):
                # print(board[i][j], board[i - 1][j + 1], board[i - 2][j + 2] ,board[i - 3][j + 3])
                return True

        # Check for Descending Diagonal line
    for i in range(3, len(board)):
        for j in range(3, len(board[0])):
            if (board[i][j] == pawn and board[i - 1][j - 1] == pawn and board[i - 2][j - 2] == pawn and board[i - 3][
                j - 3] == pawn):
                return True

    return False


def fetch_possible_columns(board):
    transposed_board = deepcopy(transpose_matrix(board)) # board_printer(board)

    count = 0
    possibilities = []
    for column in transposed_board:
        if "*" in column:
            possibilities.append(count)
        count += 1

    return possibilities


def insert_element(board, player, column_number):

    transposed_board = deepcopy(transpose_matrix(board))
    index = transposed_board[column_number].count("*")
  #  print(" Index of * in ", transposed_board[column_number], "is ", index)
    transposed_board[column_number][index - 1] = player

    board = deepcopy(transpose_matrix(transposed_board))
    print("Current Board Status After Insertion - ")
    board_printer(board)

    return board


from copy import deepcopy

player_turn = 1

print("**************************************************")
print("***************** Let's Connect! *****************")
print("**************************************************")
game_board = deepcopy(create_board(7, 7))

while True:
    if player_turn == 1:
        player_request0 = input(
            "Player {} Please enter the Column Number you wish to have your coin \n \n ".format(player_turn))
        player_turn = 2
        possible_columns = fetch_possible_columns(game_board)

        while True:
            if int(player_request0) in possible_columns:
                print("You've entered a valid column, inserting the coin to the column {}".format(player_request0))
                game_board = deepcopy(insert_element(game_board, '1', int(player_request0)))
                break
            else:
                player_request0 = print("Please enter a valid column , the valid columns are - ", possible_columns)

        if (check_victory(game_board, '1')):
            print("Player 1 has won the game, Thank you for Playing :) ")
            break

    if player_turn == 2:
        player_request1 = input(
            "Player {} Please enter the Column Number you wish to have your coin \n \n ".format(player_turn))
        player_turn = 1
        possible_columns = fetch_possible_columns(game_board)

        while True:
            if int(player_request1) in possible_columns:
                print("You've entered a valid column, inserting the coin to the column {}".format(player_request0))
                game_board = deepcopy(insert_element(game_board, '2', int(player_request1)))
                break
            else:
                player_request0 = print("Please enter a valid column , the valid columns are - ", possible_columns)

        if (check_victory(game_board, '2')):
            print("Player 2 has won the game, Thank you for Playing :) ")
            break



