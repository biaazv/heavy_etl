from pipeline.extraction import ler_arquivo_csv
from pipeline.transformation import transformar_dados_hevy
from pipeline.load import carregar_dados_mysql
from config.database import obter_conexao_mysql

FONTE_DADOS = "data/workout_data.csv"
TABELA_DESTINO = "series_treino"


def executar_pipeline():
    print(f"HEVY WORKOUT INSIGHTS (ETL E ANATYLICS)")

    try:
        dados_brutos = ler_arquivo_csv(FONTE_DADOS)

        if dados_brutos is None:
            print(f"Falha na extração de dados")
            return

        if dados_brutos.empty:
            print(f"Não há dados para tratamento")
            return
        
        dados_tratados = transformar_dados_hevy(dados_brutos)

        print(f"Amostra de dados tratados")
        print(dados_tratados.head())    
        
        engine_banco = obter_conexao_mysql()
        carregar_dados_mysql(dados_tratados, engine_banco, TABELA_DESTINO)
    except Exception as e:
        print(f"Erro no pipeline: {e}")


if __name__ == "__main__":
    executar_pipeline()