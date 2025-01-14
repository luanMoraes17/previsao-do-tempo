import requests

url = "http://localhost:8000/previsao-do-tempo"
data = {
    "cidade": "São Paulo",
    "email": "luanlima1107@gmail.com"
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print("Resposta do servidor:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")