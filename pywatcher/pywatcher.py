from watchfiles import watch, run_process
from pathlib import Path
import os
import shutil
dir_path = Path(r"E:\Playstation\ePSXe")
backup_path = Path(r"E:\backup")

def create_dir(path:str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path)

def callback(changes):
    print(changes)
    data = list(changes)[0]
    path_to_file = data[1]

    # create parent folder
    backup_full = os.path.join(backup_path, dir_path.name) 
    print("full path: %s" % backup_full)
    create_dir(backup_full)


    parent_dir = Path(path_to_file).parent.name

    relative_path = os.path.relpath(path_to_file, dir_path)
 
    x = Path(os.path.join(backup_full, relative_path)).parent
    print("x : %s" % x)
    # print("parent dir %s" % parent_dir)
    # backup = os.path.join(backup_full, parent_dir)
    create_dir(Path(x))
    print("backup_full : %s " % x)
    print(parent_dir)
    # print("backup destination: %s" % backup)
    # make parent directory
    
    file_event = data[0].name

    if file_event == "modified" or file_event == "added":
        shutil.copy2(path_to_file, os.path.join(x, Path(path_to_file).name))
        print("File copied from %s --> %s"  % (path_to_file, x))

    
    print("path file : %s // file_event : %s " % (path_to_file, file_event))
if __name__ == "__main__":

    for f in run_process(dir_path, target=None, callback=callback):
        pass
