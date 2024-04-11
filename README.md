# Folder-Management-Program--Python-3


This Python script creates folders with the names provided in the names_list within the specified base_directory. Here's a detailed breakdown of how it works:

Import os Module: The script begins by importing the os module, which provides functions for interacting with the operating system, including functions for creating directories (os.makedirs) and joining file paths (os.path.join).

Define create_folders Function: This function takes two arguments:

names: A list of strings representing the names of the folders to be created.
base_directory: A string representing the base directory where the folders will be created.
Loop Over Names List: The function iterates over each name in the names list.

Create Folder Path: For each name, it creates a folder path by joining the base_directory and the name using os.path.join.

Attempt to Create Folder: It then attempts to create the folder using os.makedirs(folder_path). This function creates a directory and also creates any necessary intermediate directories. If the directory already exists, it raises a FileExistsError.

Handle FileExistsError: If the directory already exists, the script catches the FileExistsError exception and prints a message indicating that the folder already exists.

Print Messages: Regardless of whether the folder was successfully created or not, the script prints a message indicating the outcome.

Example List of Names: This is the list of names provided as an example. You can replace it with any other list of names you want to create folders for.

Define Base Directory: This is the directory where the folders will be created. You need to specify the path to your desired directory.

Call create_folders Function: Finally, the script calls the create_folders function with the names_list and base_directory as arguments to start the process of creating folders.
