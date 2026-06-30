import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"


def cotacao_dolar():
    response = requests.get(url) 
    if response.status_code == 200: 
        data = response.json() 
       
        dolar = data["USDBRL"]["bid"]  
        return dolar
    else:
        return print("Erro ao buscar cotação")