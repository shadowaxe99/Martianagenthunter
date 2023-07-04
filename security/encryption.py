```python
from cryptography.fernet import Fernet

class EncryptionModule:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        # Convert data to bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif isinstance(data, dict):
            data = str(data).encode('utf-8')
        else:
            raise ValueError("Data type not supported for encryption")

        cipher_text = self.cipher_suite.encrypt(data)
        return cipher_text

    def decrypt_data(self, cipher_text):
        data = self.cipher_suite.decrypt(cipher_text)
        return data.decode('utf-8')
```