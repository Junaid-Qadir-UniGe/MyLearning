import pyaes
import pbkdf2
import binascii 
import os
import secrets 


# Derive a 256-bits AES encryption key from the password 

password = "s3cr3t*cod3"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key: ', binascii.hexlify(key))