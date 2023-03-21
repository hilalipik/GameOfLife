import os

def read_lines(file_path : str) -> list[str]:
    '''
    Reads lines from wanted file, may raise an error if file doesn't exist.
    Input: file path.
    Output: a list of the lines read fron file.
    '''
    if not os.path.isfile(file_path):
        raise Exception(f"File {file_path} could not be found.")
    with open(file_path, mode="r") as file:
        content = file.readlines()
    return content
