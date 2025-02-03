from cryptography.fernet import Fernet


class EncryptionService():

    def __init__(self, key=Fernet.generate_key()):
        self.key = key
        self.fernet = Fernet(self.key)

    def get_key(self):
        return self.key

    def msg_encrypter(self, msg: str):
        """Encrypts the message"""
        encrypted_msg = self.fernet.encrypt(msg.encode())
        return encrypted_msg.decode()

    def msg_decrypter(self, encrypted_msg: str):
        """Decrypts the encrypted msg"""
        decrypted_msg = self.fernet.decrypt(encrypted_msg.encode())
        return decrypted_msg.decode()
