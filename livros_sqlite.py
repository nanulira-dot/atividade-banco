# =========================================
# Aula prática: Banco de Dados com SQLite
# =========================================

import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

print("✅ Banco de dados criado/conectado com sucesso!\n")

# 1 criar tabela Livros
cursor.execute("""
CREATE TABLE IF NOT EXISTS Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    autor TEXT,
    ano INTEGER,
    genero TEXT,
    disponivel INTEGER
)
""")
print("📘 Tabela 'Livros' criada com sucesso!\n")

# 2 inserir múltiplos livros
livros = [
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Fábula", 1),
    ("Dom Casmurro", "Machado de Assis", 1899, "Romance", 1),
    ("1984", "George Orwell", 1949, "Distopia", 0),
    ("Harry Potter", "J.K. Rowling", 1997, "Fantasia", 1),
    ("É assim que começa", "Collen Hoover", 2022, "Romance", 1)
]

# 3 inserir múltiplos livros
cursor.executemany("""
INSERT OR IGNORE INTO Livros (titulo, autor, ano, genero, disponivel)
VALUES (?, ?, ?, ?, ?)
""", livros)
conn.commit()
print("📚 Livros inseridos com sucesso!\n")

# 4 consultar todos os livros
print("📖 Livros disponíveis: ")
for row in cursor.execute("SELECT * FROM Livros WHERE disponivel = 1"):
    print(row)
print()

cursor.execute("UPDATE Livros SET disponivel = ? WHERE titulo = ?", (0, 'Harry Potter'))
conn.commit()
print("🔄 Atualização concluída: 'Harry Potter' agora está indisponível.")

# 6 ordenar livros do mais novo pro mais antigo
print("📅 Livros do mais recente ao mais antigo: ")
for row in cursor.execute("SELECT titulo, ano FROM Livros ORDER BY ano DESC"):
    print(row)
print()

# 7 deletar livro antigo (antes de 1940
cursor.execute("DELETE FROM Livros WHERE ano < 1940")
conn.commit()
print("🗑️  Livros antigos (antes de 1940) removidos!\n")

# 8 criar tabela Usuario
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")
print("👤 Tabela 'Usuario' criada!\n")

# 9 alterar tabela Usuario para adicionar coluna idade
cursor.execute("ALTER TABLE Usuario ADD COLUMN idade INTEGER")
print("Campo 'idade' adicionado à tabela Usuario!\n")

# 10 inserir 5 usuários
usuarios = [
    ("Naiumy", 18),
    ("Gabriel", 19),
    ("Ryan", 20),
    ("Rafael", 25),
    ("Camila", 19)
]
cursor.executemany("INSERT INTO Usuario (nome, idade) VALUES (?, ?)", usuarios)
conn.commit()
print("👥 Usuários inseridos com sucesso!\n")

# 11 apagar tabela Usuario
cursor.execute("DROP TABLE Usuario")
conn.commit()
print("❌ Tabela 'Usuario' apagada com sucesso!\n")

# Fechar conexão
conn.close()
print("🔒 Conexão com o banco de dados fechada.")


