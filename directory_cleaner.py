from actions.files_data_collector import FilesDataCollector
from actions.md5_files_organizer import Md5FilesOrganizer
from actions.empty_files_finder import EmptyFilesFinder
from actions.files_permissions_updater import FilesPermissionsUpdater
from actions.files_remover import FilesRemover
from actions.files_renamer import FilesRenamer
from actions.files_relocator import FilesRelocator
from actions.temporary_files_finder import TemporaryFilesFinder
from actions.duplicated_filename_files_finder import (
    DuplicatedFilenameFilesFinder,
)

from parameters import (
    UNWANTED_CHARACTERS,
    UNWANTED_CHARACTERS_REPLACEMENT,
    EXPECTED_FILE_PERMISSIONS,
    TEMPORARY_FILES,
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
            self._handle_duplicated_filenames_removal()
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
        FilesRemover().run(unnecessary_files)

    def _handle_empty_files_removal(self) -> None:
        print("-> Deleting empty files")
        files = self.files_collector.get_files_data()
        empty_files = EmptyFilesFinder(files).find_files()
        FilesRemover().run(empty_files)

    def _handle_temporary_files_removal(self) -> None:
        print("-> Deleting temporary files")
        files = self.files_collector.get_files_data()
        temporary_files = TemporaryFilesFinder(
            files, TEMPORARY_FILES
        ).find_files()
        FilesRemover().run(temporary_files)

    def _handle_duplicated_filenames_removal(self) -> None:
        print("-> Deleting duplicated filenames files")
        files = self.files_collector.get_files_data()
        duplicated_filenames_finder = DuplicatedFilenameFilesFinder(files)
        duplicated_filenames_files = duplicated_filenames_finder.find_files()
        unnecessary_files = duplicated_filenames_finder.get_old_files(
            duplicated_filenames_files
        )
        FilesRemover().run(unnecessary_files)

    def _handle_files_permissions_update(self) -> None:
        print("-> Updating file permissions")
        files = self.files_collector.get_files_data()
        FilesPermissionsUpdater(EXPECTED_FILE_PERMISSIONS).run(files)

    def _handle_files_renaming(self) -> None:
        print("-> Renaming files with unwanted characters")
        files = self.files_collector.get_files_data()
        FilesRenamer(UNWANTED_CHARACTERS, UNWANTED_CHARACTERS_REPLACEMENT).run(
            files
        )

    def _handle_files_relocation(self) -> None:
        print(f"-> Relocation files to directory {self.root_dir}")
        files = self.files_collector.get_files_data()
        FilesRelocator(self.root_dir).run(files)
