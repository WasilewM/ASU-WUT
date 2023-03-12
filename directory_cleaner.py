from files_data_collector import FilesDataCollector
from md5_files_organizer import Md5FilesOrganizer
from empty_files_finder import EmptyFilesFinder
from files_permissions_updater import FilesPermissionsUpdater
from files_remover import FilesRemover
from files_renamer import FilesRenamer
from files_relocator import FilesRelocator
from temporary_files_finder import TemporaryFilesFinder

from parameters import (
    UNWANTED_CHARACTERS,
    UNWANTED_CHARACTERS_REPLACEMENT,
    EXPECTED_FILE_PERMISSIONS,
)


class DirectoryCleaner:
    def __init__(self, root_dir: str = ".") -> None:
        self.root_dir = root_dir
        self.files_collector = FilesDataCollector(self.root_dir)

    def run(self) -> None:
        print("Directory Cleaning has started")
        try:
            self._handle_duplicated_files_removal()
            self._handle_empty_files_removal()
            self._handle_temporary_files_removal()
            self._handle_files_permissions_update()
            self._handle_files_renaming()
            self._handle_files_relocation()
        except Exception as e:
            print(f"Directory cleaning has failed with following error: {e}")

    def _handle_duplicated_files_removal(self) -> None:
        print("-> Deleting duplicated files")
        files = self.files_collector.get_files_data()
        md5_organizer = Md5FilesOrganizer(files)
        organized_files = md5_organizer.get_organized_files()
        unnecessary_files = md5_organizer.get_duplicated_files(organized_files)
        FilesRemover(unnecessary_files).remove_files()

    def _handle_empty_files_removal(self) -> None:
        print("-> Deleting empty files")
        files = self.files_collector.get_files_data()
        empty_files = EmptyFilesFinder(files).find_files()
        FilesRemover(empty_files).remove_files()

    def _handle_temporary_files_removal(self) -> None:
        print("-> Deleting temporary files")
        files = self.files_collector.get_files_data()
        temporary_files = TemporaryFilesFinder(files).find_files()
        FilesRemover(temporary_files).remove_files()

    def _handle_files_permissions_update(self) -> None:
        print("-> Updating file permissions")
        files = self.files_collector.get_files_data()
        FilesPermissionsUpdater(
            files, EXPECTED_FILE_PERMISSIONS
        ).update_files_permissions()

    def _handle_files_renaming(self) -> None:
        print("-> Renaming files with unwanted characters")
        files = self.files_collector.get_files_data()
        FilesRenamer(
            UNWANTED_CHARACTERS, UNWANTED_CHARACTERS_REPLACEMENT, files
        ).replace_unwanted_chars()

    def _handle_files_relocation(self) -> None:
        print(f"-> Relocation files to directory {self.root_dir}")
        files = self.files_collector.get_files_data()
        FilesRelocator(files, self.root_dir).relocate_files()
