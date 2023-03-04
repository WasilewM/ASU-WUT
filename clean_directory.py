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

    # files = FilesDataCollector(args[1]).get_files_data()
    # # print(files)
    # organized_files = Md5FilesOrganizer(files).organize_files()
    # print(organized_files)
    # EmptyFilesRemover(files).remove_files()

    files = FilesDataCollector(args[1]).get_files_data()
    FilesPermissionsUpdater(files).update_files_permissions()


if __name__ == "__main__":
    run(sys.argv)
