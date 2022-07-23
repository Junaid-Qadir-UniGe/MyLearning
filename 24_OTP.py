import pyotp

import time
# Server Side Setup

base32secret = pyotp.random_base32()
print('Secret:', base32secret)

totp_uri = pyotp.totp.TOTP(base32secret).provisioning_uri(
    "alice@google.com",
    issuer_name="Secure App")
print(totp_uri)



#Client-Side Setup
base32secret = 'S3K3TPI5MYA2M67V'
print('Secret:', base32secret)

totp = pyotp.TOTP(base32secret)
print('OTP code:', totp.now())
time.sleep(30)
print('OTP code:', totp.now())


import pyotp

base32secret = 'S3K3TPI5MYA2M67V'
print('Secret:', base32secret)

totp = pyotp.TOTP(base32secret)
your_code = '123456'
print(totp.verify('Code Valid:', your_code))