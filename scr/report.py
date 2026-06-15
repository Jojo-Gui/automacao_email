import pandas as pd

def ler_dados_tratados(df_limpo):
    # Carrega base de dados limpa
    df = pd.read_parquet(df_limpo)
    return df

#def metricas(df_limpo):
    # Cálcula KPIs e retorna um dicionário com os resultados
    





if __name__ == "__main__":
    print("Iniciando o teste do módulo report.py...")

    df_limpo = ler_dados_tratados('data\\amazon_tratada.parquet')
#    resumo_dados = metricas(df_limpo)