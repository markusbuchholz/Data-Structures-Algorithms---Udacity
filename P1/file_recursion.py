## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

files_in_folder = []
FOLDER = 'testdir'
path = os.path.join( os.getcwd(), FOLDER)
PATH = []
PATH.append(path) 
print("PATH :::", PATH) 
#print (os.path.isdir(path))
# Let us print the files in the directory in which you are running this script
#print (os.listdir("."))
#print (os.listdir(PATH))
def print_tree(PATH):
   # print("LENGTH ::", len(PATH))
    if len(PATH) == 0:
        return 0
    else:    
        folder_paths = []
        for i in range(len(PATH)):
            for item in os.listdir(PATH[i]):
               # print(PATH[i])
               # print("items :::", item)
    #        for sub_item in item:
                if (os.path.isdir(os.path.join(PATH[i], item))):
                    print("folder :: ", item)
                    folder_paths.append(os.path.join(PATH[i], item))
                if (os.path.isfile(os.path.join(PATH[i], item))):
                    #if (item.find('.c'))> -1:
                    if item.endswith(".c"):
                        print("file :: ", item)
                        files_in_folder.append((os.path.join(PATH[i], item)))
            
    return print_tree(folder_paths)
    #    print("folder_paths", folder_paths)


print_tree(PATH)
print("files in folders :::", files_in_folder)
     #   break
   # else:
    #    


# Let us check if this file is indeed a file!
#print (os.path.isfile("./ex.py"))

# Does the file end with .py?
#print ("./ex.py".endswith(".py"))

