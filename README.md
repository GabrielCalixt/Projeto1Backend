# 🏠 Imobly — API de Gerenciamento de Imóveis

> Backend da plataforma **Imobly**: um serviço RESTful para cadastro, consulta e remoção de imóveis e seus respectivos proprietários.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints da API](#endpoints-da-api)
- [Como Executar](#como-executar)
- [Documentação Interativa](#documentação-interativa)

---

## Sobre o Projeto

A **Imobly** é uma API desenvolvida em Python com Flask, voltada para o gerenciamento de imóveis e proprietários. Ela permite consolidar os dados necessários para operações imobiliárias, oferecendo endpoints simples e bem documentados para integração com qualquer frontend ou cliente HTTP.

---

## Funcionalidades

### Imóveis (Properties)
- **Cadastrar** um novo imóvel com título, valor, tipo, endereço, status, área, número de quartos, banheiros e proprietário
- **Listar** todos os imóveis cadastrados na base de dados
- **Remover** um imóvel pelo título

### Proprietários (Owners)
- **Cadastrar** um novo proprietário com nome, e-mail e telefone
- **Listar** todos os proprietários cadastrados na base de dados

### Gerais
- Documentação interativa automática via **Swagger UI** (acessível em `/openapi`)
- Suporte a **CORS**, permitindo integração com frontends de diferentes origens
- Validação de dados com **Pydantic**
- Persistência em banco de dados via **SQLAlchemy**

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| Python | 3.x | Linguagem principal |
| Flask | 3.1.3 | Framework web |
| flask-openapi3 | 4.3.1 | Documentação Swagger automática |
| Flask-SQLAlchemy | 3.1.1 | ORM para banco de dados |
| SQLAlchemy | 2.0.48 | Mapeamento objeto-relacional |
| Pydantic | 2.12.5 | Validação de schemas |
| flask-cors | 6.0.2 | Suporte a Cross-Origin Resource Sharing |

---

## Estrutura do Projeto

```
Projeto1Backend/
├── app.py              # Ponto de entrada da aplicação e definição das rotas
├── logger.py           # Configuração do sistema de logging
├── requirements.txt    # Dependências do projeto
├── model/              # Modelos de dados (Property, Owner) e configuração do banco
└── schemas/            # Schemas de validação e serialização (Pydantic)
```

---

## Endpoints da API

### 🏘️ Imóveis — `/property`

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/property` | Cadastra um novo imóvel |
| `GET` | `/property` | Lista todos os imóveis |
| `DELETE` | `/property` | Remove um imóvel pelo título |

**Campos do imóvel:**
- `title` — Título/nome do imóvel
- `value` — Valor do imóvel
- `type` — Tipo (ex: casa, apartamento, terreno)
- `owner_id` — ID do proprietário vinculado
- `address` — Endereço completo
- `status` — Status (ex: disponível, alugado, vendido)
- `area` — Área em m²
- `rooms` — Número de quartos
- `bathrooms` — Número de banheiros

---

### 👤 Proprietários — `/owner`

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/owner` | Cadastra um novo proprietário |
| `GET` | `/owner` | Lista todos os proprietários |

**Campos do proprietário:**
- `name` — Nome completo
- `email` — Endereço de e-mail
- `phone` — Telefone de contato

---

## Como Executar

### Pré-requisitos

- Python 3.x instalado
- Recomenda-se o uso de um ambiente virtual ([venv](https://docs.python.org/3/library/venv.html))

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/GabrielCalixt/Projeto1Backend.git
cd Projeto1Backend
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv env

# Windows
env\Scripts\activate

# Linux / macOS
source env/bin/activate
```

**3. Instale as dependências:**
```bash
(env)$ pip install -r requirements.txt
```

**4. Execute a API:**
```bash
(env)$ flask run --host 0.0.0.0 --port 8888
```

**Modo desenvolvimento** (reinicia automaticamente ao salvar alterações):
```bash
(env)$ flask run --host 0.0.0.0 --port 8888 --reload
```

---

## Documentação Interativa

Com a API em execução, acesse a documentação Swagger no navegador:

```
http://localhost:8888/openapi
```

A documentação é gerada automaticamente e permite testar todos os endpoints diretamente pela interface.

---

## Respostas e Códigos HTTP

| Código | Significado |
|---|---|
| `200` | Operação realizada com sucesso |
| `400` | Erro inesperado ao processar a requisição |
| `404` | Recurso não encontrado |
| `409` | Conflito — registro duplicado na base de dados |