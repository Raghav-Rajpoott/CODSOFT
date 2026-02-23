def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Tic Tac Toe AI Game")
    print("Positions are numbered 1 to 9\n")

    while True:
        print_board(board)

        move = input(f"Player {current_player}, enter position (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input! Try again.")
            continue

        move = int(move) - 1

        if board[move] != " ":
            print("Position already taken! Try again.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()