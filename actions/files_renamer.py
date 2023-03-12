import os


class FilesRenamer:
    def __init__(
        self, unwanted_chars: list, replacement_char: str, files: list
    ) -> None:
        self.unwanted_chars = unwanted_chars
        self.replacement_char = replacement_char
        self.files = files

    def replace_unwanted_chars(self) -> None:
        for file in self.files:
            dirs, file_name = os.path.split(file.file_path)
            (
                new_file_name,
                file_extension,
            ) = self._separate_file_name_from_extension(file_name)
            for c in self.unwanted_chars:
                if c in new_file_name:
                    new_file_name = new_file_name.replace(
                        c, self.replacement_char
                    )
            new_file_name += file_extension
            new_file_path = os.path.join(dirs, new_file_name)
            os.rename(file.file_path, new_file_path)
            print(f"File {file.file_path} has been renamed to {new_file_path}")

    def _separate_file_name_from_extension(self, file_name: str) -> tuple:
        idx = len(file_name) - 1
        while idx >= 0 and file_name[idx] != ".":
            idx -= 1

        return file_name[:idx], file_name[idx:]
