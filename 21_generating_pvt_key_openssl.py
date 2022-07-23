from OpenSSL import crypto
import os
import boto3

thing_name = "TestThing001"

key = crypto.PKey()

# I suggest using at least 4096 bit key
key.generate_key(crypto.TYPE_RSA, 4096)

# to protect the Private Key on the filesystem it should be readable only by the user that generated it
# mode=0o400 sets proper permissions
with open(os.open(f"{thing_name}.key", os.O_CREAT | os.O_WRONLY, mode=0o400),'w') as f:
     f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode("utf-8"))

csr = crypto.X509Req()

# Common Name (CN) should be equal to the Name of the IoT Device
csr.get_subject().CN = thing_name
csr.set_pubkey(key)
csr.sign(key, "sha512")

# the CSR is not confidential, so we do not have to restrict the file permissions
with open(f"{thing_name}.csr","w") as f:
    f.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr).decode("utf-8"))


# A session manages state about a particular configuration.
# I recommend you specify profile and region - that is a good development practice.
session = boto3.Session(profile_name='train',region_name='eu-west-1')

# Obtain the IoT Client.
iot_c = session.client('iot')

# create the certificate based on CSR and set it to Active state
r = iot_c.create_certificate_from_csr(
    certificateSigningRequest=crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr).decode("utf-8"),
    setAsActive=True
)
