from .action_base import ActionBase
from .files_data_collector import FileData
import os


class FilesRemover(ActionBase):
    def _ask_for_user_decision(self, file: FileData):
        self._sugest_action_on_files(
            "Do you want to delete following file?", file.file_path
        )

    def _execute_action(self, file: FileData):
        os.remove(file.file_path)
        print(f"{file.file_path} has been removed")
