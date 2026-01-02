from pathlib import Path
import sys

def rename(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("Folder doesn't exist")
        return
    
    if not folder.is_dir():
        print("It's not a Directory. Please pass a Folder")
        return
    
    dir_content = []
    print(f"Reading {folder_path}:")
    for item in folder.iterdir():
        print(item)
        dir_content.append(item)
    
    files = []
    print(f"Files found in {folder_path} are:")
    for item in dir_content:
        if item.is_file():
            print(item)
            files.append(item)
    
    files = sorted(files, key=lambda x: x.name.lower())

    start = 1

    for file in files:
        new_name = (f"{folder.name}_{start}{file.suffix}")
        new_path = file.parent / new_name
        while new_path.exists():
            start +=1
            new_path = file.parent / (f"{folder.name}_{start}{file.suffix}")
        file.rename(new_path)
        start += 1
        print(f"{file.name} -> {new_path.name}")


rename(sys.argv[1])