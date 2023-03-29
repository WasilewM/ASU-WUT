from .action_base import ActionBase
from .files_data_collector import FileData
import os


class FilesRenamer(ActionBase):
    def __init__(self, unwanted_chars: list, replacement_char: str) -> None:
        self.unwanted_chars = unwanted_chars
        self.replacement_char = replacement_char
        super().__init__()

    def _ask_for_user_decision(self, file: FileData):
        self._sugest_action_on_files(
            "Do you want to rename following file?", file.file_path
        )

    def _execute_action(self, file: FileData):
        dirs, file_name = os.path.split(file.file_path)
        new_file_name, file_extension = os.path.splitext(file_name)
        for c in self.unwanted_chars:
            if c in new_file_name:
                new_file_name = new_file_name.replace(c, self.replacement_char)
        new_file_name += file_extension
        new_file_path = os.path.join(dirs, new_file_name)
        os.rename(file.file_path, new_file_path)
        print(f"File {file.file_path} has been renamed to {new_file_path}")
