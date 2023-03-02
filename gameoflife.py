import os.path
import sys
sys.argv

ALIVE = '*'
DEAD = ' '

def init_board(file_path):
    b = []
    if not os.path.isfile(file_path):
        raise Exception(f"File {file_path} could not be found.")
    with open(file_path, mode="r") as file:
        file_content = file.readlines()
    for line in file_content:
        b_line = []
        for cell in line:
            if cell == ALIVE:
                b_line.append(1)
            elif cell == DEAD:
                b_line.append(0)
            elif cell != ',' and cell !='\n':
                raise Exception(f"File {file_path} is not written according format.")
        b.append(b_line)
    return b


def life_circle(board):
    pass

def print_board(board):
    print(end="\r")
    for line in board:
        print('|', end='')
        for cell in line:
            if cell:
                print(' * ', end='');
            else:
                print('   ', end='');
        print('|')
        

def main(args):
    if len(args) != 2:
        print("Please enter 2 arguments\n\t-file path to initial board state\n\t-number of lives")
        exit()
    try:
        board = init_board(args[0])
        life = int(args[1])
    except ValueError:
        print(f"2nd argument must be a number, '{args[1]}' was entered.")
        exit()
    except Exception as e:
        print(e)
        exit()

    for i in range(life):
        board = life_circle(board)
        print_board(board)

if __name__ =="__main__":
    main(sys.argv[1:])