from .action_base_io import ActionBaseIO
from .files_data_collector import FileData
import os


class FilesPermissionsUpdater(ActionBaseIO):
    def __init__(self, files: list, expected_permissions: int = 644) -> None:
        self.files = files
        self.expected_permissions = expected_permissions

    def update_files_permissions(self) -> None:
        self._sugest_action_on_files(
            "Do you want to update permissions for following files?",
            self.files,
        )
        user_answer = self._has_user_accepted_the_action()
        if user_answer:
            for file in self.files:
                if file.permissions != self.expected_permissions:
                    self._update_file_permissions(file)

    def _update_file_permissions(self, file: FileData) -> None:
        os.chmod(file.file_path, self._get_octal_permissions())
        print(
            f"File {file.file_path} has been updated to have following "
            + f"permissions: {self.expected_permissions}"
        )

    def _get_octal_permissions(self) -> int:
        return int(str(self.expected_permissions), base=8)
