from cryptography.fernet import Fernet

class Fakestr(str):
    def __str__(self):
        return "******"
    def __repr__(self):
        return "*%^&&&&&&&"
def load_key():
    return open ("secret.key","rb").read()

def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())


def decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    decrypted=f.decrypt(encrypted_password).decode()
    return Fakestr(decrypted)
    
    
    
def get_decrypted_password():
    encrypted_password=b'gAAAAABp39LfYKWiW9uefhQJ2L4lKIpilDydr7gIOyFiWt0GyeyS7peY6DhOPX8mpVjOcKH3_BI0dv13X1F_LXjDEtSP7j2EAw=='
    return decrypt_password(encrypted_password)
    