import os
import binascii
from backports.pbkdf2 import pbkdf2_hmac
import scrypt 

salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "p@$Sw0rD~1".encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32 )
print("Derived key: ", binascii.hexlify(key))




salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
passwd = b'p@$Sw0rD~7'
key = scrypt.hash(passwd, salt, 2048, 8, 1, 32)
print("Derived key:", key.hex())