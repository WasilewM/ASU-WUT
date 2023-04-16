from .action_base import ActionBase
from .files_data_collector import FileData
import os
import shutil


class FilesRelocator(ActionBase):
    def __init__(self, new_dir: str) -> None:
        self.new_dir = new_dir
        super().__init__()

    def _ask_for_user_decision(self, file: FileData):
        self._sugest_action_on_files(
            "Do you want to relocate following file?", file.file_path
        )

    def _execute_action(self, file: FileData) -> None:
        file_name = os.path.split(file.file_path)[-1]
        new_file_path = os.path.join(self.new_dir, file_name)
        shutil.move(file.file_path, new_file_path)
        print(f"File {file.file_path} has been relocated to {new_file_path}")
