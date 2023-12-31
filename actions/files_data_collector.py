import os
import hashlib


class FileData:
    def __init__(
        self,
        file_path: str,
        md5_hash: str,
        permissions: int,
        creation_timestamp: float,
    ) -> None:
        self.file_path = file_path
        self.md5_hash = md5_hash
        self.permissions = permissions
        self.creation_timestamp = creation_timestamp

    def __repr__(self):
        description = f"file_path: {self.file_path}, "
        description += f"md5_hash: {self.md5_hash}, "
        description += f"permissions: {self.permissions}, "
        description += f"creation_timestamp: {self.creation_timestamp}"
        return description


class FilesDataCollector:
    def __init__(
        self, root_dir: str = ".", files_encoding_format: str = "UTF-8"
    ) -> None:
        self.root = root_dir
        self.files_encoding_format = files_encoding_format

    def get_files_data(self) -> list:
        return self._find_files(self.root)

    def _find_files(self, root_dir: str) -> list:
        files = []
        for f in os.listdir(root_dir):
            file_path = os.path.join(root_dir, f)
            if os.path.isfile(file_path):
                self._handle_file(files, file_path)
            elif os.path.isdir(file_path):
                self._handle_dir(files, file_path)
            else:
                self._handle_unknown_obj(file_path)
        return files

    def _handle_file(self, files: list, file_path: str) -> None:
        md5_hash = self._get_file_md5_hash(file_path)
        permissions = self._get_file_permissions(file_path)
        creation_timestamp = self._get_file_creation_timestamp(file_path)
        files.append(
            FileData(file_path, md5_hash, permissions, creation_timestamp)
        )

    def _get_file_md5_hash(self, file_path: str) -> str:
        try:
            with open(file_path, "r") as file_handle:
                encoded_file = file_handle.read().encode(
                    self.files_encoding_format
                )
                return hashlib.md5(encoded_file).hexdigest()
        except Exception as e:
            print(f"An error occurred while processing file {file_path}: {e}")
            exit(1)

    def _get_file_permissions(self, file_path: str) -> int:
        try:
            return int(oct(os.stat(file_path).st_mode)[-3:])
        except Exception as e:
            print(f"An error occurred while processing file {file_path}: {e}")
            exit(1)

    def _get_file_creation_timestamp(self, file_path: str) -> float:
        return os.stat(file_path).st_ctime

    def _handle_dir(self, files: list, file_path: str) -> None:
        subdir_files = self._find_files(file_path)
        subdir_files = subdir_files if subdir_files else []
        files += subdir_files

    def _handle_unknown_obj(self, file_path: str):
        print(f"Object {file_path} could not be recognised.")
        exit(1)
