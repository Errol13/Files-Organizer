# Utility functions for file automation
import os
import shutil
from pathlib import Path
from abc import ABC, abstractmethod

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
            file_extension = Path(filename).suffix.lower()
            file_type = get_file_type(file_extension)
            target_directory = os.path.join(directory, file_type)
            destination_path = os.path.join(target_directory, filename)
            if not os.path.exists(target_directory):
                os.makedirs(target_directory, exist_ok=True)
            """            Move the file to the target directory and skip duplicates"""
            if not os.path.exists(destination_path):
                shutil.move(original_path, destination_path)
                print(f"Moved '{filename}' to '{target_directory}'")

def count_files_by_type(directory):
    #using pathlib library here
    """Counts the number of files in each category."""
    file_counts = {file_type: 0 for file_type in FILE_TYPE_MAPPING.keys()} #using list comprehension to initialize the file counts
    file_counts['Others'] = 0 # add 'Others' category to the file counts
    if not Path(directory).exists():
        print(f"Directory '{directory}' does not exist.")
        return file_counts
    for filename in os.listdir(directory):
        original_path = os.path.join(directory, filename)
        if Path(original_path).is_file():
            file_extension = Path(filename).suffix.lower()
            file_type = get_file_type(file_extension)
            file_counts[file_type] += 1
    return file_counts

def dry_run(directory):
    """Simulates the file organization without making any changes."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    """for filename in os.listdir(directory):
        original_path = os.path.join(directory, filename)
        if os.path.isfile(original_path):
            file_extension = Path(filename).suffix.lower()
            file_type = get_file_type(file_extension)
            target_directory = os.path.join(directory, file_type)
            print(f"Would move '{filename}' to '{target_directory}'")"""
    #count the files by type and display the counts
    file_counts = count_files_by_type(directory)
    print("Total files for each category:")
    for file_type, count in file_counts.items():
        print(f"{file_type}: Would move {count} files \n")