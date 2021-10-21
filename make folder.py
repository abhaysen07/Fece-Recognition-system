import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

newname=input("enter folder name")
bb="resizedTrainingImages/"
folder_name=bb+newname
print(folder_name)
# Example
createFolder(folder_name)