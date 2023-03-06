import time
import copy
import os
import argparse

ALIVE_FORMAT = '*'
DEAD_FORMAT = ' '
ALIVE = 1
DEAD = 0

MSG = '''
   _____                         ____   __   _      _  __     
  / ____|                       / __ \ / _| | |    (_)/ _|    
 | |  __  __ _ _ __ ___   ___  | |  | | |_  | |     _| |_ ___ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | |  _| | |    | |  _/ _ \\
 | |__| | (_| | | | | | |  __/ | |__| | |   | |____| | ||  __/
  \_____|\__,_|_| |_| |_|\___|  \____/|_|   |______|_|_| \___|
                                                              
                                                              '''

def init_board(file_path : str) ->list:
    '''
    Function initializes a board sccording to the content in file.
    Input: file path.
    Output: initialized board.
    '''
    board = []
    if not os.path.isfile(file_path):
        raise Exception(f"File {file_path} could not be found.")
    with open(file_path, mode="r") as file:
        file_content = file.readlines()
    for line in file_content:
        board_line = []
        for cell in line:
            if cell == ALIVE_FORMAT:
                board_line.append(ALIVE)
            elif cell == DEAD_FORMAT:
                board_line.append(DEAD)
            elif cell != ',' and cell !='\n':
                raise Exception(f"File {file_path} is not written according format.")
        board.append(board_line)
    return board


def sum_neighbors(row : int, col : int, board : list) ->int:
    '''
    Function counts the alive neighbors around the wanted cell in the board.
    Input: the wanted call location in board, board.
    Output: the number of alive cells around the wanted cell.
    '''
    
    neighbors_count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i or j: # Don't count current cell 
                if 0 <= row+i < len(board) and 0 <= col+j < len(board[row+i]):
                    neighbors_count += board[row+i][col+j]
    
    return neighbors_count


def advance_generation(board : list) ->list:
    '''
    Function advances the board 1 generation.
    Input: the board in the current generation.
    Output: the board in the new generation.
    '''
    new_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            alive_neighbors = sum_neighbors(i,j,board)
            if board[i][j]:
                if not 2 <= alive_neighbors <= 3:
                    new_board[i][j] = DEAD
            elif alive_neighbors == 3:
                new_board[i][j] = ALIVE
    return new_board


def print_board(board : list) ->None:
    '''
    Function clears all current output and prints a board of cells according to format.
    Input: board to print.
    Output: none
    '''
    os.system('clear')
    print(MSG)
    for line in board:
        print('\t\t    |', end='')
        for cell in line:
            if cell:
                print(f' {ALIVE_FORMAT} ', end='');
            else:
                print(f' {DEAD_FORMAT} ', end='');
        print('|')


def main(args : argparse.Namespace) ->None:
    try:
        board = init_board(args.file_path)
    except Exception as e:
        print(e)
        exit()

    generations = int(args.generations)
    
    for i in range(generations):
        print_board(board)
        time.sleep(100/1000) # sleep for 100 ms
        board = advance_generation(board)


if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="the file path to the initial board state.")
    parser.add_argument("generations", type=int, help="the number of generations to present.")
    args = parser.parse_args()
    print(type(args))
    main(args)
