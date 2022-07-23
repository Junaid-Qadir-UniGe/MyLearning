import hashlib, time

startseed = str(time.time()) + '|'
min = 1
max = 10

for i in range(5):
    nextseed = startseed + str(i)
    hash = hashlib.sha256(nextseed.encode('ascii')).digest()
    bigrand = int.from_bytes(hash, 'big')
    rand = min + bigrand % (max-min +1)
    print(nextseed, bigrand, '-->', rand)

