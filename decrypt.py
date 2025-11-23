import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == 'encrypt.py' or file == 'thekey.key' or file == 'decrypt.py' or file == 'README.md':
        continue
    if os.path.isfile(file):
        files.append(file)


with open("thekey.key","rb") as key:
    decryptkey = key.read()


for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    decrypted_content = Fernet(decryptkey).decrypt(contents)

    with open(file, 'wb') as thefile:
        thefile.write(decrypted_content)