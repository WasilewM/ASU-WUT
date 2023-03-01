import os
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
