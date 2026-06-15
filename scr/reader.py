# IMPORTAÇÕES
import pandas as pd
import numpy as np

# CONFIGURAÇÕES GLOBAIS
pd.set_option('display.float_format', '{:.2f}'.format)
pd.set_option('display.max_columns', None)

# CARREGANDO ARQUIVO .CSV
def arq_entrada(base):

    dados = pd.read_csv(base, decimal=",")
    df = pd.DataFrame(dados)
    return df

# TRANSFORMANÇÕES
def transformar_dados(df):

    # Criando cópia
    df = df.copy()

    # Excluindo colunas que não serão necessárias
    df = df.drop(['product_link','img_link'],axis=1, errors='ignore')

    #Coletando somente as colunas que iremos mexer
    col_coin = ['discounted_price', 'actual_price', 'discount_percentage','rating_count']

    #Removendo $ e ,
    df[col_coin] = df[col_coin].apply(lambda x: x.str.replace(r',|₹|%','',regex=True))

    #Transformando as series (dados da coluna) em float
    df[col_coin] = df[col_coin].astype(float)

    #Convertendo % em número
    df['discount_percentage'] = df['discount_percentage'] / 100

    #Tratando a coluna 'rating'
    df['rating'] = df['rating'].replace('|',np.nan).replace(' ','')
    df['rating'] = df['rating'].astype(float)

    # Preenchendo os valores nulos da coluna 'rating' com a média dos ratings
    df['rating'] = df['rating'].fillna(df['rating'].mean())

    # Preenchendo os valores nulos da coluna 'rating_count' com 1 com base na quantidade na coluna 'user_name'
    df['rating_count'] = df['rating_count'].fillna(1)

    # Criando coluna 'full_discount' para calcular o valor total do desconto
    df['full_discount'] = df['actual_price'] - df['discounted_price']

    # Níveis de categorias e substituição da coluna 'category' por colunas de categorias
    df[['Category n0','Category n1','Category n2','Category n3','Category n4','Category n5','Category n6']] = df['category'].str.split('|',expand=True)
    df.drop('category', axis=1, inplace=True)

    # Organizando DataFrame
    df = (df[['product_id', 
        'product_name', 
        'Category n0', 
        'Category n1', 
        'Category n2',
        'Category n3', 
        'Category n4', 
        'Category n5', 
        'Category n6', 
        'actual_price',
        'discount_percentage',
        'discounted_price',
        'full_discount',
        'rating', 
        'rating_count', 
        'about_product',
        'user_id', 
        'user_name', 
        'review_id', 
        'review_title', 
        'review_content',]])

    # Preenchendo os valores nulos das colunas 'Category n[]' com '-'
    df[['Category n2', 'Category n3', 'Category n4', 'Category n5','Category n6']] = df[['Category n2', 'Category n3', 'Category n4', 'Category n5','Category n6']].fillna('-') 

    return df

# SALVANDO ARQUIVO FIAL
def salva_arq(df_transf):
    
    df_transf.to_parquet("data/amazon_tratada.parquet", index=False)
    return df_transf



if __name__ == "__main__":
    print("Iniciando o teste do módulo reader.py...")
    df = arq_entrada('data\\amazon.csv')
    df_transf = transformar_dados(df)
    salva_arq(df_transf)
    print("Teste do módulo reader.py concluído com sucesso!")