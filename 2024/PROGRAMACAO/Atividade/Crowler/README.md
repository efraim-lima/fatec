# Projeto de Programação SQLite 📊

## Home Broker + Crowler de Dados 🏦🔍

Este projeto é uma atividade proposta pelo professor Adilson de programação da Fatec São Caetano do Sul.

### Algumas ações que este home broker pode fazer:

#### Instruções de Uso:

1. Instale Python3 e pip, caso não tenha:
    ```bash
    sudo apt-get install python3 python3-pip
    ```

2. Navegue até a pasta raiz do repositório:
    ```bash
    cd caminho/para/o/repositório
    ```

3. Ative o ambiente virtual:
    ```bash
    source .venv/bin/activate
    ```

4. Instale as dependências listadas no arquivo requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o módulo principal:
    ```bash
    python main.py
    ```

6. Aguarde a solicitação (puxando todos os dados da bolsa).

7. Siga os passos solicitados na tela.

#### `broker`

Apresenta dados atuais do mercado.

#### Lógica para Comprar:

- Faça um request pela API da bolsa.
- Salve como uma nova tabela no banco de dados.
- Verifique o saldo.

#### Lógica para Vender:

- Verifique se existe este ativo na bolsa (beta).
- Verifique se existe quantidade na carteira do cliente:
    - Se existir, venda (beta).
    - Se não existir, alerte que será feita uma venda à seco (perigosa) (beta).
- Verifique o saldo (beta).
- Compare com o preço do ativo (beta).
- Venda.