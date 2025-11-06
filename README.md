# Atividade Banco de Dados – Naiumy Lira SQLite + Python

Explicação do Código
# Descrição resumida

Este projeto tem como objetivo praticar comandos SQL usando Python e SQLite, simulando o funcionamento de uma livraria.
O sistema permite criar tabelas, inserir dados, atualizar informações, consultar registros, deletar dados e manipular tabelas de forma simples e didática.

Foram criadas duas tabelas:

Livros, para armazenar informações sobre os livros cadastrados.

Usuário, para armazenar informações dos clientes (com nome e idade).

Cada comando SQL foi executado através da biblioteca sqlite3, que vem embutida no Python.

# Como executar o projeto

1. Ative o ambiente virtual

venv\Scripts\activate


2. Execute o código principal

python livros_sqlite.py


3. O programa criará automaticamente o arquivo livraria.db, que contém o banco de dados.

4. Para visualizar o conteúdo do banco:(Opcional)

sqlite3 livraria.db
.tables
SELECT * FROM Livros;

# Estrutura das tabelas criadas
📘 Tabela Livros
Coluna	Tipo	Descrição
id	INTEGER 	Identificador único
titulo	TEXT	Nome do livro
autor	TEXT	Autor do livro
ano	INTEGER	    Ano de publicação
genero	TEXT	Gênero literário
disponivel	INTEGER	1 = disponível / 0 = indisponível

👤 Tabela Usuario
Coluna	Tipo	Descrição
id	INTEGER 	Identificador único
nome	TEXT	Nome do usuário
idade	INTEGER	Idade do usuário