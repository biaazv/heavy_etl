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
│   └── workout_data.csv   # Arquivo fonte de dados (omitido no Git)
├── docker-compose.yml     # Definição do container MySQL
├── requirements.txt       # Dependências do projeto
└── main.py                # Orquestrador do pipeline ETL
```

## 🧠 Funcionamento Lógico do Pipeline

O pipeline segue o fluxo clássico de Engenharia de Dados (ETL):

1. **Extração (`extraction.py`)**: O módulo lê os dados brutos a partir do arquivo CSV localizado em `data/workout_data.csv`. Ele realiza uma validação inicial para garantir que o arquivo existe antes de carregá-lo em um DataFrame Pandas.
2. **Transformação (`transformation.py`)**: Esta é a etapa central do pipeline. Aqui, os dados passam por uma limpeza e padronização. Um ponto crítico é a **tradução de meses**, onde abreviações em português (como "Mai" ou "Dez") são convertidas para inglês, permitindo que o Pandas interprete corretamente as colunas de data e hora.
3. **Carga (`load.py`)**: Os dados processados são enviados para o banco de dados MySQL utilizando SQLAlchemy. A estratégia de carga atual é de substituição completa (`replace`), garantindo que o banco reflita sempre o estado mais recente do arquivo de exportação.

## 📊 Esquema de Dados (CSV)

Para o funcionamento correto do pipeline, o arquivo `workout_data.csv` deve conter, no mínimo, as seguintes colunas:

- `start_time`: Data e hora de início do treino.
- `end_time`: Data e hora de fim do treino.

### Lógica de Tradução e Formatação
O pipeline espera que as datas estejam no formato `%d %b %Y, %H:%M` (ex: `5 Mai 2026, 07:34`).
Devido às variações de idioma na exportação, aplicamos a seguinte tradução para os meses:
- **Jan** -> Jan, **Fev** -> Feb, **Mar** -> Mar, **Abr** -> Apr, **Mai** -> May, **Jun** -> Jun, **Jul** -> Jul, **Ago** -> Aug, **Set** -> Sep, **Out** -> Oct, **Nov** -> Nov, **Dez** -> Dec.

---

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
