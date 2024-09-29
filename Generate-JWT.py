import datetime
from IPython.utils.tz import utcnow
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import jwt
import time

#Open Private Key
with open("private_key.pem", "rb") as file1:
    private_key = serialization.load_pem_private_key(
        file1.read(),
        password=None,
        backend=default_backend()
    )

#Headers for JWT
headers = {
    "alg": "RS256",
    "typ": "JWT",
    "x5t": "<Base64URLEncoded Certificate Thumbprint>"
}


current_time = int(time.time())
expiration_time = current_time + 3600

#Payload for JWT
payload_data = {
    "aud" : "https://login.microsoftonline.com/<Entra ID Tenant ID>/oauth2/v2.0/token",
    "exp": expiration_time,
    "iss": "<Application/Client ID>",
    "jti": "<Random Unique ID. It can be Application/Client ID>",
    "nbf": current_time,
    "sub": "<Application/Client ID>"
}

token=jwt.encode(
    payload=payload_data,
    key= private_key,
    algorithm='RS256',
    headers=headers
)

print(token)