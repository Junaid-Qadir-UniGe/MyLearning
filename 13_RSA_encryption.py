from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


# RSA Key Generation
keypair = RSA.generate(3072)

pubkey = keypair.publickey()
print(f"Public Key: (n = {hex(pubkey.n)}, e={hex(pubkey.e)})") 
pubkeyPEM = pubkey.exportKey()
print(pubkeyPEM.decode('ascii'))


print(f"Private key: (n = {hex(pubkey.n)}, d={hex(keypair.d)})")
privatekeyPEM = keypair.exportKey()
print(privatekeyPEM.decode('ascii'))


# RSA Encryption
msg = b'Junaid Qadir'
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

# RSA Decryption 
decryptor = PKCS1_OAEP.new(keypair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)


