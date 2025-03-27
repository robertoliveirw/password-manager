import psycopg2

def get_connection():
    return psycopg2.connect(
        database="bot_senha",
        host="localhost",
        user="postgres",
        password='1234',
        port="5432"  
    )