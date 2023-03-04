import os
import time

DIRS = [
    {"path": "./X", "mode": 0o777},
    {"path": "./X/Y1", "mode": 0o777},
    {"path": "./X/Y1/Y11", "mode": 0o777},
    {"path": "./X/Y1/Y12", "mode": 0o777},
    {"path": "./X/Y2", "mode": 0o777},
]

FILES = [
    {"path": "./X/a.txt", "mode": 0o777, "content": "abcdefg..."},
    {"path": "./X/b.txt", "mode": 0o777, "content": "abcdefg..."},
    {"path": "./X/Y1/pi.txt", "mode": 0o444, "content": "3.14159..."},
    {"path": "./X/Y1/Y11/tmp.txt", "mode": 0o777, "content": ""},
    {"path": "./X/Y1/Y12/empty.jpg", "mode": 0o777, "content": ""},
    {"path": "./X/Y2/e.txt", "mode": 0o644, "content": "1.619..."},
]

FILES_CREATION_DELAY = 0.5


class TestEnvManager:
    def __init__(
        self,
        dirs: list = DIRS,
        files: list = FILES,
        delay: float = FILES_CREATION_DELAY,
    ) -> None:
        self.dirs = dirs
        self.files = files
        self.delay = delay

    def prepare_env(self):
        self._delete_old_env()
        self._prepare_new_env()

    def _delete_old_env(self):
        self._delete_files
        self._delete_dirs()

    def _prepare_new_env(self):
        self._create_dirs()
        self._create_files()

    def delete_env(self):
        self._delete_files()
        self._delete_dirs()

    def _create_dirs(self):
        for dir in self.dirs:
            try:
                os.mkdir(dir["path"], dir["mode"])
                # delay is needed to allow for the deletion of newer files
                time.sleep(self.delay)
            except Exception as e:
                print(e)

    def _create_files(self):
        for file in self.files:
            try:
                with open(file["path"], "w") as f:
                    f.write(file["content"])
                os.chmod(file["path"], file["mode"])
                # delay is needed to allow for the deletion of newer files
                time.sleep(self.delay)
            except Exception as e:
                print(e)

    def _delete_dirs(self):
        for file in reversed(self.dirs):
            try:
                os.rmdir(file["path"])
            except FileNotFoundError:
                print(
                    f"Directory {file['path']} not found - could "
                    + "not delete it"
                )
            except Exception as e:
                print(
                    "An error occurred while trying to delete following "
                    + f"directory {file['path']}: {e}"
                )

    def _delete_files(self):
        for file in reversed(self.files):
            try:
                os.remove(file["path"])
            except FileNotFoundError:
                print(
                    f"File {file['path']} not found - could " + "not delete it"
                )
            except Exception as e:
                print(
                    "An error occurred while trying to delete following "
                    + f"file {file['path']}: {e}"
                )
