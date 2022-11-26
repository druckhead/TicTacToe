def get_board_size() -> int:
    size = int(input('> X/O: Enter your board size (ex: 3 for 3 rows & 3 columns): '))
    return size


def initialize_board(size: int) -> list[list[None]]:
    board: list[list[None]] = list()
    for row in range(size):
        board.append([])
        for col in range(size):
            board[row].append(None)
    return board


# For 3*3 - 7 rows, 13 chars
# For 1 row add - 2 rows, 4 chars
# For 1 col add, 0 rows, 4 chars
def pprint_board(board: list[list[str]]) -> str:
    board_str = ""
    len_board = len(board[0])
    for row in range(len_board):
        board_str += f'{"-" * (len_board * 4 + 1)}\n'
        for col in range(len_board):
            shape = " " if board[row][col] is None else board[row][col]
            board_str += f"| {shape} "
        board_str += "|\n"
    board_str += f'{"-" * (len_board * 4 + 1)}\n'
    return board_str


# def display_current_board(board: list[list[str]]) -> None:
#     pass
