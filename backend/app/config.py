import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class Settings:
    """Configuration globale de l'application"""
    APP_NAME: str = "API Culturelle de Lyon"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    FRONTEND_URL: str = "http://localhost:3000"
    
    # Extension possible pour une base de données réelle
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "lyon_culture"
    
    class Config:
        env_file = ".env"

settings = Settings()
