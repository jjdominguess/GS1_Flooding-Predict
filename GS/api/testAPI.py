import requests

url = 'http://127.0.0.1:5000/predict'

# Exemplo de dados climáticos
dados = {
    "Chuva_mm": 40,
    "Umidade_%": 85,
    "Temperatura_C": 22,
    "Nivel_rio_m": 2.2
}

resposta = requests.post(url, json=dados)
print(resposta.json())
