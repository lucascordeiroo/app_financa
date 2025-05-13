import sqlite3

def conectar():
    return sqlite3.connect("financeiro.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def adicionar_transacao(descricao, valor, tipo, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transacoes (descricao, valor, tipo, data) VALUES (?, ?, ?, ?)", 
                   (descricao, valor, tipo, data))
    conn.commit()
    conn.close()

def listar_transacoes(mes=None, ano=None):
    conn = conectar()
    cursor = conn.cursor()

    if mes and ano:
        cursor.execute("""
            SELECT * FROM transacoes 
            WHERE strftime('%m', data) = ? AND strftime('%Y', data) = ?
            ORDER BY data DESC
        """, (f"{int(mes):02}", str(ano)))
    else:
        cursor.execute("SELECT * FROM transacoes ORDER BY data DESC")

    transacoes = cursor.fetchall()
    conn.close()
    return transacoes


def calcular_saldo(transacoes):
    saldo = 0
    for t in transacoes:
        if t[3] == 'entrada':
            saldo += t[2]
        elif t[3] == 'saida':
            saldo -= t[2]
    return saldo
