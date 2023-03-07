import os

def read_lines(file_path) -> str:
    if not os.path.isfile(file_path):
        raise Exception(f"File {file_path} could not be found.")
    with open(file_path, mode="r") as file:
        content = file.readlines()
    return content