from game_logic import check_win, game_stuck
from game_board import get_board_size, initialize_board, display_current_board
from game_turns import display_turn_prompt, get_user_turn, update_board_with_turn, toggle_turn, toggle_shape, Turn, \
    Shape, random_start_player
from os import system


def print_greeting() -> None:
    greeting_msg = """
 _______       ___      .__   __.  __   _______  __              ___      .__   __.  _______      ________   __  ____    ____  __     _______.
|       \\     /   \\     |  \\ |  | |  | |   ____||  |            /   \\     |  \\ |  | |       \\    |       /  |  | \\   \\  /   / (_ )   /       |
|  .--.  |   /  ^  \\    |   \\|  | |  | |  |__   |  |           /  ^  \\    |   \\|  | |  .--.  |   `---/  /   |  |  \\   \\/   /   |/   |   (----`
|  |  |  |  /  /_\\  \\   |  . `  | |  | |   __|  |  |          /  /_\\  \\   |  . `  | |  |  |  |      /  /    |  |   \\      /          \\   \\    
|  '--'  | /  _____  \\  |  |\\   | |  | |  |____ |  `----.    /  _____  \\  |  |\\   | |  '--'  |     /  /----.|  |    \\    /       .----)   |   
|_______/ /__/     \\__\\ |__| \\__| |__| |_______||_______|   /__/     \\__\\ |__| \\__| |_______/     /________||__|     \\__/        |_______/    
                     .___________. __    ______ .___________.    ___       ______ .___________.  ______    _______                            
                     |           ||  |  /      ||           |   /   \\     /      ||           | /  __  \\  |   ____|                           
                     `---|  |----`|  | |  ,----'`---|  |----`  /  ^  \\   |  ,----'`---|  |----`|  |  |  | |  |__                              
                         |  |     |  | |  |         |  |      /  /_\\  \\  |  |         |  |     |  |  |  | |   __|                             
                         |  |     |  | |  `----.    |  |     /  _____  \\ |  `----.    |  |     |  `--'  | |  |____                            
                         |__|     |__|  \\______|    |__|    /__/     \\__\\ \\______|    |__|      \\______/  |_______|                           
                                          .___  ___.      ___      .__   __.  __       ___                                                    
                                          |   \\/   |     /   \\     |  \\ |  | |  |     /   \\                                                   
                                          |  \\  /  |    /  ^  \\    |   \\|  | |  |    /  ^  \\                                                  
                                          |  |\\/|  |   /  /_\\  \\   |  . `  | |  |   /  /_\\  \\                                                 
                                          |  |  |  |  /  _____  \\  |  |\\   | |  |  /  _____  \\                                                
                                          |__|  |__| /__/     \\__\\ |__| \\__| |__| /__/     \\__\\"""

    print(greeting_msg)
    print()
    return


def start_game() -> bool:
    game_over: bool = False
    num_turns: int = 0

    size = get_board_size()
    board = initialize_board(size)
    system("clear")
    display_current_board(board)
    turn, shape = random_start_player()

    while not game_over:
        display_turn_prompt(turn, shape)
        row, col = get_user_turn(size)
        while board[row][col] == Shape.x.value or board[row][col] == Shape.o.value:
            system("clear")
            display_current_board(board)
            print("Error: Cell already taken. Please choose an available cell.\n")
            display_turn_prompt(turn, shape)
            row, col = get_user_turn(size)
        update_board_with_turn(board, row, col, shape)
        num_turns += 1
        system("clear")
        display_current_board(board)

        if num_turns >= 2 * size - 1:
            if check_win(board, size):
                game_over = True
                winner = "Player 1" if turn == Turn.player1 else "Player 2"
                print(f"The winner is: {winner}")
            elif game_stuck(board):
                game_over = True

        turn = toggle_turn(turn)
        shape = toggle_shape(shape)

    return True
