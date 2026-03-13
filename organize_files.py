import os
import shutil

def organize_files(base_path, file_types):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file)
        moved = False

        for folder_name, extensions in file_types.items():
            if extension.lower() in extensions:
                destination_folder = os.path.join(base_path, folder_name)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, file))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(base_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))

    print("\n📂 Files AFTER organizing:")
    for root, dirs, files in os.walk(base_path):
        level = root.replace(base_path, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = "  " * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
