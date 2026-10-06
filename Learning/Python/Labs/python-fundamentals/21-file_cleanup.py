#Make the folder CleanedUp/
#list the files in the Desktop/ Folder
#For each file in the Desktop/ Folder
#Move the file to thje CleanedUp/ Folder

import os

#make new directory
os.mkdir('C:/Users/myb_h/OneDrive/Desktop/CleanedUp/')

#list out what files are in the path
# folder = 'C:/Users/myb_h/OneDrive/Desktop/'
# entries = os.scandir(folder)

# # #check if a Directory Entry is a File or a Subdirectory
for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory' , entry.name)    

#Create an Absolute Path Name
folder_destination = 'C:/Users/myb_h/OneDrive/Desktop/'
new_name = os.path.join(folder_destination, 'new.txt')

# #move a file
folder_original = 'C:/Users/myb_h/OneDrive/Desktop/'
folder_destination = 'C:/Users/myb_h/OneDrive/Desktop/CleanedUp'

location_original = os.path.join(folder_original, 'new.txt')
location_destination = os.path.join(folder_destination, 'new.txt')

# #rename file
if os.path.isfile(location_original):
    os.rename(location_original, location_destination)

