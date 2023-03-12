import os


class EmptyFilesFinder:
    def __init__(self, files: list) -> None:
        self.files = files

    def find_files(self) -> list:
        return [
            file for file in self.files if os.path.getsize(file.file_path) == 0
        ]
