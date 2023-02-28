import os
import sys
import hashlib


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

    def _handle_files(self, root_dir, files_by_md5) -> None:
        for f in os.listdir(root_dir):
            file_path = os.path.join(root_dir, f)
            if os.path.isfile(file_path):
                self._handle_single_file(files_by_md5, file_path)
            elif os.path.isdir(file_path):
                self._handle_single_dir(files_by_md5, file_path)
            else:
                print(f"Object {file_path} could not be recognised.")
                exit(1)

    def _handle_single_file(self, files_by_md5, file_path):
        with open(file_path, "r") as file_handle:
            encoded_file = file_handle.read().encode(
                self.files_encoding_format
            )
            md5_hash = hashlib.md5(encoded_file).hexdigest()
            self._update_files_by_md5_dict(files_by_md5, file_path, md5_hash)

    def _handle_single_dir(self, files_by_md5, file_path):
        subdir_files_by_md5 = self.organize_files(file_path)
        for md5_hash in subdir_files_by_md5:
            for md5_hash_file_path in subdir_files_by_md5[md5_hash]:
                self._update_files_by_md5_dict(
                    files_by_md5, md5_hash_file_path, md5_hash
                )

    def _update_files_by_md5_dict(self, files_by_md5, file_path, md5_hash):
        if md5_hash not in files_by_md5.keys():
            files_by_md5[md5_hash] = []
        files_by_md5[md5_hash].append(file_path)


def run(args) -> int:
    print("CWD: ", os.getcwd())

    if len(args) != 2:
        print("Invalid number of provided arguments")
        return 1

    files_by_md5 = Md5FilesOrganizer(args[1]).organize_files()
    print(f"files_by_md5: {files_by_md5}")

    empty_files = find_empty_files(args[1])
    print(f"empty_files: {empty_files}")
    suggest_empty_files_removal(empty_files)
    user_answer = has_user_accepted_file_removal()
    if user_answer:
        delete_empty_files(empty_files)


def find_empty_files(root_dir: str) -> list:
    empty_files = []
    for f in os.listdir(root_dir):
        file_path = os.path.join(root_dir, f)
        if os.path.isfile(file_path):
            if os.path.getsize(file_path) == 0:
                empty_files.append(file_path)
        elif os.path.isdir(file_path):
            subdir_empty_files = find_empty_files(file_path)
            subdir_empty_files = (
                subdir_empty_files if subdir_empty_files else []
            )
            empty_files += subdir_empty_files
        else:
            print(f"Object {file_path} could not be recognised.")
            exit(1)
    return empty_files


def suggest_empty_files_removal(empty_files: list) -> None:
    print("Do you want to delete following empty files?")
    for file_path in empty_files:
        print(file_path)
    print("Y/N?")


def has_user_accepted_file_removal() -> bool:
    user_answer = input()
    if user_answer in ("y", "Y"):
        return True
    elif user_answer in ("n", "N"):
        return False
    else:
        print("Invalid option. Aborting the script...")
        exit(1)


def delete_empty_files(empty_files: list) -> None:
    for file_path in empty_files:
        os.remove(file_path)
        print(f"{file_path} has been removed")


if __name__ == "__main__":
    run(sys.argv)
