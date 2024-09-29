import base64

# Hexadecimal string
hex_string = "<Your Certificate Thumbprint>"

# Convert hex to bytes
byte_data = bytes.fromhex(hex_string)

# Base64 URL encode the byte data
base64_url_encoded = base64.urlsafe_b64encode(byte_data).decode('utf-8').rstrip('=')

print("Base64 URL Encoded:", base64_url_encoded)