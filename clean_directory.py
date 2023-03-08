import os
import sys
from files_data_collector import FilesDataCollector
from md5_files_organizer import Md5FilesOrganizer
from empty_files_finder import EmptyFilesFinder
from files_permissions_updater import FilesPermissionsUpdater
from files_remover import FilesRemover


def run(args: list) -> int:
    print("CWD: ", os.getcwd())

    if len(args) != 2:
        print("Invalid number of provided arguments")
        return 1

    collector = FilesDataCollector(args[1])
    files = collector.get_files_data()
    md5_organizer = Md5FilesOrganizer(files)
    organized_files = md5_organizer.organize_files()
    print(f"organized_files: {organized_files}\n")
    unnecessary_files = md5_organizer.get_unnecessary_files_from_duplicated(
        organized_files
    )
    print(f"unnecessary_files: {unnecessary_files}\n")
    FilesRemover(unnecessary_files).remove_files()

    files = collector.get_files_data()
    empty_files = EmptyFilesFinder(files).get_empty_files()
    print(f"empty_files: {empty_files}\n")
    FilesRemover(empty_files).remove_files()

    files = collector.get_files_data()
    FilesPermissionsUpdater(files).update_files_permissions()


if __name__ == "__main__":
    run(sys.argv)
