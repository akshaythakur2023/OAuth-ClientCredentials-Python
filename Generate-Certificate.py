from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta

#Open private key
with open("private_key.pem", "rb") as file1:
    private_key = serialization.load_pem_private_key(
        file1.read(),
        password=None,
        backend=default_backend()
    )

#Open Public Key
with open('public_key.pem', 'rb') as file2:
    public_key = serialization.load_pem_public_key(
        file2.read(),
        backend=default_backend()
    )

#Create subject for your certificate
subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"CA"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"<Province/State>"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"<City>"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"<Your Org name>"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"<Your FQDN>"),
])

issuer = subject  # Self-signed, so issuer is the same as subject

#create a certificate and store it in the object
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(public_key)
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now())
    .not_valid_after(datetime.now() + timedelta(days=365))  # Valid for 1 year
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    )
    .sign(private_key, hashes.SHA256(), default_backend())
)

# Save the certificate to a file
with open('certificate.pem', 'wb') as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Certificate generated and saved as 'certificate.pem'.")