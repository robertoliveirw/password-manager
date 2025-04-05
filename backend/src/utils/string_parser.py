from security.crypto import encrypt_data

def string_parse(texto):
    palavras = texto.split()
    
    aplicacao = palavras[0] if len(palavras) > 0 else ""
    usuario = palavras[1] if len(palavras) > 1 else ""
    email = palavras[2] if len(palavras) > 2 else ""
    senha = palavras[3] if len(palavras) > 3 else ""
    
    encripted_usuario = encrypt_data(usuario)
    encripted_email = encrypt_data(email)
    encripted_senha = encrypt_data(senha)

    return aplicacao, encripted_usuario, encripted_email, encripted_senha