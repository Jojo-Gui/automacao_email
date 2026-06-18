import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

def gerar_html(mock):

    #Criando corpo do email
    corpo_email = f"""
    <h2>Resumo dos Produtos Analisados</h2>
    <p><strong>Produtos Analisados:</strong> {mock.get('Produtos Analisados')}</p>
    <p><strong>Média do Preço Original (R$):</strong> {mock.get('Média do Preço Original (R$)')}</p>
    <p><strong>Média dos Preços com Desconto (R$):</strong> {mock.get('Média dos Preços com Desconto (R$)')}</p>
    <p><strong>Produto com Maior Desconto:</strong> {mock.get('Produto com Maior Desconto')}</p>
    <p><strong>Preço do Produto com Maior Desconto (R$):</strong> {mock.get('Preço do Produto com Maior Desconto (R$)')}</p>
    <p><strong>Maior Desconto Percentual (%):</strong> {mock.get('Maior Desconto Percentual (%)')}</p>
    <p><strong>Produto Mais Caro:</strong> {mock.get('Produto Mais Caro')}</p>
    <p><strong>Preço do Produto Mais Caro (R$):</strong> {mock.get('Preço do Produto Mais Caro (R$)')}</p>
    <p><strong>Percentual de Desconto do Produto Mais Caro (%):</strong> {mock.get('Percentual de Desconto do Produto Mais Caro (%)')}</p>
    """

    return corpo_email

def enviar_email(corpo_email, destinatario):

    # Carrega dados do .env
    load_dotenv()

    # Guarda as credenciais/variáveis
    email_remetente = os.getenv("EMAIL_REMETENTE")
    senha_remetente = os.getenv("SENHA_APP")

    # Configurações do email
    msg = EmailMessage()
    msg['Subject'] = 'Resumo dos Produtos Analisados'
    msg['From'] = email_remetente
    msg['To'] = destinatario

    # Injetando o HTML
    msg.set_content(corpo_email, subtype='html')

    # Abre a conexão segura com o servidor do Google na porta 465
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_remetente, senha_remetente) # Faz o login
        smtp.send_message(msg) # enviar email
        print("E-mail enviado com sucesso!")


if __name__ == "__main__":
    print("Iniciando o teste do módulo mailer.py...")

    # {Chave} originais com {valor} ficticios
    mock = {
        "Produtos Analisados": 1234,
        "Média do Preço Original (R$)": 1000,
        "Média dos Preços com Desconto (R$)": 56954,
        "Produto com Maior Desconto": "CABO USB-C TIPO SEI LÁ O QUE",
        "Preço do Produto com Maior Desconto (R$)": 4999,
        "Maior Desconto Percentual (%)": 95.0,
        "Produto Mais Caro": "TELEVISÃO 4K",
        "Preço do Produto Mais Caro (R$)": 59876533,
        "Percentual de Desconto do Produto Mais Caro (%)": 90.0,
    }

    # Gera HTML
    html = gerar_html(mock)
    
    lista_de_emails = [
        'sdayane577@gmail.com',
        'leo.mlr06@gmail.com',
        'jpguidetti2@hotmail.com'        
    ]

    # tranforma a lista em texto
    lista_de_emails = ', '.join(lista_de_emails)

    # Envia email
    enviar_email(html, lista_de_emails)