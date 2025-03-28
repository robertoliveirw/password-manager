from database.database import get_connection
from security.crypto import decrypt_data

# Escrever add_sql() e search_sql()
# (usando a conexão centralizada)

def add_sql(aplicacao, encripted_usuario, encripted_email, encripted_senha):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
        query = """ INSERT INTO senhas_db_1 (aplicacao, usuario, email, senha) VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (aplicacao, encripted_usuario, encripted_email, encripted_senha))
        conexao.commit()
        print("Dados inseridos com sucesso!")

        cursor.close()
        conexao.close()
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def return_sql(aplicacao_desejada):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
    
        query = """
        SELECT aplicacao, usuario, email, senha 
        FROM senhas_db_1
        WHERE LOWER(aplicacao) = LOWER(%s);
        """

        cursor.execute(query, (aplicacao_desejada,))
        resultado = cursor.fetchone()
        
        if resultado:
            aplicacao, encripted_usuario, encripted_email, encripted_senha = resultado
            usuario = decrypt_data(encripted_usuario)
            email = decrypt_data(encripted_email)
            senha = decrypt_data(encripted_senha)

            print(f"Aplicativo: {aplicacao}\nUsuário: {usuario}\nE-mail: {email}\nSenha: {senha}")
        else:
            print(f"Aplicação '{aplicacao_desejada}' não encontrada.")

        cursor.close()
        conexao.close()
        
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

