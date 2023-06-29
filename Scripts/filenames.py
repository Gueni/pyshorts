
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

#---------------------------------------------------------------------
folder_path         = "C:/Users/HomePC/Downloads"
destination_folder  = "D:/8 PC"
rename_files(folder_path,destination_folder)
