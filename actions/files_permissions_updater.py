from .action_base_io import ActionBaseIO, UserActionAnswerEnum
from .files_data_collector import FileData
import os


class FilesPermissionsUpdater(ActionBaseIO):
    def __init__(self, files: list, expected_permissions: int = 644) -> None:
        self.files = files
        self.expected_permissions = expected_permissions
        self.apply_action_to_all = False

    def update_files_permissions(self) -> None:
        for file in self.files:
            if not self.apply_action_to_all:
                self._handle_individual_file_permissions_update(file)
            else:
                self._update_file_permissions(file)

    def _handle_individual_file_permissions_update(self, file: FileData):
        self._sugest_action_on_files(
            "Do you want to update permissions for following files?",
            file.file_path,
        )
        user_answer = self._has_user_accepted_the_action()
        if user_answer == UserActionAnswerEnum.YES:
            self._update_file_permissions(file)
        elif user_answer == UserActionAnswerEnum.APPLY_TO_ALL:
            self.apply_action_to_all = True
            self._update_file_permissions(file)

    def _update_file_permissions(self, file: FileData) -> None:
        if file.permissions != self.expected_permissions:
            os.chmod(file.file_path, self._get_octal_permissions())
            print(
                f"File {file.file_path} has been updated to have following "
                + f"permissions: {self.expected_permissions}"
            )

    def _get_octal_permissions(self) -> int:
        return int(str(self.expected_permissions), base=8)
