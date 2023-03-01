import os


class EmptyFilesRemover:
    def __init__(self, root_dir: str = ".") -> None:
        self.root = root_dir

    def remove_files(self):
        files = self._find_files(self.root)
        self._suggest_files_removal(files)
        user_answer = self._has_user_accepted_file_removal()
        if user_answer:
            self._delete_files(files)

    def _find_files(self, root_dir: str) -> list:
        files = []
        for f in os.listdir(root_dir):
            file_path = os.path.join(root_dir, f)
            if os.path.isfile(file_path):
                self._handle_file(files, file_path)
            elif os.path.isdir(file_path):
                self._handle_dir(files, file_path)
            else:
                self._handle_unknown_obj(file_path)
        return files

    def _handle_file(self, files: list, file_path: str):
        if os.path.getsize(file_path) == 0:
            files.append(file_path)

    def _handle_dir(self, files: list, file_path: str):
        subdir_files = self._find_files(file_path)
        subdir_files = subdir_files if subdir_files else []
        files += subdir_files

    def _handle_unknown_obj(self, file_path: str):
        print(f"Object {file_path} could not be recognised.")
        exit(1)

    def _suggest_files_removal(self, files: list) -> None:
        print("Do you want to delete following empty files?")
        for file_path in files:
            print(file_path)
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
        for file_path in files:
            os.remove(file_path)
            print(f"{file_path} has been removed")
