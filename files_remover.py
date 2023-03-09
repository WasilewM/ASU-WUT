import os


class FilesRemover:
    def __init__(self, files: list) -> None:
        self.files = files

    def remove_files(self):
        self._suggest_files_removal(self.files)
        user_answer = self._has_user_accepted_file_removal()
        if user_answer:
            self._delete_files(self.files)

    def _suggest_files_removal(self, files: list) -> None:
        print("Do you want to delete following files?")
        for file in files:
            print(file.file_path)
        print("Y/N?")

    def _has_user_accepted_file_removal(self) -> bool:
        user_answer = input()
        if user_answer in ("y", "Y"):
            return True
        elif user_answer in ("n", "N"):
            return False
        else:
            print("Invalid option. Aborting the script...")
            exit(1)

    def _delete_files(self, files: list) -> None:
        for file in files:
            os.remove(file.file_path)
            print(f"{file.file_path} has been removed")
