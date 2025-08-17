from sys import argv
from state_management.state_management import reset_game_info, setup_board, make_move
from utils.file_reader import read_info_file

def play_game():
    print("Starting the game...")
    reset_game_info()

    print("Game setup...")
    setup_board()

    while True:
        next_move = input('Enter next move: ')

        if next_move in ['exit', 'quit']:
            print("Exiting the game.")
            break

        make_move()


if __name__ == "__main__":
    cell_list, player_clues = read_info_file()

    if len(argv) > 1 and argv[1] in ['reset', 'setup']:
        reset_game_info()
        exit
    
    if len(argv) > 1 and argv[1] == 'play':
        play_game()
        exit