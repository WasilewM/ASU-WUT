from file_data import FileData


class Md5FilesOrganizer:
    def __init__(self, files: list) -> None:
        self.files = files

    def organize_files(self) -> dict:
        files_by_md5 = dict()
        for file in self.files:
            self._update_files_by_md5_dict(files_by_md5, file)
        return files_by_md5

    def _update_files_by_md5_dict(self, files_by_md5: dict, file: FileData):
        if file.md5_hash not in files_by_md5.keys():
            files_by_md5[file.md5_hash] = []
        files_by_md5[file.md5_hash].append(file.file_path)
