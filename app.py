# app.py — CÓDIGO VULNERÁVEL PARA FINS EDUCACIONAIS
# Este arquivo simula um login inseguro com SQL Injection
# NÃO use em produção

import sqlite3

def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'senha123')")
    conn.commit()
    conn.close()

def login_vulneravel(username, password):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    # VULNERABILIDADE: concatenação direta de input do usuário na query
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    print(f"Query executada: {query}")
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

# Teste normal
criar_banco()
print("=== Teste normal ===")
print("Login admin/senha123:", login_vulneravel("admin", "senha123"))

# Teste com SQL Injection
print("\n=== Teste com SQL Injection ===")
print("Login com payload:", login_vulneravel("admin' --", "qualquer"))
