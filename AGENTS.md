# Instruções para Agentes (Jules)

Este arquivo contém diretrizes essenciais para que qualquer agente de IA (como o Jules) possa operar de forma eficiente neste repositório sem a necessidade de exploração manual repetitiva.

## 🚀 Contexto do Projeto
Este é um pipeline de Engenharia de Dados (ETL) para processar históricos de treinos do aplicativo **Hevy**.
- **Linguagem:** Python 3.10+
- **Bibliotecas Principais:** Pandas, SQLAlchemy, PyMySQL.
- **Infraestrutura:** MySQL 8.0 via Docker Compose.

## 🛠️ Regras de Desenvolvimento e Padrões
1. **Logging:** Não use `print()`. Utilize sempre o logger configurado em `config/logging_config.py`.
   - Importação: `import logging; logger = logging.getLogger(__name__)`
2. **Transformação de Datas:** O pipeline espera datas no formato `%d %b %Y, %H:%M`.
   - **IMPORTANTE:** Existe uma lógica de tradução de meses de Português (ex: Mai, Dez) para Inglês (May, Dec) em `pipeline/transformation.py`. Mantenha esta lógica ao adicionar novos tratamentos.
3. **Tratamento de Dados Vazios:** Se o CSV estiver vazio ou nulo, o pipeline deve logar um erro/aviso e encerrar graciosamente (implementado na branch `feat/logging...`).

## 📁 Estrutura de Arquivos Rápida
- `main.py`: Orquestrador principal.
- `pipeline/`: Contém os módulos `extraction.py`, `transformation.py` e `load.py`.
- `config/`: Configurações de banco de dados e logging.
- `data/`: Local do arquivo `workout_data.csv`.

## 🧪 Comandos Úteis
- Iniciar Banco: `docker compose up -d`
- Rodar Testes: `pytest`
- Rodar Pipeline: `python main.py`
