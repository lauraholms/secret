# Encryption

The application uses symmetric AES encryption through the `cryptography` package.

Workflow

1. Authenticate
2. Encrypt note
3. Store encrypted data
4. Decrypt only when needed

No network communication is performed.
