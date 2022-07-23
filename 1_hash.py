import hashlib
import binascii

from Crypto.Hash import keccak

text = 'hello'
data = text.encode("utf8")

sha224hash = hashlib.sha224(data).digest()
print("SHA-224: ", binascii.hexlify(sha224hash))

sha256hash =  hashlib.sha256(data).digest()
print("SHA-256: ", binascii.hexlify(sha256hash))

sha3_224hash = hashlib.sha3_224(data).digest()
print("SHA3_224: ", binascii.hexlify(sha3_224hash))

sha3_384hash =  hashlib.sha3_384(data).digest()
print("SHA3_384: ", binascii.hexlify(sha3_384hash))

keccak_384 =  keccak.new(data = b'hello', digest_bits = 384).digest()
print("Keccak384: ", binascii.hexlify(keccak_384))


whirlpool_512 =  whirlpool.new(data = b'hello', digest_bits = 384).digest()
print("Whirlpool: ", binascii.hexlify(whirlpool_512))