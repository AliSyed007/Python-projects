import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Desktop")

extensions ={
    ".jpg" : "Images",
    ".png" : "Images",
    ".gif" : "Images",
    ".mp4" : "Videos",
    ".mov" : "Videos",
    ".flv" : "Videos",
    ".csv" : "Documents",
    ".docx" : "Documents",
    ".txt" : "Documents",
    ".xlsx" : "Documents",
    ".rtf" : "Documents",
    ".pdf" : "Documents",
    ".mp3" : "Music",
    ".wav" : "Music"

}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename) [1]. lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"moved {filename} to {folder_name}.")
        else:
            print(f"skipped {filename}. unknown file extension.")

    else:
        print(f"skipped {filename}. It is a directory.")

print("file organization completed!")
