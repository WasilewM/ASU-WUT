import os
import sys
from files_data_collector import FilesDataCollector
from md5_files_organizer import Md5FilesOrganizer
from empty_files_remover import EmptyFilesRemover
from files_permissions_updater import FilesPermissionsUpdater


def run(args: list) -> int:
    print("CWD: ", os.getcwd())

    if len(args) != 2:
        print("Invalid number of provided arguments")
        return 1

    files = FilesDataCollector(args[1]).get_files_data()
    print(files)
    Md5FilesOrganizer(args[1]).organize_files()
    EmptyFilesRemover(args[1]).remove_files()
    FilesPermissionsUpdater(args[1]).update_files_permissions()


if __name__ == "__main__":
    run(sys.argv)
