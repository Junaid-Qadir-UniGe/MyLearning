# import numpy as np
# import matplotlib.pyplot as plt
# xstart = -20
# xstop = 20
# increment = 0.1
# x = np.arange(xstart,xstop,increment)
# y = 2 * x*x + 20 * x - 22
# plt.plot(x,y)
# plt.grid()
# i = 0
# while y[i] > y[i+1]:
#     i = i+1


# print(x[i])
# print(y[i])
# plt.xlabel('x')
# # plt.ylabel('y')
# # plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# xstart = 0
# xstop = 2*np.pi
# increment = 0.1
# x = np.arange(xstart,xstop,increment)
# y = np.sin(x)
# plt.subplot(2,1,2)
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()
# plt.subplot(2,1,2)
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()


import datetime
import hashlib, binascii
sha3_256hash = hashlib.sha3_256(b'hello').digest()
print("SHA3-256('hello') =", binascii.hexlify(sha3_256hash))


import datetime
import hashlib
import binascii

sha3_256hash = hashlib.sha3_256(b'Junaid').digest()
print("SHA3-256('junaid') =", binascii.hexlify(sha3_256hash))