from watchfiles import watch, run_process
from pathlib import Path
import os
import shutil
import argparse

# parser = argparse.ArgumentParser(
#     prog="Data Backupper",
#     description="File monitor and data backupper",
#     epilog="Bottom text")

# parser.add_argument("-input", "-i", help="Directory to monitor for events", metavar="input", required=True)
# parser.add_argument("-output", "-o", help="Backup for directory.")


# args = parser.parse_args()
# print(args.input)
# print(args.output)

dir_path = Path(r"E:\Playstation\ePSXe")
backup_path = Path(r"E:\backup")

def create_dir(path:str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path)

def callback(changes):
    for c in changes:
        print(c)

        data = list(c)
        path_to_file = data[1]
        file_event = data[0].name

        # create parent folder
        backup_parent_dir = os.path.join(backup_path, dir_path.name) 
        create_dir(backup_parent_dir)
        relative_path = os.path.relpath(path_to_file, dir_path)
        dst = Path(os.path.join(backup_parent_dir, relative_path)).parent
        create_dir(dst)
        if file_event == "modified" or file_event == "added":
            shutil.copy2(path_to_file, os.path.join(dst, Path(path_to_file).name))
            print("File copied from %s --> %s"  % (path_to_file, dst))

if __name__ == "__main__":
    print("running")
    for f in run_process(dir_path, target=None, callback=callback):
        pass
