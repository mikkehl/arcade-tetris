import os
import re

# 1. List folders in directory
# 2. For each folder do:
    # 2.1 Rename ".*_block.png" to "single.png"
    # 2.2 Rename ".*_1.png" to "north.png"
    # 2.3 Rename ".*_2.png" to "east.png"
    # 2.4 Rename ".*_3.png" to "south.png"
    # 2.5 Rename ".*_4.png" to "west.png"

rename_patterns = [
    (r".*_block\.png$", "single.png"),
    (r".*_[A-Z]1\.png$", "north.png"),
    (r".*_[A-Z]2\.png$", "east.png"),
    (r".*_[A-Z]3\.png$", "south.png"),
    (r".*_[A-Z]4\.png$", "west.png"),
]


def get_matching_pattern(file):
    for pattern, new_name in rename_patterns:
        if re.match(pattern, file):
            return new_name
    return None


def process_file(folder_path, file):
    file_path = os.path.join(folder_path, file)
    if not os.path.isfile(file_path):
        return
    
    new_name = get_matching_pattern(file)
    if new_name:
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)


def rename_files(root):
    for folder in os.listdir(root):
        folder_path = os.path.join(root, folder)
        if not os.path.isdir(folder_path):
            continue
        
        for file in os.listdir(folder_path):
            process_file(folder_path, file)


if __name__ == "__main__":
    rename_files("./Tetris/Assets/Blocks/")
