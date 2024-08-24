from os import listdir
from os.path import isfile,join

def list_dir_tree(start_dir):
    for file in sorted(listdir(start_dir)):
        fullpath = join(start_dir,file)
        if isfile(fullpath):
            print(fullpath)
        else:
            list_dir_tree(fullpath)

list_dir_tree(".")