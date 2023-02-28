import os
import sys
import hashlib

FILES_ENCODING_FORMAT = 'UTF-8'


def run(args) -> int:
    print("CWD: ", os.getcwd())

    if len(args) != 2:
        print("Invalid number of provided arguments")
        return 1

    files_by_md5 = get_files_by_md5(args[1])
    print(f"files_by_md5: {files_by_md5}")


def get_files_by_md5(root_dir: str) -> dict:
    files_by_md5 = dict()
    for f in os.listdir(root_dir):
        file_path = os.path.join(root_dir, f)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file_handle:
                encoded_file = file_handle.read().encode(FILES_ENCODING_FORMAT)
                md5_hash = hashlib.md5(encoded_file).hexdigest()

                _update_files_by_md5_dict(files_by_md5, file_path, md5_hash)
        if os.path.isdir(file_path):
            subdir_files_by_md5 = get_files_by_md5(file_path)
            for md5_hash in subdir_files_by_md5:
                for md5_hash_file_path in subdir_files_by_md5[md5_hash]:
                    _update_files_by_md5_dict(files_by_md5, md5_hash_file_path, md5_hash)
    return files_by_md5


def _update_files_by_md5_dict(files_by_md5, file_path, md5_hash):
    if md5_hash not in files_by_md5.keys():
        files_by_md5[md5_hash] = []
    files_by_md5[md5_hash].append(file_path)


if __name__ == "__main__":
    run(sys.argv)
