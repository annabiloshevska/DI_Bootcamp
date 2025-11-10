from utils import unzip_with_7z
import os


zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

print(os.path.exists(zip_file_path))
find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
found = False
for i in letters:
    for j in letters:
        find_me = f"{i}{j}"
        secret_password = find_me + "bcmpda"
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print('password found')
            break