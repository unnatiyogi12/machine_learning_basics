from pathlib import Path
import os


# show all the files and folders in the current directory
def readfileanfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
            print(f"{i+1}. File: {items}")
        

# used to create a file

def createfile():

    try:
        readfileanfolder()
        name = input("Enter the file name to be created: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter the data to be written to the file: ")
                fs.write(data)
            print(f"{name} created successfully")
        else:
            print(f"{name} already exists")
    except Exception as e:
        print(e)


# used to read a file

def readfile():
    try:
        readfileanfolder()
        name = input("Enter the file name to be read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p ,'r') as fs:
                data = fs.read()
                print(f"The content of the file is: {data}")
        else:
            print(f"{name} does not exist or is not a file")
    except Exception as e:
        print(e)


# used to update a file
def updatefile():
    try:
        readfileanfolder()
        name = input("Enter the file name to be updated: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1 for changing the name of the file")
            print("2 for overwriting the content of the file")
            print("3 for appending the content of the file")

            res = int(input("Enter your response:"))

            # used to rename the file
            if res == 1:
                name = input("Enter the new name of the file: ")
                newp = Path(name)
                p.rename(newp)
                print(f"{name} renamed successfully")

            # used to overwrite the content of the file
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter what you want to write to the file: ")
                    fs.write(data)
                print(f"{name} updated successfully")

            # used to append the content of the file
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Enter what you want to append to the file: ")
                    fs.write(data)
                print(f"{name} updated successfully")

    except Exception as e:
        print(e)


# used to delete a file
def deletefile():
    try:
        readfileanfolder()
        name = input("Enter the file name to be deleted: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print(f"{name} deleted successfully")
        else:   
            print(f"{name} does not exist or is not a file")
    except Exception as e:
        print(e)


# all the choices for the user to perform file handling operations
print("1 for creating a file")
print("2 for reading a file")   
print("3 for updating a file")
print("4 for deleting a file")
choice = int(input("Enter your choice: "))

if choice == 1:
    createfile()

if choice == 2:
    readfile()

if choice == 3:
    updatefile()

if choice == 4:
    deletefile()