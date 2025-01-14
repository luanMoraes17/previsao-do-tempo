import smtplib
from email.mime.text import MIMEText
from .config import settings

class EmailService:
    def __init__(self):
        self.sender = settings.EMAIL_SENDER
        self.password = settings.EMAIL_PASSWORD
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_weather_email(self, to_email: str, weather_data: dict):
        message = f"""
        Previsão do tempo para {weather_data['cidade']}:
        
        Temperatura: {weather_data['temperatura']}°C
        Sensação térmica: {weather_data['sensacao_termica']}°C
        Umidade: {weather_data['umidade']}%
        Condição: {weather_data['descricao']}
        """

        msg = MIMEText(message)
        msg['Subject'] = f'Previsão do tempo para {weather_data["cidade"]}'
        msg['From'] = self.sender
        msg['To'] = to_email

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender, self.password)
            server.send_message(msg)