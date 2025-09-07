Meu Estoque: Sistema de Gerenciamento de Produtos

Descrição do Projeto

Este projeto é um sistema de gerenciamento de estoque desenvolvido como trabalho final para o módulo "Software Product: Analysis, Specification, Project & Implementation" da Faculdade Impacta Tecnologia. Ele oferece funcionalidades básicas para a gestão de produtos, incluindo cadastro, listagem, atualização de quantidade em estoque e desativação de produtos.

Funcionalidades

•
Cadastro de Produtos: Permite adicionar novos produtos ao estoque com informações como descrição, valor unitário, quantidade em estoque e fornecedor.

•
Listagem de Produtos: Exibe todos os produtos ativos no estoque, ordenados por código de produto.

•
Atualização de Estoque: Possibilita a modificação da quantidade em estoque de um produto existente.

•
Desativação de Produtos: Altera o status de um produto para inativo, removendo-o da visualização principal sem excluí-lo permanentemente do banco de dados.

Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

•
Python: Linguagem de programação principal.

•
Flask: Microframework web para Python, utilizado para construir a aplicação web.

•
Psycopg2: Adaptador PostgreSQL para Python, utilizado para interagir com o banco de dados PostgreSQL.

•
PostgreSQL (Neon.tech): Sistema de gerenciamento de banco de dados relacional, hospedado na plataforma Neon.tech para persistência dos dados.

•
HTML/CSS: Utilizados para a construção das interfaces de usuário (templates).

Estrutura do Projeto

O repositório está organizado da seguinte forma:

•
app.py: Contém a lógica principal da aplicação Flask, definindo as rotas e a interação com as funções de gerenciamento de produtos.

•
db.py: Responsável pela conexão com o banco de dados PostgreSQL, utilizando a string de conexão fornecida.

•
models.py: Define as funções de manipulação de dados (CRUD - Create, Read, Update, Delete) para os produtos no banco de dados.

•
templates/: Diretório que armazena os arquivos HTML (templates Jinja2) para as páginas da aplicação (base.html, cadastrar.html, listar.html).

•
README.md: O README original do projeto, com informações básicas.

•
requirements.txt: Arquivo que lista as dependências Python do projeto.

Configuração e Execução

Para configurar e executar o projeto localmente, siga os passos abaixo:

Pré-requisitos

•
Python 3.x instalado.

•
Acesso a um banco de dados PostgreSQL. Este projeto utiliza Neon.tech, mas pode ser adaptado para outras instâncias PostgreSQL.

Instalação das Dependências

Navegue até o diretório raiz do projeto no seu terminal e instale as dependências listadas no requirements.txt:

Bash


pip install -r requirements.txt


Configuração do Banco de Dados

O projeto está configurado para usar um banco de dados PostgreSQL hospedado no Neon.tech. A string de conexão está definida no arquivo db.py:

Python


conn_str = "postgresql://neondb_owner:npg_i3WyNPMKJzn7@ep-proud-rice-ac2xu92h-pooler.sa-east-1.aws.neon.tech/banco_pystock?sslmode=require&channel_binding=require"


Importante: Para usar este projeto, você precisará substituir npg_i3WyNPMKJzn7 pela sua própria senha de banco de dados e garantir que o banco de dados banco_pystock exista e tenha a tabela produto com a seguinte estrutura:

SQL






