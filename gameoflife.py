import time
import copy
import os
import sys
sys.argv

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

def init_board(file_path):
    b = []
    if not os.path.isfile(file_path):
        raise Exception(f"File {file_path} could not be found.")
    with open(file_path, mode="r") as file:
        file_content = file.readlines()
    for line in file_content:
        b_line = []
        for cell in line:
            if cell == ALIVE_FORMAT:
                b_line.append(ALIVE)
            elif cell == DEAD_FORMAT:
                b_line.append(DEAD)
            elif cell != ',' and cell !='\n':
                raise Exception(f"File {file_path} is not written according format.")
        b.append(b_line)
    return b


def sum_neighbors(row, col, board):
    
    neighbors_count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i or j: # Don't count current cell 
                if(0 <= row+i < len(board) and 0 <= col+j < len(board[row+i]) and board[row+i][col+j]):
                    neighbors_count += 1
    
    return neighbors_count


def advance_generation(board):
    new_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            surround = sum_neighbors(i,j,board)
            if board[i][j]:
                if not (2 <= surround <= 3):
                    new_board[i][j] = DEAD
            elif surround == 3:
                new_board[i][j] = ALIVE
    return new_board


def print_board(board):
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


def main(args):
    if len(args) != 2:
        print("Please enter 2 arguments\n\t-file path to initial board state\n\t-number of generations")
        exit()
    try:
        board = init_board(args[0])
        generations = int(args[1])
    except ValueError:
        print(f"2nd argument must be a number, '{args[1]}' was entered.")
        exit()
    except Exception as e:
        print(e)
        exit()

    for i in range(generations):
        print_board(board)
        time.sleep(100/1000) # sleep for 100 ms
        board = advance_generation(board)


if __name__ =="__main__":
    main(sys.argv[1:])