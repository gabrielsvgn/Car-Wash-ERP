## AutoDetail ERP — Sistema de Gestão para Estética Automotiva

Sistema ERP para gestão de estéticas automotivas, desenvolvido com FastAPI e PostgreSQL. Centraliza o controle de agendamentos, clientes, veículos, funcionários e financeiro em uma única plataforma.


**Projeto em desenvolvimento ativo**



## Funcionalidades implementadas

### Rotas de Autenticação
- [x] Cadastro de usuários
- [x] Login utilizando JWT
- [x] Login via OAuth2 Password Flow para testes de API
- [x] Refresh Token
- [x] Alteração de senha
- [x] Proteção de rotas com autenticação
- [x] Proteção de rotas com autenticação de administrador

### Rotas de Veículos
- [x] CRUD de marca
- [x] CRUD de modelo
- [x] CRUD de veículo
- [x] Validação de placas duplicadas
- [x] Relacionamento entre marca, modelo e veículo

### Rotas de CEP
- [x] CRUD de cidade
- [x] CRUD de estado
- [x] Relacionamente entre cidade e estado

### Rotas de Usuários
- [x] Implementada a funcionalidade de gerenciamento de administradores
- [x] Implementada a funcionalidade de listar usuários da plataforma


## Planejadas


- [ ] Gestão financeira (receitas e despesas)
- [ ] Controle de estoque de produtos
- [ ] Relatórios financeiros por período
- [ ] Dashboard com indicadores da estética
- [ ] Histórico de serviços por veículo
- [ ] Controle de comissões por funcionário
- [ ] Notificações de agendamento
- [ ] Cadastro de clientes e funcionários
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

**Pré Requisitos**

- Docker Desktop instalado
- Git instalado

**1. Clone o respositório**
```
git clone https://github.com/gabrielsvgn/Car-Wash-ERP.git .
cd seu-repo
```

**2. Configure as variáveis de ambiente**
Crie um arquivo `.env` na raiz baseado no `.env.example`:
`cp .env.example .env`

Preencha o `.env` com suas credenciais
```
DATABASE_URL=postgresql://usuario:senha@db:5432/nome_do_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_EXPIRED_TOKEN=30
POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha
POSTGRES_DB=nome_do_banco
```

* **O host na DATABASE_URL deve ser sempre "db"!**

**3. Suba o projeto**
```
docker-compose up --build
```

O Docker vai automaticamente:
- ✅ Criar e inicializar o banco de dados PostgreSQL
- ✅ Rodar as migrations com Alembic
- ✅ Subir a API com Uvicorn

**4. Acesse a documentação**

http://localhost:8000/docs
