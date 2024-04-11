import os

def create_folders(names, base_directory):
    for name in names:
        folder_path = os.path.join(base_directory, name)
        try:
            os.makedirs(folder_path)
            print(f"Folder created: {folder_path}")
        except FileExistsError:
            print(f"Folder already exists: {folder_path}")

# Example list of names
names_list = [
    "Elijah Kariuki",
    "Samantha Mwangi",
    "Maxwell Okoth",
    "Aisha Chepkoech",
    "Patrick Otieno",
    "Fiona Auma",
    "David Gitau",
    "Esther Wanjiku",
    "Brian Omondi",
    "Alice Kamau",
    "Daniel Waweru"
]



# Directory where folders will be created (Create a folder called a on the desktop)
base_directory = "/Users/kenronoh/Desktop/name_of_the_folder"


create_folders(names_list, base_directory)
