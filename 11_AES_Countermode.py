import secrets
import pyaes
#import random
import os
import binascii



# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
key = os.urandom(32) 
iv = secrets.randbits(256)
plaintext = "Junaid"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted from the word "Junaid": ', binascii.hexlify(ciphertext))




# To decrypt the plaintext with the given
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)

print('Decrypted: ', decrypted)


#   # random decryption key
# aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
# print('Wrongly decrypted:', aes.decrypt(ciphertext))


