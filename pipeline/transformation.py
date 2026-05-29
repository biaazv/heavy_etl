import pandas as pd
import logging

logger = logging.getLogger(__name__)

TAXONOMIA_EXERCICIOS = {
    "Extensão de Tríceps na Polia (Máquina)": {"grupo": "Tríceps", "estimulo": "Empurrar"},
    "Rosca Direta na Polia": {"grupo": "Bíceps", "estimulo": "Puxar"},
    "Abdominal Na Máquina": {"grupo": "Core / Abdômen", "estimulo": "Isolados / Estabilização"},
    "Remada Baixa Iso-Lateral": {"grupo": "Costas", "estimulo": "Puxar"},
    "Desenvolvimento (Halter)": {"grupo": "Ombros", "estimulo": "Empurrar"},
    "Máquina De Fundos Sentado": {"grupo": "Peito", "estimulo": "Empurrar"},
    "Rosca Direta (Halter)": {"grupo": "Bíceps", "estimulo": "Puxar"},
    "Extensão Lombar Maquina": {"grupo": "Lombar", "estimulo": "Isolados / Estabilização"},
    "Elevação Lateral Unilateral (Cabo)": {"grupo": "Ombros", "estimulo": "Isolados / Estabilização"},
    "Barra Fixa Pronada Assistida": {"grupo": "Costas", "estimulo": "Puxar"},
    "Remadas Iso-Lateral (Máquina)": {"grupo": "Costas", "estimulo": "Puxar"},
    "Cadeira Flexora (Máquina)": {"grupo": "Posteriores de Coxa", "estimulo": "Membros Inferiores"},
    "Elevação Pélvica (Barra)": {"grupo": "Glúteos", "estimulo": "Membros Inferiores"},
    "Cadeira Extensora (Máquina)": {"grupo": "Quadríceps", "estimulo": "Membros Inferiores"},
}

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
