import pandas as pd
import pytest
from pipeline.transformation import transformar_dados_hevy

def test_transformar_dados_hevy_traducao_meses():
    # Dados de entrada com todos os meses em português conforme o dicionário em transformation.py
    # Formato esperado: "%d %b %Y, %H:%M"
    dados = {
        "start_time": [
            "01 Jan 2023, 10:00",
            "02 Fev 2023, 11:00",
            "03 Mar 2023, 12:00",
            "04 Abr 2023, 13:00",
            "05 Mai 2023, 14:00",
            "06 Jun 2023, 15:00",
            "07 Jul 2023, 16:00",
            "08 Ago 2023, 17:00",
            "09 Set 2023, 18:00",
            "10 Out 2023, 19:00",
            "11 Nov 2023, 20:00",
            "12 Dez 2023, 21:00"
        ],
        "end_time": [
            "01 Jan 2023, 11:00",
            "02 Fev 2023, 12:00",
            "03 Mar 2023, 13:00",
            "04 Abr 2023, 14:00",
            "05 Mai 2023, 15:00",
            "06 Jun 2023, 16:00",
            "07 Jul 2023, 17:00",
            "08 Ago 2023, 18:00",
            "09 Set 2023, 19:00",
            "10 Out 2023, 20:00",
            "11 Nov 2023, 21:00",
            "12 Dez 2023, 22:00"
        ]
    }
    df_input = pd.DataFrame(dados)

    # Executa a transformação
    df_output = transformar_dados_hevy(df_input)

    # Verifica se as colunas limpas foram criadas
    assert "start_time_limpo" in df_output.columns
    assert "end_time_limpo" in df_output.columns

    # Verifica se o tipo é datetime64[ns]
    assert pd.api.types.is_datetime64_any_dtype(df_output["start_time_limpo"])
    assert pd.api.types.is_datetime64_any_dtype(df_output["end_time_limpo"])

    # Verifica conversões específicas
    # Jan -> Jan
    assert df_output.loc[0, "start_time_limpo"] == pd.Timestamp(2023, 1, 1, 10, 0)
    # Mai -> May
    assert df_output.loc[4, "start_time_limpo"] == pd.Timestamp(2023, 5, 5, 14, 0)
    # Dez -> Dec
    assert df_output.loc[11, "start_time_limpo"] == pd.Timestamp(2023, 12, 12, 21, 0)

def test_transformar_dados_hevy_dataframe_vazio():
    df_input = pd.DataFrame(columns=["start_time", "end_time"])
    df_output = transformar_dados_hevy(df_input)

    assert df_output.empty
    assert "start_time_limpo" in df_output.columns
    assert "end_time_limpo" in df_output.columns
