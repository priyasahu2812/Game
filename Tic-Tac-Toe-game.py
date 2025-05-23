import os
import time

board = [' ' for _ in range(9)]  # 3x3 board initialized with spaces

def print_board():
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def is_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw():
    return all(space != ' ' for space in board)

def play_game():
    current_player = 'X'

    for turn in range(9):
        print_board()
        move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1

        if board[move] != ' ' or move < 0 or move > 8:
            print("Invalid move. Try again.")
            time.sleep(1)
            continue

        board[move] = current_player

        if is_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            return

        if is_draw():
            print_board()
            print("It's a draw!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print("Game over!")

play_game()
