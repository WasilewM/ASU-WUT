from .action_base_io import ActionBaseIO, UserActionAnswerEnum
from .files_data_collector import FileData
import os


class FilesRemover(ActionBaseIO):
    def __init__(self, files: list) -> None:
        self.files = files
        self.apply_action_to_all = False

    def remove_files(self) -> None:
        for file in self.files:
            if not self.apply_action_to_all:
                self._handle_individual_files_removal(file)
            else:
                self._remove_file(file)

    def _handle_individual_files_removal(self, file: FileData):
        self._sugest_action_on_files(
            "Do you want to delete following file?", file.file_path
        )
        user_answer = self._has_user_accepted_the_action()
        if user_answer == UserActionAnswerEnum.YES:
            self._remove_file(file)
        elif user_answer == UserActionAnswerEnum.APPLY_TO_ALL:
            self.apply_action_to_all = True
            self._remove_file(file)

    def _remove_file(self, file: FileData):
        os.remove(file.file_path)
        print(f"{file.file_path} has been removed")
