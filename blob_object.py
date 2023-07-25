from bz2 import compress
import hashlib
import os
import zlib

def create_blob(repo_path,file_path):
    with open(file_path, "rb") as f:
        content = f.read()

    header = f"blob {len(content)}\x00".encode("utf-8")

    data = header + content
    sha1 = hashlib.sha1(data).hexdigest()

    object_dir = os.path.join(repo_path,'git','objects', sha1[:2])
    os.makedirs(object_dir, exist_ok = True)
    object_path = os.path.join(object_dir, sha1[2:])

    compressed_data = zlib.compress(data)

    with open(object_path, "wb") as f:
        f.write(compressed_data)
    
    return sha1

repo_path = "/mnt/c/Users/Rishabh/OneDrive/Desktop/github/git-full-imlementation"
file_path = "/mnt/c/Users/Rishabh/OneDrive/Desktop/github/git-full-imlementation/.git/objects/blob_test.txt"
print(create_blob(repo_path, file_path))

