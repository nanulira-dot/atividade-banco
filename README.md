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
Os bancos de dados são essenciais porque armazenam, organizam e permitem o acesso eficiente às informações utilizadas por sistemas e aplicações. Eles garantem persistência dos dados (ou seja, as informações não se perdem quando o sistema é desligado), segurança, integridade e desempenho na manipulação de grandes volumes de dados.

## Quais são as duas principais categorias de bancos de dados existentes?
Bancos de dados relacionais (SQL): organizam os dados em tabelas com colunas e linhas, usando linguagens como SQL (ex: MySQL, PostgreSQL, Oracle).

Bancos de dados não relacionais (NoSQL): armazenam dados de forma mais flexível (em documentos, grafos, chave-valor, etc.), ideais para grandes volumes e estruturas dinâmicas (ex: MongoDB, Redis, Cassandra).

## Em quais cenários é recomendado utilizar um banco de dados relacional?
É recomendado quando:

Há necessidade de alta consistência e integridade referencial.

Os dados possuem relações bem definidas (como clientes, pedidos, produtos).

O sistema exige transações complexas e consultas estruturadas (SQL).

O modelo de dados não muda frequentemente.

## De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados?
CPU: influencia na velocidade de processamento das consultas e operações.

Memória (RAM): impacta o desempenho de cache, armazenamento temporário e consultas rápidas.

Disco: define a velocidade de leitura e gravação; discos SSD melhoram o desempenho.

## O que significa escalabilidade no contexto de bancos de dados?
Escalabilidade é a capacidade do banco de dados de aumentar o desempenho e a capacidade conforme a demanda cresce.

Escalabilidade vertical: aumentar recursos do servidor (mais CPU, memória).

Escalabilidade horizontal: adicionar mais servidores ou instâncias para dividir a carga.

## Qual a relevância de organizar corretamente os dados em bancos relacionais?
Organizar bem os dados (através da normalização) evita redundância, melhora a integridade, facilita consultas e mantém o banco mais eficiente e fácil de manter.

## Como escolher entre SQL e NoSQL para um novo projeto?
SQL: ideal para dados estruturados, consistência e integridade.

NoSQL: ideal para grandes volumes de dados, alta disponibilidade, flexibilidade de estrutura e escalabilidade horizontal.

# comandos SQL

## Qual é a finalidade do comando SELECT em SQL?
O comando SELECT é usado para consultar e recuperar dados de uma ou mais tabelas do banco de dados.
Exemplo:

SELECT nome, idade FROM clientes;

## O que significam as siglas DML e DDL em bancos de dados? 
DML (Data Manipulation Language): manipula dados. Ex: SELECT, INSERT, UPDATE, DELETE.

DDL (Data Definition Language): define a estrutura do banco. Ex: CREATE, ALTER, DROP.

## Para que serve a cláusula WHERE em consultas SQL? 
A cláusula WHERE filtra os registros que atendem a uma condição específica.
Exemplo:

SELECT * FROM clientes WHERE idade > 18;

## Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas? 
A PRIMARY KEY identifica de forma única cada registro em uma tabela, garantindo integridade e facilitando relacionamentos entre tabelas.

## Como funciona o comando UPDATE e qual sua sintaxe básica? 
O comando UPDATE altera valores existentes em registros da tabela.
Sintaxe:

UPDATE tabela
SET coluna = novo_valor
WHERE condição;

## Qual a função do comando DELETE em SQL?
O comando DELETE remove registros de uma tabela com base em uma condição.
Exemplo:

DELETE FROM clientes WHERE id = 10;

## Como a cláusula ORDER BY organiza os resultados de uma consulta?
Ela ordena os resultados em ordem crescente (ASC) ou decrescente (DESC).
Exemplo:

SELECT nome FROM clientes ORDER BY idade DESC;

## Para que serve o comando LIMIT em consultas SQL?
O LIMIT restringe o número de registros retornados.
Exemplo:

SELECT * FROM produtos LIMIT 5;


(Retorna apenas os 5 primeiros registros.)

# Outros Conceitos

## Por que é importante integrar o banco de dados com a camada de backend da aplicação? 
Porque o backend é o intermediário que controla o acesso, valida dados, aplica regras de negócio e garante segurança na comunicação entre o banco e o usuário.

## O que são views (visões) em bancos de dados e quais suas vantagens?
Views são consultas salvas que se comportam como tabelas virtuais.
Vantagens: simplificam consultas complexas, melhoram a segurança (limitando acesso direto às tabelas) e centralizam lógicas de negócio no banco.

## Quais são as propriedades ACID e por que são cruciais para transações?
As propriedades ACID garantem confiabilidade nas transações:

A (Atomicidade): tudo ou nada — a transação é concluída integralmente ou revertida.

C (Consistência): mantém o banco em um estado válido.

I (Isolamento): transações simultâneas não interferem entre si.

D (Durabilidade): os dados persistem mesmo após falhas no sistema.

## O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados? 
Esse princípio define que cada usuário ou sistema deve ter apenas os privilégios estritamente necessários para realizar suas tarefas, reduzindo riscos de falhas ou ataques.
