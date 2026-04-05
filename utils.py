# Utility functions for file automation
import os
import shutil

#File type mapping
FILE_TYPE_MAPPING = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar.gz']
}

def get_file_type(file_extension):
    """Returns the file type based on the file extension."""
    for file_type, extensions in FILE_TYPE_MAPPING.items():
        if file_extension.lower() in extensions:
            return file_type
    return 'Others'

#Organize files in the specified directory
def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    for filename in os.listdir(directory):
        #check if it is a file
        original_path = os.path.join(directory, filename)
        if os.path.isfile(original_path):
            file_extension = os.path.splitext(filename)[1]
            file_type = get_file_type(file_extension)
            target_directory = os.path.join(directory, file_type)
            destination_path = os.path.join(target_directory, filename)
            if not os.path.exists(target_directory):
                os.mkdir(target_directory)
            """            Move the file to the target directory and skip duplicates"""
            if not os.path.exists(destination_path):
                shutil.move(original_path, destination_path)
                print(f"Moved '{filename}' to '{target_directory}'")
            
