import os
import shutil

def organizer(folder):
    # Loop through all items in the folder
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue


        if "." in file:
            extension = file.split(".")[-1].lower()
        else:
            extension = "no extension"

        main_folder = os.path.join(folder, extension)
        os.makedirs(main_folder, exist_ok=True)


        shutil.move(file_path, os.path.join(main_folder, file))

    print("Your file has been organized successfully")

if __name__ == "__main__":
    organizer("C:/Users/Ayinyintan Oresanya/Documents")