<h1 align="center">ETL e Automação de Envio de E-Mail</h1>
 
---
 
## 📌 Índice
 
- [Descrição do Projeto](#page_facing_up-descrição-do-projeto)
- [Funcionalidades do Projeto](#hammer-funcionalidades-do-projeto)
- [Tecnologias Utilizadas](#fireworks-técnicas-e-tecnologias-utilizadas)
- [Acesso ao Projeto](#open_file_folder-acesso-ao-projeto)
- [Abrir e Rodar o Projeto](#hammer_and_wrench-abrir-e-rodar-o-projeto)
- [Próximos Passos (Evolução)](#crystal_ball-próximos-passos)
- [Autores](#autores)
---
 
<p align="center">
  <img alt="Status Concluído" src="https://img.shields.io/badge/status-concluido-green">
</p>
---
 
## :page_facing_up: Descrição do Projeto
 
Projeto de simulação de ETL e automação de envio de e-mails pelo Gmail de indicadores de descontos de produtos da Amazon.
 
---
 
## :hammer: Funcionalidades do Projeto
 
- `Carregar e tratar arquivo .csv (reader.py)`: Coleta base de dados bruta em `.csv` e realiza todo o tratamento.
- `Transformações em .parquet (reader.py)`: Salva a base já tratada em um arquivo de alta performance `.parquet`.
- `Cálculos e Métricas (report.py)`: Realiza os cálculos estatísticos para as métricas financeiras solicitadas.
- `Envio de e-mail (mailer.py)`: Realiza a montagem descritiva do corpo HTML e o disparo de rede.
---
 
## :fireworks: Técnicas e Tecnologias Utilizadas
 
- `Python 3`: Linguagem base para desenvolvimento.
- `Pandas`: Framework para manipulação de dados, agregações e cálculos estatísticos.
- `Apache Parquet`: Formato de dados colunar altamente otimizado para Big Data e Analytics.
- `python-dotenv`: Biblioteca de segurança e proteção de credenciais de ambiente.
- `smtplib & email.message`: Bibliotecas nativas para estruturação de HTML e comunicação com protocolo de e-mail.
- `Agendador de Tarefas do Windows (Task Scheduler)`: Orquestrador local para engatilhar e executar o script em horários pré-determinados.
- `Pipeline E2E (End-to-End)/ETL`: Arquitetura de extração, transformação e carregamento cobrindo todas as etapas de forma autônoma.
- `Comunicação Segura (SSL/TLS)`: Envio de dados sensíveis encapsulados por criptografia de ponta a ponta através da porta 465.
---
 
## :open_file_folder: Acesso ao Projeto
 
Você pode acessar o projeto clonando o repositório para sua máquina. Abra seu terminal e execute o comando abaixo:
 
```bash
git clone https://github.com/Jojo-Gui/automacao_email.git
```
 
---
 
## :hammer_and_wrench: Abrir e Rodar o Projeto
 
Após clonar o repositório, siga as etapas abaixo para configurar o ambiente e executar a automação de forma segura.
 
**1. Abra a pasta do projeto no VS Code**
 
Navegue até a pasta clonada e abra-a no seu editor de código:
 
```bash
cd automacao_email
code .
```
 
**2. Crie e ative o ambiente virtual**
 
Crie um ambiente isolado para evitar conflitos com o sistema operacional:
 
```bash
python -m venv .venv
```
 
Ative o ambiente:
 
```bash
source .venv/Scripts/activate
```
 
**3. Instale as dependências**
 
Com o ambiente ativado `(.venv)`, instale todas as bibliotecas necessárias:
 
```bash
pip install -r requirements.txt
```
 
**4. Configure as credenciais de segurança**
 
O projeto utiliza um cofre de variáveis para proteger senhas sensíveis.
 
- Localize o arquivo `.env.example` na raiz do projeto.
- Renomeie-o para `.env`.
- Abra o arquivo e preencha com o seu e-mail e a Senha de Aplicativo gerada:
```text
EMAIL_REMETENTE=seu_email@gmail.com
SENHA_APP=sua_senha_de_16_digitos_aqui
```
 
> **NOTA:** Em caso de dúvidas de como gerar a `SENHA_APP`, acesse o link: https://support.google.com/accounts/answer/185833?hl=pt-BR
 
**5. Altere os e-mails de destinatários**
 
É necessário abrir o `mailer.py` e o `main.py` para realizar a alteração dos e-mails de destinatário:
 
```python
lista_de_emails = [
    'email1@gmail.com',
    'email2@gmail.com',
    'email3@hotmail.com'
    # Pode realizar a adição de quantos destinatários necessários
]
```
 
**6. Execute o Orquestrador**
 
Com tudo configurado, execute o arquivo principal para dar a largada no pipeline E2E. O robô fará a limpeza da base de dados e o disparo automático do e-mail:
 
```bash
python main.py
```
 
---
 
## :crystal_ball: Próximos Passos
 
- Migrar a orquestração local para a nuvem utilizando **GitHub Actions** ou **Power Automate**.
- Substituir a extração em arquivo físico (CSV) por uma conexão nativa direta a um banco de dados relacional.
---
 
## Autores
 
[<img loading="lazy" src="https://avatars.githubusercontent.com/u/102173992?s=400&u=8aa86a0133ba5f556dc56371a8b3514ce08dfdf5&v=4" width=115><br><sub>João Guidetti</sub>](https://github.com/Jojo-Gui)