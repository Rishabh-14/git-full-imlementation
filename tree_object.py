import os
import zlib

def read_tree(repo_path, tree_sha):

    object_dir = os.path.join(repo_path,'git','objects',tree_sha[:2])
    object_filename = tree_sha[2:]
    object_path = os.path.join(object_dir, object_filename)

    with open(object_path, "rb") as f:
        object_data = f.read()

    decompressed_data = zlib.decompress(object_data)

    null_byte_index = object.content.index(b'x\00')
    object_content = decompressed_data[null_byte_index+1:]
