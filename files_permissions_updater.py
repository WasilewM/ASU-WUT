class FilesPermissionsUpdater:
    def __init__(
        self, root_dir: str = ".", expected_files_permissions: int = 0o777
    ) -> None:
        self.root = root_dir
        self.expected_files_permissions = expected_files_permissions

    def update_files_permissions(self) -> None:
        pass
