def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Перевірка рядків
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Перевірка колонок
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Діагоналі
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Хід гравця {current_player}")
        try:
            row = int(input("Введи рядок (1-3): ")) - 1
            col = int(input("Введи колонку (1-3): ")) - 1
        except ValueError:
            print("❌ Введи число!")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("❌ Неправильний хід. Спробуй ще раз.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Гравець {current_player} переміг!")
            break

        if is_full(board):
            print_board(board)
            print("🤝 Нічия!")
            break

        # Зміна гравця
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
