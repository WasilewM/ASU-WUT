import os
import time

DIRS = [
    {"path": "./X", "mode": 0o777},
    {"path": "./X/Y1", "mode": 0o777},
    {"path": "./X/Y1/Y11", "mode": 0o777},
    {"path": "./X/Y1/Y12", "mode": 0o777},
    {"path": "./X/Y2", "mode": 0o777},
    {"path": "./X/Y2/Y12", "mode": 0o777},
]

FILES = [
    {"path": "./X/a.txt", "mode": 0o777, "content": "abcdefg..."},
    {"path": "./X/b.txt", "mode": 0o777, "content": "abcdefg..."},
    {"path": "./X/Y1/pi.txt", "mode": 0o444, "content": "3.14159..."},
    {"path": "./X/Y1/Y11/tmp.txt", "mode": 0o777, "content": ""},
    {"path": "./X/Y1/Y12/empty.jpg", "mode": 0o777, "content": ""},
    {"path": "./X/Y2/e.txt", "mode": 0o644, "content": "1.619..."},
    {"path": "./X/Y2/Y12/f?f#$f.txt", "mode": 0o614, "content": "1.619A.."},
    {"path": "./X/Y2/Y12/g g.txt", "mode": 0o612, "content": "1.619AB."},
    {"path": './X/Y2/Y12/h"h".txt', "mode": 0o613, "content": "1.619ABC"},
]

FILES_CREATION_DELAY = 0.5


class TestFilesCreator:
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
        print("Preparing test files")
        self._create_dirs()
        self._create_files()

    def _create_dirs(self):
        print("Creating directories...")
        for dir in self.dirs:
            try:
                os.mkdir(dir["path"], dir["mode"])
                print(f"Created {dir['path']}")
                # delay is needed to allow for the deletion of newer files
                time.sleep(self.delay)
            except Exception as e:
                print(e)

    def _create_files(self):
        print("Creating files...")
        for file in self.files:
            try:
                with open(file["path"], "w") as f:
                    f.write(file["content"])
                os.chmod(file["path"], file["mode"])
                print(f"Created {file['path']}")
                # delay is needed to allow for the deletion of newer files
                time.sleep(self.delay)
            except Exception as e:
                print(e)
