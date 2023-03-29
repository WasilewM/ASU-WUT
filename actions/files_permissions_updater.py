from .action_base import ActionBase
from .files_data_collector import FileData
import os


class FilesPermissionsUpdater(ActionBase):
    def __init__(self, expected_permissions: int = 644) -> None:
        self.expected_permissions = expected_permissions
        self.apply_action_to_all = False

    def _ask_for_user_decision(self, file: FileData):
        self._sugest_action_on_files(
            "Do you want to update permissions for following files?",
            file.file_path,
        )

    def _execute_action(self, file: FileData) -> None:
        if file.permissions != self.expected_permissions:
            os.chmod(file.file_path, self._get_octal_permissions())
            print(
                f"File {file.file_path} has been updated to have following "
                + f"permissions: {self.expected_permissions}"
            )

    def _get_octal_permissions(self) -> int:
        return int(str(self.expected_permissions), base=8)
