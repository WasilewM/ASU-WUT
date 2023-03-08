from files_data_collector import FilesDataCollector
from md5_files_organizer import Md5FilesOrganizer
from empty_files_finder import EmptyFilesFinder
from files_permissions_updater import FilesPermissionsUpdater
from files_remover import FilesRemover


class DirectoryCleaner:
    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir

    def run(self) -> None:
        collector = FilesDataCollector(self.root_dir)
        files = collector.get_files_data()
        md5_organizer = Md5FilesOrganizer(files)
        organized_files = md5_organizer.get_organized_files()
        print(f"organized_files: {organized_files}\n")
        unnecessary_files = md5_organizer.get_duplicated_files(organized_files)
        print(f"unnecessary_files: {unnecessary_files}\n")
        FilesRemover(unnecessary_files).remove_files()

        files = collector.get_files_data()
        empty_files = EmptyFilesFinder(files).get_empty_files()
        print(f"empty_files: {empty_files}\n")
        FilesRemover(empty_files).remove_files()

        files = collector.get_files_data()
        FilesPermissionsUpdater(files).update_files_permissions()
