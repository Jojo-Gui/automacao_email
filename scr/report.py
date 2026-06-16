import pandas as pd

def ler_dados_tratados(df_limpo):

    # Carrega base de dados limpa
    df = pd.read_parquet(df_limpo)
    return df

def metricas(df_limpo):

    # Cálcula KPIs
    produtos_analisados = int(df_limpo['product_name'].nunique())
    media_preco_original = float(round(df_limpo['actual_price'].mean(), 2))
    media_descontos = float(round(df_limpo['discounted_price'].mean(), 2))

    produto_maior_desconto = str(df_limpo.loc[df_limpo['discount_percentage'].idxmax(), 'product_name'])
    preco_produto_maior_desconto = float(round((df_limpo['actual_price'].loc[df_limpo['discount_percentage'].idxmax()]), 2))
    maior_desconto_percentual = float(round(df_limpo['discount_percentage'].max() * 100, 2))

    produto_mais_caro = str(df_limpo.loc[df_limpo['actual_price'].idxmax(), 'product_name'])
    preco_produto_mais_caro = float(round(df_limpo['actual_price'].max(), 2))
    porcentagem_produto_mais_caro = float(round(df_limpo['discount_percentage'].loc[df_limpo['actual_price'].idxmax()] * 100, 2))


    # Armazena resultados em um dicionário
    resumo_dados = {
        "Produtos Analisados": produtos_analisados,
        "Média do Preço Original (R$)": media_preco_original,
        "Média dos Preços com Desconto (R$)": media_descontos,
        "Produto com Maior Desconto": produto_maior_desconto,
        "Preço do Produto com Maior Desconto (R$)": preco_produto_maior_desconto,
        "Maior Desconto Percentual (%)": maior_desconto_percentual,
        "Produto Mais Caro": produto_mais_caro,
        "Preço do Produto Mais Caro (R$)": preco_produto_mais_caro,
        "Percentual de Desconto do Produto Mais Caro (%)": porcentagem_produto_mais_caro,
    }

    return resumo_dados

if __name__ == "__main__":
    print("Iniciando o teste do módulo report.py...")

    # Executa o pipeline
    df_limpo = ler_dados_tratados('data\\amazon_tratada.parquet')
    resumo_dados = metricas(df_limpo)

    # Imprime resultados
    print("\n****** RESULTADOS FINANCEIROS ******")
    for chave, valor in resumo_dados.items():
        print(f"{chave}: {valor}")