import math

HUMAN = "X"
AI = "O"


def print_board(board):
    print()
    for i in range(9):
        cell = board[i] if board[i] != " " else str(i + 1)
        print(f" {cell} ", end="")

        if i % 3 != 2:
            print("|", end="")
        else:
            print()

        if i % 3 == 2 and i != 8:
            print("---+---+---")

    print()


def winner(board):
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def game_over(board):
    return winner(board) is not None or " " not in board


def minimax(board, depth, maximizing):
    result = winner(board)

    # AI wins
    if result == AI:
        return 10 - depth

    # Human wins
    if result == HUMAN:
        return depth - 10

    # Draw
    if " " not in board:
        return 0

    if maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = AI

                score = minimax(board, depth + 1, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN

                score = minimax(board, depth + 1, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play():
    board = [" "] * 9

    print("================================")
    print("       TIC-TAC-TOE AI")
    print("================================")
    print("You = X")
    print("AI  = O")

    print_board(board)

    while not game_over(board):

        # -------------------------
        # HUMAN TURN
        # -------------------------
        while True:
            try:
                choice = int(input("Your move (1-9): "))

                if choice < 1 or choice > 9:
                    print("Choose a number from 1 to 9.")
                    continue

                index = choice - 1

                if board[index] != " ":
                    print("That position is already occupied.")
                    continue

                board[index] = HUMAN
                break

            except ValueError:
                print("Please enter a valid number.")

        print_board(board)

        # Check human win
        if winner(board) == HUMAN:
            print("🎉 You win!")
            return

        # Check draw
        if " " not in board:
            print("🤝 Draw!")
            return

        # -------------------------
        # AI TURN
        # -------------------------
        print("AI is thinking...")

        move = best_move(board)

        if move is not None:
            board[move] = AI

        print(f"AI placed O at position {move + 1}")
        print_board(board)

        # Check AI win
        if winner(board) == AI:
            print("🤖 AI wins!")
            return

        # Check draw
        if " " not in board:
            print("🤝 Draw!")
            return


if __name__ == "__main__":
    play()