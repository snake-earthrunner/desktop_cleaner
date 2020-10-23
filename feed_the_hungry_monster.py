#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:38:12 2020

@author: earthrunner
"""

# Importing the os library that handles ...
import os

#Specifiying the paths to the directories used/investigated.
folder_to_track = '/Users/earthrunner/Desktop/full_fridge'
folder_destination = '/Users/earthrunner/Desktop/hungry_monster'


#THIS PART creates a dictionary of the files in the directory "folder_to_track" i.e.filename:path
#Placeholder (empty) lists for the files stored in "folder_to_track" and "folder_destination"
file_list_destination = []
file_list_tracking = []

"""
Explanation  to the codes below:
    
    Loop to extract files inside the directories
 
    path --> Name of each directory
    folders --> List of subdirectories inside current 'path'
    files --> List of files inside current 'path'
"""

#DESTINATION-loop that extracts all files recursively from "folder_to_track" and stores the files in file_list_destination = []
#Directories (".DS_Store") are excluded and thus not stored in the list

#Gets all the files in the "folder_to_track" directory and stores them in the file_list_tracking = []
for path, folders, files in os.walk(folder_to_track):
    for file in files:
        if file != ".DS_Store":
            file_list_tracking.append(file)


# Get the list of all files in directory tree at given path and stores them in listOfFiles list
listOfFiles = []
for (dirpath, dirnames, filenames) in os.walk(folder_to_track):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]  
    # removes the directory paths containi9ng ".DS_Store" from the list because they are not needed/desired
for elem in listOfFiles:
    if ".DS_Store" in elem:
        listOfFiles.remove(elem)

fridge_storage_map = dict(zip(file_list_tracking, listOfFiles)) 
print (fridge_storage_map)

#TRACKING-loop that extracts all files recursively from path = folder_to_track and adds the files to the above empty placeholder list
for path, folders, files in os.walk(folder_to_track):
    for file in files:
        if file != ".DS_Store":
            file_list_tracking.append(file)    
#print(file_list_tracking)"""


#THIS PART creates a list (file_list_food) that contains unique files within the folder_to_track that should finally be moved to the folder_destination
#DESTINATION-loop that extracts all files recursively from path = folder_destination and adds the files to the above empty placeholder list (file_list_destination = [])
for path, folders, files in os.walk(folder_destination):
    for file in files:
        file_list_destination.append(file)


        
#Compares the two file lists generated (file_list_tracking, file_list_destination) and stores unique files in placeholder list (file_list_food)
#This lines of codes thus make sure no file that already exists in the destination_folder is replaced (or worse) during the final action which is the relocation of the fiules from tracking folder to destination folder...
a = set(file_list_tracking)
b = set(file_list_destination)
file_list_food = (a.difference(b))
print ("We are YUMMY treats, FEED us to the hungry monster:" + str(file_list_food))

#So far we have the following:
    # file_list_food = list containing all files unique within the directory "folder_to_track"
    # fridge_storage_map = dictionary storing the maps (paths) for all files stored within the directory "folder_to_track"
#We now can retrieve the specific storage paths of the unique files and implement the path (source_location) in the final function below to move (relocate) the files to the directory "folder_destination".

#THIS PART creates a function called "def move_files()" which moves the unique files within the directory "folder_to_track" into file-specific directories within folder_destination
#Example: the unique file "I am a YUMMY banana.doc" would be moved into the subfolder "Documents" within folder_destination
def move_files():
    for filename in file_list_food:
        if filename in fridge_storage_map:
            source_location = fridge_storage_map[filename]
            filename_extension = str(filename).split(".")[-1]
            #new_location = folder_destination + "/" + filename
            if filename_extension.lower() in ["mp4", "webm", "mkv", "flv", "avi", "wmv"]:
                new_location = folder_destination + "/Videos/" + filename
            elif filename_extension.lower() in ["mp3", "wav", "ogg", "m4a"]:
                new_location = folder_destination + "/Music/" + filename
            elif filename_extension.lower() in ["docx", "txt", "pub", "pptx", "xls", "doc"]:
                new_location = folder_destination + "/Documents/" + filename
            elif filename_extension.lower() in ["jpg", "jpeg", "gif", "png"]:
                new_location = folder_destination + "/Pictures/" + filename
            else:
                new_location = folder_destination + "/Others/" + filename
        os.rename(source_location, new_location)
        
#Executes the function move_files()
move_files()


#issue: if twice same file in folder to track but not any in folder destination what will hapen? overwritting?
