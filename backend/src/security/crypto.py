import cryptocode

def encrypt_data(data, password='12345'):
    encrypted_data = data
    return cryptocode.encrypt(encrypted_data, password)

def decrypt_data(encrypted_data, password='12345'):
    decrypted_data = encrypted_data
    return cryptocode.decrypt(decrypted_data, password)