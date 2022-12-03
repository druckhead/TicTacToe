from src.game_turns import Shape, toggle_shape
from copy import deepcopy


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

def stuck(board: list[list[str]], len_board: int, curr_shape: str) -> int:
    count = 0
    for row in range(len_board):
        for col in range(len_board):
            next_turn_board = deepcopy(board)
            if next_turn_board[row][col] is None:
                next_turn_board[row][col] = curr_shape
                if check_win(next_turn_board, len_board):
                    count += 1
                    continue
    return count


# driver for game stuck helper funcs
def game_stuck(board: list[list[str]], len_board: int, curr_shape: str) -> bool:
    # assumes no "stupid" moves are made
    next_shape = toggle_shape(curr_shape)
    if stuck(board, len_board, curr_shape) >= 2:
        return False
    if stuck(board, len_board, next_shape) >= 1:
        return False
    return True
