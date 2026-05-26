import os
import pandas as pd

WORKOUT_DATA = "workout_data.csv"
def ler_arquivo_csv(dados_entrada):
    if not os.path.exists(dados_entrada):
        raise FileNotFoundError(f"Arquivo {dados_entrada} não encontrado.")
    
    print(f"Carregando o arquivo CSV: {dados_entrada}")

    try:
        df_bruto = pd.read_csv(dados_entrada, sep=',', encoding='utf-8')
        print(f"Arquivo lido com sucesso")
        print(df_bruto.head())
        return df_bruto
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None