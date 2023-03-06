import os

class FileReader:
    def __init__(self, file_path : str) -> None:
        if not os.path.isfile(file_path):
            raise Exception(f"File {file_path} could not be found.")
        self.__file_path = file_path
    
    def read_lines(self) -> str:
        with open(self.__file_path, mode="r") as file:
            content = file.readlines()
        return content