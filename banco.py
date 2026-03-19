import sqlite3

def conectar():
    conexao = sqlite3.connect("meu_banco.db")
    return conexao, conexao.cursor()

def criar_tabela():
    conexao, cursor = conectar()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_usuario(nome, email):
    conexao, cursor = conectar()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def deletar_usuario(id_usuario):
    conexao, cursor = conectar()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    conexao.close()

def atualizar_email(id_usuario, novo_email):
    conexao, cursor = conectar()
    cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (novo_email, id_usuario))
    conexao.commit()
    conexao.close()



def buscar_usuario(nome):
    conexao, cursor = conectar()
    # O '%' faz a busca ser flexível (antes e depois do nome)
    cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", (f'%{nome}%',))
    dados = cursor.fetchall()
    conexao.close()
    return dados

def exportar_dados():
    conexao,cursor = conectar()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall() # Aqui ele pega a lista completa
    conexao.close()
    return dados