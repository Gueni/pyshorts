
import os

def rename_files(folder_path):
    file_list = os.listdir(folder_path)  # Get the list of file names in the folder

    for file_name in file_list:
        old_file_path = os.path.join(folder_path, file_name)
        new_file_name = str(hash(file_name)) + file_name[:-1]  # Add a unique number and remove the last character

        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(old_file_path, new_file_path)  # Rename the file

    print("Files renamed successfully!")

#---------------------------------------------------------------------
folder_path = "C:/Users/HomePC/Videos"
rename_files(folder_path)
