import os


class DuplicatedFilenameFilesFinder:
    def __init__(self, files: list) -> None:
        self.files = files

    def find_files(self) -> dict:
        duplicated_filenames_files = dict()
        for file in self.files:
            curr_filename = os.path.split(file.file_path)[-1]
            if curr_filename not in duplicated_filenames_files:
                duplicated_filenames_files[curr_filename] = []
            duplicated_filenames_files[curr_filename].append(file)
        return duplicated_filenames_files

    def get_old_files(self, files: dict) -> list:
        unnecessary_files = []
        for filename in files:
            current_hash_unnecessary = self._get_old_files_from_list(
                files[filename]
            )
            unnecessary_files += current_hash_unnecessary
        return unnecessary_files

    def _get_old_files_from_list(self, files: list) -> list:
        if len(files) > 1:
            newest = max([file.creation_timestamp for file in files])
            unnecessary_files = [
                file for file in files if file.creation_timestamp < newest
            ]
            return unnecessary_files
        return []
