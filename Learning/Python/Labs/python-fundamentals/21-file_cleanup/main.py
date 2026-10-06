# Exercise: File Cleanup
#
# Demonstrate creating a directory and moving files between folders.
#
# Concepts:
# - File operations
# - Directory creation
# - `os` module
# - Path handling

# Create a cleanup directory for files that should be organized.
import os

os.mkdir('C:/Users/myb_h/OneDrive/Desktop/CleanedUp/')

# List the entries in the original directory and classify each one.
# folder = 'C:/Users/myb_h/OneDrive/Desktop/'
# entries = os.scandir(folder)
for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory', entry.name)

# Build a destination path and prepare to move a file into the cleanup folder.
folder_destination = 'C:/Users/myb_h/OneDrive/Desktop/'
new_name = os.path.join(folder_destination, 'new.txt')

folder_original = 'C:/Users/myb_h/OneDrive/Desktop/'
folder_destination = 'C:/Users/myb_h/OneDrive/Desktop/CleanedUp'

location_original = os.path.join(folder_original, 'new.txt')
location_destination = os.path.join(folder_destination, 'new.txt')

# Rename the file by moving it to the cleanup directory.
if os.path.isfile(location_original):
    os.rename(location_original, location_destination)

