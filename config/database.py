from sqlalchemy import create_engine
# Credenciais (No futuro, virão de variáveis de ambiente .env)
USER = "eng_dados"
PASSWORD = "senha_segura_123"
HOST = "127.0.0.1"
PORT = "3307"
DATABASE = "hevy_insights"

def obter_conexao_mysql():
    """Cria e retorna o motor de conexão com o banco de dados."""
    url_conexao = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    return create_engine(url_conexao)