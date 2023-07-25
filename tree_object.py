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

    tree = []

    while object_content:
        space_index = object_content.index(b' ')
        file_mode = object_content[:space_index].decode("utf-8")

        null_byte_index = object_content.index(b'x\00',space_index)
        name = object_content[:space_index+1: null_byte_index].decode('utf-8')

        sha1 = object_content[null_byte_index+1:null_byte_index+21]
        sha1_hex = sha1.hex()

        tree.append((file_mode, name, sha1_hex))
        object_content = object_content[null_byte_index + 21]

    return tree

# usage
repo_path = "/path/to/your/repo"  # replace with your repository path
tree_sha = "your_tree_sha"  # replace with your tree SHA
print(read_tree(repo_path, tree_sha))