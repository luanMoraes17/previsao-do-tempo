from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from .weather_service import WeatherService
from .email_service import EmailService
from pydantic_settings import BaseSettings

app = FastAPI(title="API de Previsão do Tempo")

weather_service = WeatherService()
email_service = EmailService()

class WeatherRequest(BaseModel):
    cidade: str
    email: EmailStr

@app.post("/previsao-do-tempo")
async def get_weather_forecast(request: WeatherRequest):
    try:
        # Obtém a previsão do tempo
        weather_data = weather_service.get_weather(request.cidade)
        
        # Envia o email
        email_service.send_weather_email(request.email, weather_data)
        
        return {
            "mensagem": "Previsão do tempo enviada com sucesso para seu email!",
            "dados": weather_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 