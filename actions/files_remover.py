from action_base_io import ActionBaseIO
import os


class FilesRemover(ActionBaseIO):
    def __init__(self, files: list) -> None:
        self.files = files

    def remove_files(self) -> None:
        self._sugest_action_on_files(
            "Do you want to delete following files?", self.files
        )
        user_answer = self._has_user_accepted_the_action()
        if user_answer:
            self._delete_files(self.files)

    def _delete_files(self, files: list) -> None:
        for file in files:
            os.remove(file.file_path)
            print(f"{file.file_path} has been removed")
