import logging
from config.logging_config import configurar_logging
from pipeline.extraction import ler_arquivo_csv
from pipeline.transformation import transformar_dados_hevy
from pipeline.load import carregar_dados_mysql
from config.database import obter_conexao_mysql

# Inicializa a configuração de logging
configurar_logging()
logger = logging.getLogger(__name__)

FONTE_DADOS = "data/workout_data.csv"
TABELA_DESTINO = "series_treino"


def executar_pipeline():
    logger.info("HEVY WORKOUT INSIGHTS (ETL E ANATYLICS) - Iniciando Pipeline")

    try:
        dados_brutos = ler_arquivo_csv(FONTE_DADOS)

        if dados_brutos is None:
            logger.error("Falha na extração de dados: O retorno foi nulo.")
            return

        if dados_brutos.empty:
            logger.warning("Não há dados para tratamento: O DataFrame está vazio.")
            return

        dados_tratados = transformar_dados_hevy(dados_brutos)

        logger.info("Amostra de dados tratados:")
        # Usamos o logger para exibir a amostra (pode ser convertido em string)
        logger.info(f"\n{dados_tratados.head()}")

        engine_banco = obter_conexao_mysql()
        carregar_dados_mysql(dados_tratados, engine_banco, TABELA_DESTINO)
        logger.info("Pipeline executado com sucesso!")

    except Exception as e:
        logger.error(f"Erro fatal no pipeline: {e}", exc_info=True)


if __name__ == "__main__":
    executar_pipeline()
