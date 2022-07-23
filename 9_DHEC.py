import pyDHE

alice = pyDHE.new()
alicePubKey = alice.getPublicKey()
print("Alice public key: ", hex(alicePubKey))


bob = pyDHE.new()
bobPubKey = bob.getPublicKey()
print("Bob public key: ", hex(bobPubKey))

print("Now exchange the public key (e.g. through Internet)")


aliceSharedKey = alice.update(bobPubKey)
print("Alice share key: ", hex(aliceSharedKey))

bobSharedKey = bob.update(alicePubKey)
print("Bob shared key: ", hex(bobSharedKey))

print("Equal shared keys: ", aliceSharedKey == bobSharedKey)
