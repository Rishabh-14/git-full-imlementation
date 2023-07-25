from genericpath import isfile
import hashlib
import os
import zlib

def create_tree(repo_path, dir_path):
    items = os.listdir(dir_path)
    tree_content = b''

    for item in items:
        item_path = os.path.join(dir_path, item)

        if os.path.isfile(item_path):
            file_mode = '100644'
            file_type = 'blob'
        if os.path.isdir(item_path):
            file_mode = '040000'
            file_type = 'tree'
        else:
            continue
        
        