## AutoDetail ERP — Sistema de Gestão para Estética Automotiva

Sistema ERP completo para gestão de estéticas automotivas, desenvolvido com FastAPI e PostgreSQL. Centraliza o controle de agendamentos, clientes, veículos, funcionários e financeiro em uma única plataforma.


**Projeto em desenvolvimento ativo**



## Funcionalidades implementadas


- [x] Rotas de autenticação de login utilizando schemas, login utilizando o formulário oauth2, cadastro, refresh token e change password
- [x] Dependência de verificação de token para validar usuários em rotas protegidas


## Planejadas


- [ ] Gestão financeira (receitas e despesas)
- [ ] Controle de estoque de produtos
- [ ] Relatórios financeiros por período
- [ ] Dashboard com indicadores da estética
- [ ] Histórico de serviços por veículo
- [ ] Controle de comissões por funcionário
- [ ] Notificações de agendamento
- [ ] Autenticação com JWT e OAuth2
- [ ] Cadastro de clientes, veículos e funcionários
- [ ] Sistema de agendamentos
- [ ] Cadastro de serviços oferecidos pela estética

## Tecnologias


| Tecnologia | Uso |
|------------|-----|
| Python | Linguagem principal |
| FastAPI | Framework web e API REST |
| PostgreSQL | Banco de dados relacional |
| SQLAlchemy | ORM para mapeamento das tabelas |
| Alembic | Migrações e versionamento do banco |
| JWT + OAuth2 | Autenticação e autorização |
| Pydantic | Validação de dados e schemas |


## Como rodar o projeto

**Pré-requisitos**


Python 3.10+
PostgreSQL instalado e rodando


## Instalação

**Clone o repositório**
`git clone https://github.com/gabrielsvgn/Car-Wash-ERP.git .`

**Entre na pasta principal**
`cd '..\Sistema Financeiro Estética Automotiva\'`

# Crie e ative o ambiente virtual
`python -m venv .venv`
`.venv\Scripts\activate`

# Instale as dependências
`pip install -r requirements.txt`

## Configuração

**Crie um arquivo .env na raiz com as seguintes variáveis:**

`DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco`
`SECRET_KEY=sua_chave_secreta`
`ALGORITHM=HS256`

## Banco de dados

**Aplique as migrations**

`alembic upgrade head`

## Rodando

`uvicorn main:app --reload`

**Acesse a documentação interativa em: http://localhost:8000/docs**