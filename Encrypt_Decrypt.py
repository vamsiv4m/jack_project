from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
class Encrypt_Decrypt:
    def __init__(self,passwd=b"Madhuri@0119"):
        encrypasswd=cipher_suite.encrypt(passwd)
        self.passwd=encrypasswd

    def get_decode(self):
        decoded_text = cipher_suite.decrypt(self.get_encode()).decode()
        self.passwd=decoded_text
        return self.passwd

    def get_encode(self):
        return self.passwd
