class FileData:
    def __init__(
        self, file_path: str, md5_hash: str, permissions: str
    ) -> None:
        self.file_path = file_path
        self.md5_hash = md5_hash
        self.permissions = permissions

    def __repr__(self):
        description = f"file_path: {self.file_path}, "
        description += f"md5_hash: {self.md5_hash}, "
        description += f"permissions: {self.permissions}"
        return description
