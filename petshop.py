import json

def carregar_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo de dados não encontrado.")
        return {}

def exibir_menu(dados):
    print("SISTEMA DE BANHO PETSHOP")
    racas = list(dados.keys())
    
    for i, raca in enumerate(racas, 1):
        print(f"{i}. {raca}")
    print("0. Sair")
    
    return racas

def calcular_banho(peso):
    # Regra: R$ 2.50 por quilo
    return peso * 2.5