import re


class TemporaryFilesFinder:
    def __init__(self, files: list, tmp_files_re: str) -> None:
        self.files = files
        self.tmp_files_re = re.compile(tmp_files_re)

    def find_files(self) -> list:
        return [
            file
            for file in self.files
            if self.tmp_files_re.match(file.file_path)
        ]
