import re


class TemporaryFilesFinder:
    def __init__(self, files: list, tmp_files_re: list) -> None:
        self.files = files
        self.tmp_file_formats_re = [
            re.compile(tmp_format_re) for tmp_format_re in tmp_files_re
        ]

    def find_files(self) -> list:
        tmp_files = []
        for tmp_format_re in self.tmp_file_formats_re:
            for file in self.files:
                if (
                    tmp_format_re.match(file.file_path)
                    and file not in tmp_files
                ):
                    tmp_files.append(file)
        return tmp_files
