def main():
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]

    active_player_index = 0
    players = ["player_1", "player_2"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    show_header()

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        show_board(board)

        if not select_token_position(board, player, symbol):
            print()
            print("Invalid position, choose another column")
            continue

        active_player_index = (active_player_index + 1) % len(players)

    print(f"GAME OVER!, winner is {player}, has won with the board:")
    show_board(board)


def show_header():
    print("---------------------")
    print("WELCOME TO CONNNECT4")
    print("---------------------")


def show_board(board):
    for row in board:
        print("| ", end="")
        for cell in row:
            cell = cell if cell is not None else "_"
            print(cell, end=" | ")
        print()


def select_token_position(board, active_player, symbol):
    token_text = input(f"It's {active_player}'s turn. Select the column where you want to put the token:")
    token = int(token_text) - 1

    if token < 0 or token >= len(board[0]):
        return False

    if not check_empty_place(board, token, symbol):
        return False

    return True


def check_empty_place(board, token, symbol):
    for row in reversed(board):
        if not row[token]:
            row[token] = symbol
            return True
        elif check_column_full(board, token, symbol):
            return False


def check_column_full(board, token, symbol):
    column = []
    for row in reversed(board):
        column.append(row[token])

    if all(cell == symbol for cell in column):
        return True


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol = cells[0]
        if symbol and all(symbol == cell for cell in cells):
            return True


def get_winning_sequences(board):
    sequences = []

    # rows
    sequences.extend(get_sequences_of_four_cells(board))

    # columns
    columns = []
    for col_idx in range(0, 7):
        column = []
        for n in range(0, 6):
            column.append(board[n][col_idx])
        columns.append(column)

    sequences.extend(get_sequences_of_four_cells(columns))

    # diagonals
    diagonals = [
        [board[2][0], board[3][1], board[4][2], board[5][3]],
        [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]],
        [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]],
        [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5], board[5][6]],
        [board[0][2], board[1][3], board[2][4], board[3][5], board[4][6]],
        [board[0][3], board[1][4], board[2][5], board[3][6]],
        [board[0][3], board[1][2], board[2][1], board[3][0]],
        [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]],
        [board[0][5], board[1][4], board[2][3], board[3][2], board[4][1], board[5][0]],
        [board[0][6], board[1][5], board[2][4], board[3][3], board[4][2], board[5][1]],
        [board[1][6], board[2][5], board[3][4], board[4][3], board[5][2]],
        [board[2][6], board[3][5], board[4][4], board[5][3]],
    ]

    sequences.extend(get_sequences_of_four_cells(diagonals))

    return sequences


def get_sequences_of_four_cells(rows):
    sequences = []

    for row in rows:
        cells_4 = []
        for n in range(0, len(row) - 3):
            for i in range(n, n + 4):
                cells_4.append(row[i])
                if len(cells_4) == 4:
                    sequences.append(cells_4)
                    cells_4 = []

    return sequences


if __name__ == '__main__':
    main()
