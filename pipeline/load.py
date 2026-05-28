import pandas as pd
import logging

logger = logging.getLogger(__name__)

def carregar_dados_mysql(df, engine, nome_tabela="series_treino"):
    logger.info(f"Iniciando carga de dados no MySQL na tabela: {nome_tabela}")
    #replace usado pois o arquivo de entrada é sempre todo o histórico de treino
    try:
        df.to_sql(
            name=nome_tabela,
            con=engine,
            if_exists="replace",
            index=False
        )
        logger.info(f"Dados carregados com sucesso na tabela {nome_tabela}")
    except Exception as e:
        logger.error(f"Erro ao carregar dados no MySQL: {e}")
        raise e
