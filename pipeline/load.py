import pandas as pd

def carregar_dados_mysql(df, engine, nome_tabela):
    print(f"Carrega dados no MySQL")
    #replace usado pois o arquivo de entrada é sempre todo o histórico de treino
    try:
        if nome_tabela == "workout_data":
            estrategia = "append"
        else:
            estrategia = "replace"

        df.to_sql(
            name=nome_tabela,
            con=engine,
            if_exists=estrategia,
            index=False
        )
        print(f"Dados carregados com sucesso na tabela {nome_tabela}"
        )
    except Exception as e:
        print(f"Erro ao carregar dados no MySQL: {e}")
        raise e