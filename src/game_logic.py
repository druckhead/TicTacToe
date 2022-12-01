from src.game_turns import Shape


def check_win_row(board: list[list[str]], row: int, len_col: int) -> bool:
    for col in range(len_col - 1):
        if board[row][col] is None:
            return False
        if board[row][col] != board[row][col + 1]:
            return False
    return True


def check_win_rows(board: list[list[str]], num_rows: int) -> bool:
    for row in range(num_rows):
        if check_win_row(board, row, len_col=num_rows) is True:
            return True
    return False


def check_win_col(board: list[list[str]], col: int, len_row: int) -> bool:
    for row in range(len_row - 1):
        if board[row][col] is None:
            return False
        if board[row][col] != board[row + 1][col]:
            return False
    return True


def check_win_cols(board: list[list[str]], num_cols: int) -> bool:
    for col in range(num_cols):
        if check_win_col(board, col, len_row=num_cols) is True:
            return True
    return False


def check_top_left_bottom_right_diagonal_win(board: list[list[str]], num_rows: int) -> bool:
    for row in range(num_rows - 1):
        for col in range(row, row + 1):
            if board[row][col] is None:
                return False
            if board[row][col] != board[row + 1][col + 1]:
                return False
    return True


def check_top_right_bottom_left_diagonal_win(board: list[list[str]], num_rows: int) -> bool:
    for row in range(num_rows - 1, 0, -1):
        for col in range(num_rows - 1 - row, num_rows - row):
            if board[row][col] is None:
                return False
            if board[row][col] != board[row - 1][col + 1]:
                return False
    return True


def check_win_diagonals(board: list[list[str]], num_rows: int) -> bool:
    return check_top_right_bottom_left_diagonal_win(board, num_rows) \
           or check_top_left_bottom_right_diagonal_win(board, num_rows)


def check_win(board: list[list[str]], num_rows: int) -> bool:
    return check_win_rows(board, num_rows) \
           or check_win_cols(board, num_cols=num_rows) \
           or check_win_diagonals(board, num_rows)


# **************************************************************************
#                               GAME STUCK
# **************************************************************************


# row stuck
def row_stuck(board: list[list[str]], row: int, len_board: int):
    if row < len_board:
        if Shape.x.value in board[row] and Shape.o.value in board[row]:
            return True and row_stuck(board, row + 1, len_board)
        else:
            return False
    return True


# all rows stuck
def all_rows_stuck(board: list[list[str]], len_board: int):
    return row_stuck(board, 0, len_board)


def col_stuck(board: list[list[str]], col: int, len_board: int):
    if col < len_board:
        curr_column: list[str] = []
        for row in range(len_board):
            curr_column.append(board[row][col])
        if Shape.x.value in curr_column and Shape.o.value in curr_column:
            return True and col_stuck(board, col + 1, len_board)
        else:
            return False
    return True


def all_cols_stuck(board: list[list[str]], len_board: int):
    return col_stuck(board, 0, len_board)


def tl_br_diag_stuck(board: list[list[str]], len_board: int):
    tl_br_diag: list[str] = []
    for row in range(len_board):
        for col in range(row, row + 1):
            tl_br_diag.append(board[row][col])
    if Shape.x.value in tl_br_diag and Shape.o.value in tl_br_diag:
        return True
    return False


def tr_bl_diag_stuck(board: list[list[str]], len_board: int):
    tr_bl_diag: list[str] = []
    for row in range(len_board - 1, 0, -1):
        for col in range(len_board - 1 - row, len_board - row):
            tr_bl_diag.append(board[row][col])
    if Shape.x.value in tr_bl_diag and Shape.o.value in tr_bl_diag:
        return True
    return False


# driver for game stuck helper funcs
def game_stuck(board: list[list[str]]) -> bool:
    len_board = len(board)
    full_stack = all_rows_stuck(board, len_board) and all_cols_stuck(board, len_board) and \
                 tl_br_diag_stuck(board, len_board) and tr_bl_diag_stuck(board, len_board)
    return full_stack
