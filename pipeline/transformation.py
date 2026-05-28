import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transformar_dados_hevy(df):
    df_trab = df.copy()
    logger.info(f"Iniciando transformação dos dados")

    # Dicionário para traduzir os meses abreviados no Hevy
    traducao_meses = {
        "Jan": "Jan",
        "Fev": "Feb",
        "Mar": "Mar",   
        "Abr": "Apr",
        "Mai": "May",
        "Jun": "Jun",
        "Jul": "Jul",
        "Ago": "Aug",
        "Set": "Sep",
        "Out": "Oct",
        "Nov": "Nov",
        "Dez": "Dec"
    }

    for mes_pt, mes_en in list(traducao_meses.items()):
        df_trab['start_time'] = df_trab['start_time'].str.replace(mes_pt, mes_en, regex=False)
        df_trab['end_time'] = df_trab['end_time'].str.replace(mes_pt, mes_en, regex=False)
    
    mascara_data = "%d %b %Y, %H:%M"
    df_trab["start_time_limpo"] = pd.to_datetime(
        df_trab["start_time"], format = mascara_data
    )
    
    df_trab["end_time_limpo"] = pd.to_datetime(
        df_trab["end_time"], format = mascara_data
    )

    logger.info(f"Transformação concluída com sucesso")
    return df_trab
