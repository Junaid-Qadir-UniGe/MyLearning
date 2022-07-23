import hashlib, hmac, binascii

# mac = hmac.new(b'key', b'some msg', hashlib.sha256).digest()
# print(binascii.hexlify(mac))
# next_seed = MAC(salt, seed)
# HMAC(key, msg, hash_func)
def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()

key = b"12345"
msg = b"sample message"
print(binascii.hexlify(hmac_sha256(key, msg)))





def hmac_sha384(key, msg):
    return hmac.new(key, msg, hashlib.sha384).digest()

key = b"cryptography"
msg = b"hello"
print(binascii.hexlify(hmac_sha384(key, msg)))