import os
import zlib

def read_blob(repo_path,blob_sha):
    object_dir = os.path.join(repo_path, '.git', 'objects', blob_sha[0:2])
    object_filename = blob_sha[2:]
    object_path = os.path.join(object_dir, object_filename)

    with open(object_path, "rb") as f:
        object_data = f.read()
    
    decompressed_data = zlib.decompress(object_data)

    null_byte_index = decompressed_data.index(b'\x00')
    object_data = decompressed_data[null_byte_index + 1:]

    return object_data.decode('utf-8')

repo_path = "/mnt/c/Users/Rishabh/OneDrive/Desktop/github/git-full-imlementation"  # replace with your repository path
blob_sha = "50262eafc16e0d7b0b0e7428d09f2ab8a791fa62"  # replace with your blob SHA

# Call the function and print the content of the blob
print(read_blob(repo_path, blob_sha))
