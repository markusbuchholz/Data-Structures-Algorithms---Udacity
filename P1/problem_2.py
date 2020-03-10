## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

files_in_folder = list()
# FOLDER = 'testdir'
# path = os.path.join( os.getcwd(), FOLDER)
# PATH = []
# PATH.append(path) 


def find_files(suffix, PATH):
    
    folder_paths = []

    if len(PATH) == 0:
        return files_in_folder
    else:    
        try:
            for i in range(len(PATH)):
                for item in os.listdir(PATH[i]):

                    if (os.path.isdir(os.path.join(PATH[i], item))):
                    # print("folder :: ", item)
                        folder_paths.append(os.path.join(PATH[i], item))
                    if (os.path.isfile(os.path.join(PATH[i], item))):
                        #if (item.find('.c'))> -1:
                        if item.endswith(suffix):
                            #print("file :: ", item)
                            files_in_folder.append((os.path.join(PATH[i], item)))
        except:
            print("wrong path ...")
            
    return find_files(suffix, folder_paths)
    #    print("folder_paths", folder_paths)


#print(find_files(PATH))
#print(find_files('./home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir'))
#print("files in folders :::", files_in_folder)


if __name__ == '__main__':

    def test_1():
        print("***********************************")
        path = []
        PATH = '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir'
        path.append(PATH)
        # print(find_files('.c', path))
        # ---------test prints
        # ['/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/t1.c',
        #  '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/subdir5/a.c',
        #  '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/subdir1/a.c',
        #   '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/subdir3/subsubdir1/b.c']
      

    def test_2():
        print("***********************************")
        path = []
        PATH = '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir'
        path.append(PATH)
        # print(find_files('.h', path))
        # ---------test prints
        # ['/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/t1.h',
        #  '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/subdir5/a.h',
        #   '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/subdir1/a.h',
        #    '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir/subdir3/subsubdir1/b.h']

    def test_3():
        print("***********************************")
        path = []
        PATH = '/home/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir'
        path.append(PATH)
        # print(find_files('.123', path)
        # ---------test prints
        # []

    def test_4():
        print("***********************************")
        path = []
        PATH = '/home1/markus/dsa/Data-Structures-Algorithms---Udacity/P1/testdir'
        path.append(PATH)
        # print(find_files('.c', path))
        # ---------test prints
        # wrong path ...
        # []

    test_1()
    test_2()
    test_3()
    test_4()



