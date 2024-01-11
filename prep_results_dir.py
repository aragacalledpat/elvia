import os
import shutil

def create_folders(source_directory, destination_directory):
    # Get a list of all files in the source directory
    files = os.listdir(source_directory)

    for file in files:
        # Check if the item is a file
        if os.path.isfile(os.path.join(source_directory, file)):
            # Remove the file extension
            #folder_name = os.path.splitext(file)[0]
            folder_name = file

            # Create a folder with the name (without extension) in the destination directory
            folder_path = os.path.join(destination_directory, folder_name)

            # Check if the folder already exists, if not, create it
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

if __name__ == "__main__":
    source_directory = "C:\\code\\elvia\\data"
    destination_directory = "C:\\code\\elvia\\results"

    create_folders(source_directory, destination_directory)
