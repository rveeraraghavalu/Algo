from collections import deque
from os import listdir
from os.path import isfile, join

def list_dir_tree(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir,file)
            if isfile(fullpath):
                print(fullpath)
            else:
                search_queue.append(fullpath)

list_dir_tree(".")
