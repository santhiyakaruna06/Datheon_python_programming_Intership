import os
import shutil
folder_path = os.path.join(os.path.dirname(__file__), "Test_Files")

files = os.listdir(folder_path)
print(files)
count = 0
file_types = {
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",

    ".py": "Code",
    ".html": "Code",
    ".css": "Code"
}

for file in files:
    name, extension = os.path.splitext(file)

    destination = file_types.get(extension)

    if destination is None:
        continue

    os.makedirs(destination, exist_ok=True)

    destination_file = os.path.join(destination, file)

    if os.path.exists(destination_file):
        print(file, "already exists. Skipping.")
        continue
    try:
        shutil.move(
            os.path.join(folder_path, file),
            os.path.join(destination, file)
    )

        print(file, "moved to", destination)
        count += 1

    except FileExistsError:
        print(file, "already exists.")

    except PermissionError:
        print(file, "Permission denied")
    
    print(file)
print("Total files relocated:", count)