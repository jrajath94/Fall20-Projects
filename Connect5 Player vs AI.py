import math


def board_printer(board):
    for row in board:
        print(row)


def create_board(m, n):
    game_board = [["*" for i in range(m)] for j in range(n)]
    # print(game_board)
   # board_printer(game_board)
    return game_board


def transpose_matrix(board):
    # print([[row[i] for row in board] for i in range(len(board[0]))])
    return [[row[i] for row in board] for i in range(len(board[0]))]


def check_victory(board, pawn):
    # Check for vertical line
    for i in range(0, len(board) - 4):
        for j in range(0, len(board[0])):
            if (board[i][j] == pawn and board[i + 1][j] == pawn and board[i + 2][j] == pawn and board[i + 3][j] == pawn and board[i+4][j] == pawn):
                return True

    # Check for horizontal line

    for j in range(0, len(board[0]) - 4):
        for i in range(0, len(board)):
            # print(i,j)
            if (board[i][j] == pawn and board[i][j + 1] == pawn and board[i][j + 2] == pawn and board[i][j+3] == pawn and board[i][j+4] == pawn):
                return True

        # Check for Asecending Diagonal line
    for i in range(4, len(board)):
        for j in range(0, len(board[0]) - 4):
            if (board[i][j] == pawn and board[i-1][j+1] == pawn and board[i-2][j+2] == pawn and board[i-3][j+3] == pawn and board[i-4][j+4] == pawn):
                # print(board[i][j], board[i - 1][j + 1], board[i - 2][j + 2] ,board[i - 3][j + 3])
                return True

        # Check for Descending Diagonal line
    for i in range(4, len(board)):
        for j in range(4, len(board[0])):
            if (board[i][j] == pawn and board[i-1][j-1] == pawn and board[i-2][j-2] == pawn and board[i-3][j-3] == pawn and board[i-4][j-4] == pawn):
                return True

    return False


def fetch_possible_columns(board):
    transposed_board = deepcopy(transpose_matrix(board))  # board_printer(board)

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
    #print("Current Board Status After Insertion - ")
   # board_printer(board)

    return board


def get_best_move(board, possible_moves, player):
    new_board = deepcopy(board)
    highest_score = 0
    move_with_highest_score = possible_moves[0]

    for move in possible_moves:
        new_board_2 = deepcopy(insert_element(new_board, player, int(move)))
        score = get_score(new_board_2, player)
        print("Score for move - ", move, " from ", player, " is ", score)

        if score > highest_score:
            highest_score = score
            move_with_highest_score = move

    return move_with_highest_score

def opposition_score(board, pawn):
    opp_score = 0
    for i in range(0, len(board) - 4):
        for j in range(0, len(board[0])):
            elements = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j], board[i + 4][j]]
            if elements.count(pawn) == 5:
                opp_score -= 10000000

    # Check for horizontal line

    for j in range(0, len(board[0]) - 4):
        for i in range(0, len(board)):
            # print(i,j)
            elements = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3], board[i][j + 4]]
            if elements.count(pawn) == 5:
                opp_score -= 10000000

        # Check for Asecending Diagonal line
    for i in range(4, len(board)):
        for j in range(0, len(board[0]) - 4):
            elements = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3], board[i - 4][j + 4]]
            if elements.count(pawn) == 5:
                opp_score -= 10000000

        # Check for Descending Diagonal line
    for i in range(4, len(board)):
        for j in range(4, len(board[0])):
            elements = [board[i][j], board[i - 1][j - 1], board[i - 2][j - 2], board[i - 3][j - 3], board[i - 4][j - 4]]
            if elements.count(pawn) == 5:
                opp_score -= 10000000

    return opp_score

def get_score(board, pawn):
    # Check for vertical line
    score = 0
    for i in range(0, len(board) - 4):
        for j in range(0, len(board[0])):
            elements = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j], board[i + 4][j]]
            if elements.count(pawn) == 5:
                score += 100000000
            if elements.count(pawn) == 4 and elements.count('*') == 1:
                score += 100000
            if elements.count(pawn) == 3 and elements.count('*') == 2:
                score += 10000
            elif elements.count(pawn) ==3 and elements.count('*') < 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') == 3:
                score += 500

                # Check for horizontal line

    for j in range(0, len(board[0]) - 4):
        for i in range(0, len(board)):
            # print(i,j)
            elements = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3],board[i][j + 4]]
            if elements.count(pawn) == 5:
                score += 100000000
            if elements.count(pawn) == 4 and elements.count('*') == 1:
                score += 100000
            if elements.count(pawn) == 3 and elements.count('*') == 2:
                score += 10000
            elif elements.count(pawn) == 3 and elements.count('*') < 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') == 3:
                score += 500

                # Check for Asecending Diagonal line
    for i in range(4, len(board)):
        for j in range(0, len(board[0]) - 4):
            elements = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3], board[i - 4][j + 4]]
            if elements.count(pawn) == 5:
                score += 100000000
            if elements.count(pawn) == 4 and elements.count('*') == 1:
                score += 50000
            if elements.count(pawn) == 3 and elements.count('*') == 2:
                score += 10000
            elif elements.count(pawn) == 3 and elements.count('*') < 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') == 3:
                score += 500

        # Check for Descending Diagonal line
    for i in range(3, len(board)):
        for j in range(3, len(board[0])):
            elements = [board[i][j], board[i - 1][j - 1], board[i - 2][j - 2], board[i - 3][j - 3] , board[i - 4][j - 4]]
            if elements.count(pawn) == 5:
                score += 100000000
            if elements.count(pawn) == 4 and elements.count('*') == 1:
                score += 50000
            if elements.count(pawn) == 3 and elements.count('*') == 2:
                score += 10000
            elif elements.count(pawn) == 3 and elements.count('*') < 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') == 3:
                score += 500

    if pawn == '1':
        score += opposition_score(board, '2')
    else:
        score += opposition_score(board, '1')

    return score


