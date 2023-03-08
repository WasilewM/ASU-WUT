from files_data_collector import FilesDataCollector
from md5_files_organizer import Md5FilesOrganizer
from empty_files_finder import EmptyFilesFinder
from files_permissions_updater import FilesPermissionsUpdater
from files_remover import FilesRemover


class DirectoryCleaner:
    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir
        self.files_collector = FilesDataCollector(self.root_dir)

    def run(self) -> None:
        self._handle_duplicated_files_removal()
        self._handle_empty_files_removal()
        self._handle_files_permissions_update()

    def _handle_duplicated_files_removal(self):
        files = self.files_collector.get_files_data()
        md5_organizer = Md5FilesOrganizer(files)
        organized_files = md5_organizer.get_organized_files()
        unnecessary_files = md5_organizer.get_duplicated_files(organized_files)
        FilesRemover(unnecessary_files).remove_files()

    def _handle_empty_files_removal(self):
        files = self.files_collector.get_files_data()
        empty_files = EmptyFilesFinder(files).get_empty_files()
        FilesRemover(empty_files).remove_files()

    def _handle_files_permissions_update(self):
        files = self.files_collector.get_files_data()
        FilesPermissionsUpdater(files).update_files_permissions()
