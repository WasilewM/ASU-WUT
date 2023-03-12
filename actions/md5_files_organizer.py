from .files_data_collector import FileData


class Md5FilesOrganizer:
    def __init__(self, files: list) -> None:
        self.files = files

    def get_organized_files(self) -> dict:
        files_by_md5 = dict()
        for file in self.files:
            self._update_files_by_md5_dict(files_by_md5, file)
        return files_by_md5

    def get_duplicated_files(self, organized_files: dict) -> list:
        unnecessary_files = []
        for md5_hash in organized_files:
            current_hash_unnecessary = self._get_unnecessary_files_from_list(
                organized_files[md5_hash]
            )
            unnecessary_files += current_hash_unnecessary
        return unnecessary_files

    def _get_unnecessary_files_from_list(self, files: list) -> list:
        if len(files) > 1:
            oldest = min([file.creation_timestamp for file in files])
            unnecessary_files = [
                file for file in files if file.creation_timestamp > oldest
            ]
            return unnecessary_files
        return []

    def _update_files_by_md5_dict(self, files_by_md5: dict, file: FileData):
        if file.md5_hash not in files_by_md5.keys():
            files_by_md5[file.md5_hash] = []
        files_by_md5[file.md5_hash].append(file)