def minimax(board, depth, maxPlayer):
    """
    inspired by -
    1. https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    2. https://www.youtube.com/watch?v=MMLtza3CZFM&ab_channel=KeithGalli&t=3861s Source Code - https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
    3. https://en.wikipedia.org/wiki/Minimax#Pseudocode
    """
    pos_locations = fetch_possible_columns(board)

    if depth == 0:
        return (None, get_score(board, '2'))
    elif check_victory(board, '2'):
        return (None, 9999999999)
    elif check_victory(board, '1'):
        return (None, -9999999999)

    if maxPlayer:
        val = -math.inf
        column = pos_locations[0]

        for col in pos_locations:
            copy_board = deepcopy(board)
            copy_board = insert_element(copy_board, '2', col)
            latest_score = minimax(copy_board, depth - 1, False)[1]
            if latest_score > val:
                val = latest_score
                column = col
        return column, val

    else:
        val = math.inf
        column = pos_locations[0]
        for col in pos_locations:
            copy_board = deepcopy(board)
            copy_board = insert_element(copy_board, '1', col)
            latest_score = minimax(copy_board, depth - 1, True)[1]
            if latest_score < val:
                val = latest_score
                column = col
        return column, val

def minimax_alpha_beta_prunning(board, depth, alpha, beta, maxPlayer):
    """
    inspired by -
    1. https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    2. https://www.youtube.com/watch?v=MMLtza3CZFM&ab_channel=KeithGalli&t=3861s Source Code - https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
    3. https://en.wikipedia.org/wiki/Minimax#Pseudocode
    """
    pos_locations = fetch_possible_columns(board)

    # Termination Conditions

    if depth == 0:
        return (None, get_score(board, '2'))
    elif check_victory(board, '2'):
        return (None, 9999999999)
    elif check_victory(board, '1'):
        return (None, -9999999999)

    # Maximising Player

    if maxPlayer:
        val = -math.inf
        column = pos_locations[0]

        for col in pos_locations:
            copy_board = deepcopy(board)
            copy_board = insert_element(copy_board, '2', col)
            latest_score = minimax_alpha_beta_prunning(copy_board, depth - 1, alpha, beta, False)[1]
            if latest_score > val:
                val = latest_score
                column = col
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return column, val

    # Minimising Player
    else:
        val = math.inf
        column = pos_locations[0]
        for col in pos_locations:
            copy_board = deepcopy(board)
            copy_board = insert_element(copy_board, '1', col)
            latest_score = minimax_alpha_beta_prunning(copy_board, depth - 1, alpha, beta, True)[1]
            if latest_score < val:
                val = latest_score
                column = col
            beta = min(beta, val)
            if alpha >= beta:
                break
    return column, val

from copy import deepcopy

player_turn = 1

print("**************************************************")
print("***************** Let's Connect! *****************")
print("**************************************************")
game_board = deepcopy(create_board(7, 7))

import random

def simulator(number):
    player_turn = 1
    player_1_victory = 0
    player_2_victory = 0
    draw = 0
    count = 0
    for i in range(0,number):
        print("Game number - ", count)
        count +=1
        game_board = deepcopy(create_board(9, 9))

        while True:
            if player_turn == 1:
                board_printer(game_board)
                player_request0 = input(
                    "Player {} Please enter the Column Number you wish to have your coin \n \n ".format(player_turn))
                player_turn = 2
                possible_columns = fetch_possible_columns(game_board)
                if possible_columns == []:
                    print("\n\n****************************************************")
                    print("********* GAME ENDS IN A DRAW **********************")
                    print("****************************************************")
                    break
                while True:
                    if int(player_request0) in possible_columns:
                        print("You've entered a valid column, inserting the coin to the column {}".format(
                            player_request0))
                        game_board = deepcopy(insert_element(game_board, '1', int(player_request0)))
                        break
                    else:
                        player_request0 = print("Please enter a valid column , the valid columns are - ",
                                                possible_columns)

                if (check_victory(game_board, '1')):
                    print("\n\n****************************************************")
                    print("Player 1 has won the game, Thank you for Playing :) ")
                    print("****************************************************")
                    break

            if player_turn == 2:
                # player_request1 = input("Player {} Please enter the Column Number you wish to have your coin \n \n ".format(player_turn))
                player_turn = 1
                possible_columns = fetch_possible_columns(game_board)
                board_printer(game_board)
                if possible_columns == []:
                    print("\n\n****************************************************")
                    print("********* GAME ENDS IN A DRAW **********************")
                    print("****************************************************")
                    draw+=1
                    break

                move, score = minimax_alpha_beta_prunning(game_board, 3, -math.inf, math.inf, True)

                print("AI 2 has chosen the column -  ", int(move))
                game_board = deepcopy(insert_element(game_board, '2', int(move)))

                if (check_victory(game_board, '2')):
                    board_printer(game_board)
                    print("\n\n****************************************************")
                    print("Player 2 has won the game, Thank you for Playing :) ")
                    print("****************************************************")

                    player_2_victory +=1
                    break
    print("Summary - ")
    print(" Player 1 victory - ",player_1_victory , " Percentage = ", (player_1_victory/(player_1_victory + player_2_victory+draw))*100)
    print(" Player 2 victory - ",player_2_victory , " Percentage = ", (player_2_victory/(player_1_victory + player_2_victory+draw))*100)
    print("Draws - ",draw)

simulator(1)