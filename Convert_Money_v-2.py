import requests
import json

# Lista de moedas
MOEDAS = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CAD",
    "AUD",
    "CHF",
    "CNY",
    "BRL",
]

# Exibe a lista de moedas
def exibe_moedas():
    print("Moedas disponíveis:")
    for moeda in MOEDAS:
        print(moeda)

# Solicita o valor a ser convertido
def solicita_valor():
    while True:
        try:
            valor = float(input("Insira o valor a ser convertido: "))
            break
        except ValueError:
            print("Valor inválido. Insira apenas números.")
    return valor

"""def solicita_valor():
    valor = float(input("Insira o valor a ser convertido: "))
    return valor"""

# Solicita a moeda de entrada
def solicita_moeda_entrada():
    moeda_entrada = input("Insira a moeda de entrada: ").upper()
    while moeda_entrada not in MOEDAS:
        print("Moeda inválida. Tente novamente.")
        moeda_entrada = input("Insira a moeda de entrada: ").upper()
    return moeda_entrada

# Solicita a moeda de origem
def solicita_moeda_origem():
    moeda_origem = input("Insira a moeda de origem: ").upper()
    while moeda_origem not in MOEDAS:
        print("Moeda inválida. Tente novamente.")
        moeda_origem = input("Insira a moeda de origem: ").upper()
    return moeda_origem

# Realiza a conversão
def converte_moedas(valor, moeda_entrada, moeda_origem):
    # Obtém a taxa de conversão
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(moeda_entrada)
    response = requests.get(url)
    data = json.loads(response.text)
    taxa_conversao = data["rates"][moeda_origem]

    # Realiza a conversão
    valor_convertido = valor * taxa_conversao

    # Formata o valor convertido
    valor_convertido = "{:.2f}".format(valor_convertido)

    print(f"A taxa de conversão de {moeda_entrada} para {moeda_origem} é {taxa_conversao}")

    return valor_convertido

# Programa principal
if __name__ == "__main__":
    # Exibe a lista de moedas
    exibe_moedas()

    # Solicita o valor a ser convertido
    valor = solicita_valor()

    # Solicita a moeda de entrada
    moeda_entrada = solicita_moeda_entrada()

    # Solicita a moeda de origem
    moeda_origem = solicita_moeda_origem()

    # Realiza a conversão
    valor_convertido = converte_moedas(valor, moeda_entrada, moeda_origem)

    # Exibe o resultado
    print(f"O Valor de {valor} {moeda_entrada} equivale a {valor_convertido} em {moeda_origem}")
