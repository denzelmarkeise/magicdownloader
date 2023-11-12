import os
import shutil

def organize_files_and_folders(source_folder, destination_folder):
    # ---CREATE THE DESTINATION FOLDER IF IT DOES NOT EXIST!!---
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # ---ITERATE THROUGH ALL ITEMS (FILES AND FOLDERS) IN THE SOURCE FOLDER!!---
    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)

        # ---CHECK IF IT'S A FILE OR A FOLDER!!---
        if os.path.isfile(source_path):
            # ---FOR FILES: GET THE FILE EXTENSION!!---
            _, extension = os.path.splitext(item)
            destination_path = os.path.join(destination_folder, extension[1:])
        elif os.path.isdir(source_path):
            # ---FOR FOLDERS: USE THE FOLDER NAME!!---
            destination_path = os.path.join(destination_folder, item)
        else:
            # Skip if it's neither a file nor a folder
            continue

        # ---CREATE THE SUBDIRECTORY BASED ON THE ITEM TYPE (FILE OR FOLDER)!---
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # ---MOVE THE ITEM TO THE APPROPRIATE SUBDIRECTORY!---
        shutil.move(source_path, os.path.join(destination_path, item))

if __name__ == "__main__":
    # ---SPECIFY THE SOURCE & DESTINATION FOLDERS!---
    source_folder = r"C:\Users\yourusername\Downloads"
    destination_folder = r"/Users/yourusername/Documents/OrganizedDownloads"

    # ---ORGANIZE FILES AND FOLDERS!---
    organize_files_and_folders(source_folder, destination_folder)

    print("File and folder organization has been completed!")
