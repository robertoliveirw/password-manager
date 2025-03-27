import cryptocode

def encrypt_data(data, password='12345'):
    return cryptocode.encrypt(data, password)

def  decryppt_data(encrypted_data, password='12345'):
    dencrypted_data = encrypted_data
    return cryptocode.decrypt(dencrypted_data, password)