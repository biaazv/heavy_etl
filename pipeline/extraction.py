import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

WORKOUT_DATA = "workout_data.csv"

def ler_arquivo_csv(dados_entrada):
    if not os.path.exists(dados_entrada):
        logger.error(f"Arquivo {dados_entrada} não encontrado.")
        raise FileNotFoundError(f"Arquivo {dados_entrada} não encontrado.")
    
    logger.info(f"Carregando o arquivo CSV: {dados_entrada}")

    try:
        df_bruto = pd.read_csv(dados_entrada, sep=',', encoding='utf-8')
        logger.info(f"Arquivo lido com sucesso. Total de linhas: {len(df_bruto)}")
        return df_bruto
    except Exception as e:
        logger.error(f"Erro ao ler o arquivo CSV: {e}")
        return None
