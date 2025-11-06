# Atividade Banco de Dados – Naiumy Lira SQLite + Python

## Explicação do Código
Descrição resumida:

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
| Coluna      | Tipo      | Descrição                              |
|--------------|-----------|----------------------------------------|
| id           | INTEGER (PK) | Identificador único                   |
| titulo       | TEXT      | Nome do livro                          |
| autor        | TEXT      | Nome do autor                          |
| ano          | INTEGER   | Ano de publicação                      |
| genero       | TEXT      | Gênero literário                       |
| disponivel   | INTEGER   | 1 = disponível / 0 = indisponível      |

👤 Tabela Usuario

| Coluna | Tipo | Descrição |
|--------|------|------------|
| id     | INTEGER (PK) | Identificador do usuário |
| nome   | TEXT | Nome do usuário |
| idade  | INTEGER | Idade do usuário |


# Questões teóricas

## Por que os bancos de dados são essenciais em aplicações modernas?

## Quais são as duas principais categorias de bancos de dados existentes?

## Em quais cenários é recomendado utilizar um banco de dados relacional?

## De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados?

## O que significa escalabilidade no contexto de bancos de dados?

## Qual a relevância de organizar corretamente os dados em bancos relacionais?

## Como escolher entre SQL e NoSQL para um novo projeto?

# comandos SQL

## Qual é a finalidade do comando SELECT em SQL?

## O que significam as siglas DML e DDL em bancos de dados? 

## Para que serve a cláusula WHERE em consultas SQL? 

## Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas? 

## Como funciona o comando UPDATE e qual sua sintaxe básica? 

## Qual a função do comando DELETE em SQL?

## Como a cláusula ORDER BY organiza os resultados de uma consulta?

## Para que serve o comando LIMIT em consultas SQL?

# outros Conceitos

## Por que é importante integrar o banco de dados com a camada de backend da aplicação? 

## O que são views (visões) em bancos de dados e quais suas vantagens?

## Quais são as propriedades ACID e por que são cruciais para transações?

## O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados? 
