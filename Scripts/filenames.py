
import os,shutil

def rename_files(folder_path,destination_folder):
    file_list = os.listdir(folder_path)  # Get the list of file names in the folder

    for file_name in file_list:
        if file_name.endswith(".mp4_"):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_name = str(hash(file_name)) + file_name[:-1]  # Add a unique number and remove the last character

            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)  # Rename the file
            #move file to destination            
            shutil.move(new_file_path, destination_folder)
    print("Files renamed successfully!")

from pathlib import Path

def sort_files_by_creation_date(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out only files (not directories)
    files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

    # Sort files by their creation date
    files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

    # Add a number to the beginning of their names
    for index, file in enumerate(files):
        new_name = f"{index:02d}.mp4"#_{file}"
        # new_name = new_name[10:]
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

#---------------------------------------------------------------------
if __name__ == "__main__":
    folder_path         = "C:/Users/HomePC/Downloads"
    destination_folder  = "D:/8 PC"
    rename_files(folder_path,destination_folder)
    sort_files_by_creation_date(destination_folder)

