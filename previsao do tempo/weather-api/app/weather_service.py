import requests
from .config import settings

class WeatherService:
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, cidade: str):
        params = {
            "q": f"{cidade},BR",
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br"
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        weather_data = response.json()
        return {
            "cidade": cidade,
            "temperatura": weather_data["main"]["temp"],
            "sensacao_termica": weather_data["main"]["feels_like"],
            "umidade": weather_data["main"]["humidity"],
            "descricao": weather_data["weather"][0]["description"]
        }