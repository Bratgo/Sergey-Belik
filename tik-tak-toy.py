def display_board(board):
    for row in board:
        print(" | ".join(row))
        print('__________')


def check_winner(board):
    # Проверка выигрышных комбинаций по строкам, столбцам и диагоналям
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    game_over = False

    while not game_over:
        display_board(board)
        print("Ход игрока", current_player)
        row = int(input("Выберите строку (1-3): ")) - 1
        col = int(input("Выберите столбец (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                display_board(board)
                print("Победитель:", winner)
                game_over = True
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                display_board(board)
                print("Ничья!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Недопустимый ход. Попробуйте снова.")


play_game()
