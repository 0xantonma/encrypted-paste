# Encrypted Paste
Send notes that are Fernet encrypted and will self-destroy after reading.

# What is Fernet?
Fernet is a symmetric encryption method which makes sure that the message encrypted cannot be manipulated/read without the key. It uses URL safe encoding for the keys. Fernet also uses 128-bit AES in CBC mode and PKCS7 padding, with HMAC using SHA256 for authentication.
