from copy import deepcopy


def board_printer(board):
    for row in board:
        print(row)


def create_board(m, n):
    game_board = [["*" for i in range(m)] for j in range(n)]
    # print(game_board)
    #board_printer(game_board)
    return game_board


def transpose_matrix(board):
    # print([[row[i] for row in board] for i in range(len(board[0]))])
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
        #print("Score for move - ", move, " from ", player, " is ", score)

        if score > highest_score:
            highest_score = score
            move_with_highest_score = move

    return move_with_highest_score


def opposition_score(board, pawn):
    opp_score = 0
    for i in range(0, len(board) - 3):
        for j in range(0, len(board[0])):
            elements = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]]
            if elements.count(pawn) == 4:
                opp_score -= 10000000

    # Check for horizontal line

    for j in range(0, len(board[0]) - 3):
        for i in range(0, len(board)):
            # print(i,j)
            elements = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3]]
            if elements.count(pawn) == 4:
                opp_score -= 10000000

        # Check for Asecending Diagonal line
    for i in range(3, len(board)):
        for j in range(0, len(board[0]) - 3):
            elements = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]]
            if elements.count(pawn) == 4:
                opp_score -= 10000000

        # Check for Descending Diagonal line
    for i in range(3, len(board)):
        for j in range(3, len(board[0])):
            elements = [board[i][j], board[i - 1][j - 1], board[i - 2][j - 2], board[i - 3][j - 3]]
            if elements.count(pawn) == 4:
                opp_score -= 10000000

    return opp_score

def get_score(board, pawn):
    # Check for vertical line
    score = 0
    for i in range(0, len(board) - 3):
        for j in range(0, len(board[0])):
            elements = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]]
            if elements.count(pawn) == 4:
                score += 100000000

            if elements.count(pawn) == 3 and elements.count('*') == 1:
                score += 100000
            if elements.count(pawn) == 2 and elements.count('*') == 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') < 2:
                score += 100
            elif elements.count(pawn) == 1 and elements.count('*') == 3:
                score += 50

                # Check for horizontal line

    for j in range(0, len(board[0]) - 3):
        for i in range(0, len(board)):
            # print(i,j)
            elements = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3]]
            if elements.count(pawn) == 4:
                score += 100000000
            if elements.count(pawn) == 3 and elements.count('*') == 1:
                score += 100000
            if elements.count(pawn) == 2 and elements.count('*') == 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') < 2:
                score += 100
            elif elements.count(pawn) == 1 and elements.count('*') == 3:
                score += 50

                # Check for Asecending Diagonal line
    for i in range(3, len(board)):
        for j in range(0, len(board[0]) - 3):
            elements = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]]
            if elements.count(pawn) == 4:
                score += 100000000
            if elements.count(pawn) == 3 and elements.count('*') == 1:
                score += 50000
            elif elements.count(pawn) == 2 and elements.count('*') < 2:
                score += 100
            elif elements.count(pawn) == 1 and elements.count('*') == 3:
                score += 50

        # Check for Descending Diagonal line
    for i in range(3, len(board)):
        for j in range(3, len(board[0])):
            elements = [board[i][j], board[i - 1][j - 1], board[i - 2][j - 2], board[i - 3][j - 3]]
            if elements.count(pawn) == 4:
                score += 100000000
            if elements.count(pawn) == 3 and elements.count('*') == 1:
                score += 50000
            if elements.count(pawn) == 2 and elements.count('*') == 2:
                score += 1000
            elif elements.count(pawn) == 2 and elements.count('*') < 2:
                score += 100
            elif elements.count(pawn) == 1 and elements.count('*') == 3:
                score += 50

    if pawn == '1':
        score += opposition_score(board, '2')
    else:
        score += opposition_score(board, '1')

    return score


from copy import deepcopy



print("**************************************************")
print("***************** Let's Connect! *****************")
print("**************************************************")


import random

def simulator(number):
    player_turn = 1
    player_1_victory = 0
    player_2_victory = 0
    draw = 0
    for i in range(0,number):
        game_board = deepcopy(create_board(7, 7))
        while True:
            if player_turn == 1:

                player_turn = 2
                possible_columns = fetch_possible_columns(game_board)
                if possible_columns == []:
                    print("\n\n****************************************************")
                    print("********* GAME ENDS IN A DRAW **********************")
                    print("****************************************************")
                    draw += 1
                    break

                move = random.choice(possible_columns)
                print("AI 1 has chosen the column -  ", int(move))
                game_board = deepcopy(insert_element(game_board, '1', int(move)))

            if (check_victory(game_board, '1')):
                print("\n\n****************************************************")
                print("Player 1 has won the game, Thank you for Playing :) ")
                print("****************************************************")
                player_1_victory += 1
                break

            if player_turn == 2:
                # player_request1 = input("Player {} Please enter the Column Number you wish to have your coin \n \n ".format(player_turn))
                player_turn = 1
                possible_columns = fetch_possible_columns(game_board)
                if possible_columns == []:
                    print("\n\n****************************************************")
                    print("********* GAME ENDS IN A DRAW **********************")
                    print("****************************************************")
                    break

                move = get_best_move(game_board, possible_columns, '2')

                print("AI 2 has chosen the column -  ", int(move))
                game_board = deepcopy(insert_element(game_board, '2', int(move)))

                if (check_victory(game_board, '2')):
                    print("\n\n****************************************************")
                    print("Player 2 has won the game, Thank you for Playing :) ")
                    print("****************************************************")
                    player_2_victory += 1
                    break

    print("Summary - ")
    print(" Player 1 victory - ",player_1_victory , " Percentage = ", (player_1_victory/(player_1_victory + player_2_victory+draw))*100)
    print(" Player 2 victory - ",player_2_victory , " Percentage = ", (player_2_victory/(player_1_victory + player_2_victory+draw))*100)
    print("Draws - ",draw)

simulator(100000)