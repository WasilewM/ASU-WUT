from .files_data_collector import FileData
import os
import shutil


class FilesRelocator:
    def __init__(self, files: list, new_dir: str) -> None:
        self.files = files
        self.new_dir = new_dir

    def relocate_files(self) -> None:
        for file in self.files:
            self._relocate_file(file)

    def _relocate_file(self, file: FileData) -> None:
        file_name = os.path.split(file.file_path)[-1]
        new_file_path = os.path.join(self.new_dir, file_name)
        shutil.move(file.file_path, new_file_path)
