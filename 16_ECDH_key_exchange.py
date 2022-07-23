
from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n) #Alice generates a random ECC key pair: {alicePrivKey, alicePubKey = alicePrivKey * G}
alicePubKey = alicePrivKey * curve.g
print("Alice public key:", compress(alicePubKey)) 

bobPrivKey = secrets.randbelow(curve.field.n) # Bob generates a random ECC key pair: {bobPrivKey, bobPubKey = bobPrivKey * G}
bobPubKey = bobPrivKey * curve.g
print("Bob public key:", compress(bobPubKey))

print("Now exchange the public keys (e.g. through Internet)") #Alice and Bob exchange their public keys through the insecure channel (e.g. over Internet)

aliceSharedKey = alicePrivKey * bobPubKey #Alice calculates sharedKey = bobPubKey * alicePrivKey
print("Alice shared key:", compress(aliceSharedKey))

bobSharedKey = bobPrivKey * alicePubKey #Bob calculates sharedKey = alicePubKey * bobPrivKey
print("Bob shared key:", compress(bobSharedKey))

print("Equal shared keys:", aliceSharedKey == bobSharedKey) #Now both Alice and Bob have the same sharedKey == bobPubKey * alicePrivKey == alicePubKey * bobPrivKey