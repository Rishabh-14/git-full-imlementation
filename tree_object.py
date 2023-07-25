import os
import zlib

def read_tree(repo_path, tree_sha):

    object_dir = os.path.join(repo_path,'git','objects',tree_sha[:2])
    object_filename = tree_sha[2:]
    object_path = os.path.join(object_dir, object_filename)
