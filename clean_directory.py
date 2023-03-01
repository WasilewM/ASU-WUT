import os
import sys
import hashlib


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
        files.append(FileData(file_path, md5_hash, permissions))

    def _get_file_md5_hash(self, file_path: str):
        try:
            with open(file_path, "r") as file_handle:
                encoded_file = file_handle.read().encode(
                    self.files_encoding_format
                )
                return hashlib.md5(encoded_file).hexdigest()
        except Exception as e:
            print(f"An error occurred while processing file {file_path}: {e}")

    def _get_file_permissions(self, file_path: str) -> int:
        try:
            return os.stat(file_path).st_mode
        except Exception as e:
            print(f"An error occurred while processing file {file_path}: {e}")

    def _handle_dir(self, files: list, file_path: str):
        subdir_files = self._find_files(file_path)
        subdir_files = subdir_files if subdir_files else []
        files += subdir_files

    def _handle_unknown_obj(self, file_path: str):
        print(f"Object {file_path} could not be recognised.")
        exit(1)


class Md5FilesOrganizer:
    def __init__(
        self, root_dir: str = ".", files_encoding_format: str = "UTF-8"
    ) -> None:
        self.root = root_dir
        self.files_encoding_format = files_encoding_format

    def organize_files(self, root_dir: str = None) -> dict:
        root_dir = root_dir if root_dir else self.root
        files_by_md5 = dict()
        self._handle_files(root_dir, files_by_md5)
        return files_by_md5

    def _handle_files(self, root_dir: str, files_by_md5: dict) -> None:
        for f in os.listdir(root_dir):
            file_path = os.path.join(root_dir, f)
            if os.path.isfile(file_path):
                self._handle_single_file(files_by_md5, file_path)
            elif os.path.isdir(file_path):
                self._handle_single_dir(files_by_md5, file_path)
            else:
                self._handle_unknown_obj(file_path)

    def _handle_single_file(self, files_by_md5: dict, file_path: str):
        with open(file_path, "r") as file_handle:
            encoded_file = file_handle.read().encode(
                self.files_encoding_format
            )
            md5_hash = hashlib.md5(encoded_file).hexdigest()
            self._update_files_by_md5_dict(files_by_md5, file_path, md5_hash)

    def _handle_single_dir(self, files_by_md5: dict, file_path: str):
        subdir_files_by_md5 = self.organize_files(file_path)
        for md5_hash in subdir_files_by_md5:
            for md5_hash_file_path in subdir_files_by_md5[md5_hash]:
                self._update_files_by_md5_dict(
                    files_by_md5, md5_hash_file_path, md5_hash
                )

    def _handle_unknown_obj(self, file_path: str):
        print(f"Object {file_path} could not be recognised.")
        exit(1)

    def _update_files_by_md5_dict(
        self, files_by_md5: dict, file_path: str, md5_hash: str
    ):
        if md5_hash not in files_by_md5.keys():
            files_by_md5[md5_hash] = []
        files_by_md5[md5_hash].append(file_path)


class EmptyFilesRemover:
    def __init__(self, root_dir: str = ".") -> None:
        self.root = root_dir

    def remove_files(self):
        files = self._find_files(self.root)
        self._suggest_files_removal(files)
        user_answer = self._has_user_accepted_file_removal()
        if user_answer:
            self._delete_files(files)

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

    def _handle_file(self, files: list, file_path: str):
        if os.path.getsize(file_path) == 0:
            files.append(file_path)

    def _handle_dir(self, files: list, file_path: str):
        subdir_files = self._find_files(file_path)
        subdir_files = subdir_files if subdir_files else []
        files += subdir_files

    def _handle_unknown_obj(self, file_path: str):
        print(f"Object {file_path} could not be recognised.")
        exit(1)

    def _suggest_files_removal(self, files: list) -> None:
        print("Do you want to delete following empty files?")
        for file_path in files:
            print(file_path)
        print("Y/N?")

    def _has_user_accepted_file_removal(self) -> bool:
        user_answer = input()
        if user_answer in ("y", "Y"):
            return True
        elif user_answer in ("n", "N"):
            return False
        else:
            print("Invalid option. Aborting the script...")
            exit(1)

    def _delete_files(self, files: list) -> None:
        for file_path in files:
            os.remove(file_path)
            print(f"{file_path} has been removed")


class FilesPermissionsUpdater:
    def __init__(
        self, root_dir: str = ".", expected_files_permissions: int = 0o777
    ) -> None:
        self.root = root_dir
        self.expected_files_permissions = expected_files_permissions

    def update_files_permissions(self) -> None:
        pass


def run(args: list) -> int:
    print("CWD: ", os.getcwd())

    if len(args) != 2:
        print("Invalid number of provided arguments")
        return 1

    files = FilesDataCollector(args[1]).get_files_data()
    print(files)
    # Md5FilesOrganizer(args[1]).organize_files()
    # EmptyFilesRemover(args[1]).remove_files()
    # FilesPermissionsUpdater(args[1]).update_files_permissions()


if __name__ == "__main__":
    run(sys.argv)
