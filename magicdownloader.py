import os
import shutil

def organize_files(source_folder, destination_folder):
    # ---CREATE THE DESTINATION FOLDER IF IT DOES NOT EXIST!!---
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # ---ITERATE THROUGH ALL FILES IN THE SOURCE FOLDER!!---
    
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # ---CHECK IF IT'S A FILE!!---

        if os.path.isfile(source_path):
            # ---GET THE FILE EXTENSION!!----
            
            _, extension = os.path.splitext(filename)

            # ---CREATE A SUBDIRECTORY BASED ON THE FILE EXTENSION!!---
            
            destination_path = os.path.join(destination_folder, extension[1:])
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # ---MOVE THE FILE TO THE APPROPRIATE SUBDIRECTORY!!---
            
            shutil.move(source_path, os.path.join(destination_path, filename))

if __name__ == "__main__":
    
    # ---SPECIFY THE SOURCE & DESTINATION FOLDERS!!---
    
    source_folder = r"C:\Users\yourusername\Downloads"
    destination_folder = r"C:\Users\yourusername\Organized Downloads"

    # ---ORGANIZE FILES!!---

    organize_files(source_folder, destination_folder)

    print("File organization has been completed!")