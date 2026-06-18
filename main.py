# Trazendo as funções do arquivo report.py mailer.py
from scr.reader import arq_entrada, transformar_dados, salva_arq
from scr.report import ler_dados_tratados, metricas
from scr.mailer import gerar_html, enviar_email

if __name__ == "__main__":

    # Lendo caminho do .csv e o arquivo tratado .parquet
    caminho_csv = 'data\\amazon.csv'
    caminho_parquet = 'data\\amazon_tratada.parquet'

    #Lista com dos destinatários
    lista_de_emails = [
        'sdayane577@gmail.com',
        'leo.mlr06@gmail.com',
        'jpguidetti2@hotmail.com'        
    ]

    # tranforma a lista em texto
    lista_de_emails = ', '.join(lista_de_emails)

    # Lendo o arquivo .csv
    df = arq_entrada(caminho_csv)

    # Transformando os dados
    df_transformado = transformar_dados(df)

    # Salvando o arquivo tratado
    salva_arq(df_transformado)

    # Lendo o arquivo tratado
    df_tratado = ler_dados_tratados(caminho_parquet)

    # Gerando as métricas
    resumo_financeiro = metricas(df_tratado)

    # Gerando o HTML    
    html = gerar_html(resumo_financeiro)

    # Enviando o email
    enviar_email(html, lista_de_emails)