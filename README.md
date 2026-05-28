# 🏋️‍♂️ Hevy Workout Analytics Pipeline (ETL)

Este é um pipeline de Engenharia de Dados focado na extração, tratamento e armazenamento de históricos de treinos exportados do aplicativo Hevy. O projeto processa os dados brutos, aplica regras de limpeza e padronização de tipos de dados, e persiste as informações em um banco de dados relacional para futuras análises de performance física.

## 🏗️ Arquitetura e Tecnologias Utilizadas

- **Python 3.10+**: Linguagem base do projeto.
- **Pandas**: Biblioteca para extração, manipulação e transformação dos dados.
- **Docker & Docker Compose**: Criação e isolamento do ambiente de banco de dados.
- **MySQL 8.0**: Banco de dados relacional para persistência dos dados de treino.
- **SQLAlchemy & PyMySQL**: Ferramentas de conexão e ORM para comunicação entre Python e MySQL.

## 📂 Estrutura do Projeto

```text
├── config/
│   └── database.py        # Configuração da engine de conexão do MySQL
├── pipeline/
│   ├── __init__.py        
│   ├── extraction.py      # Módulo de leitura de arquivos (CSV)
│   ├── transformation.py  # Módulo de limpeza e tratamento de tipos
│   └── load.py            # Módulo de carga de dados para o MySQL
├── data/
│   └── treinos_hevy.csv   # Arquivo fonte de dados (omitido no Git)
├── docker-compose.yml     # Definição do container MySQL
├── requirements.txt       # Dependências do projeto
└── main.py                # Orquestrador do pipeline ETL
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente, subir a infraestrutura e rodar o pipeline ETL completo.

### 1. Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
* **Python 3.10 ou superior**
* **Docker Desktop** ativo e rodando

---

### 2. Configuração da Infraestrutura (MySQL via Docker)

Abra o seu terminal (Prompt de Comando ou PowerShell no Windows) na raiz do projeto e execute o comando abaixo para iniciar o banco de dados em segundo plano:

```bash
docker compose up -d
```

---

## 🤖 Uso do Jules

Este projeto suporta o uso do agente de codificação Jules. Se você deseja utilizar o Jules e encontrou problemas na instalação (como o erro `npm: command not found`), consulte o nosso tutorial dedicado:

👉 **[Como instalar e configurar o Jules](./JULES_SETUP.md)**