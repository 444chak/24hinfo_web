from app.models.cultural_items import Monument
from app.models.base import Arrondissement

# Données d'exemple pour les monuments (vide par défaut, mais structure prête)
monuments = []

def get_all_monuments():
    """Récupère tous les monuments"""
    return monuments

def get_monument_by_id(monument_id: int):
    """Récupère un monument par son ID"""
    for monument in monuments:
        if monument.id == monument_id:
            return monument
    return None

def get_monuments_by_arrondissement(arrondissement: Arrondissement):
    """Récupère les monuments par arrondissement"""
    return [monument for monument in monuments if monument.arrondissement == arrondissement]

def get_unesco_monuments():
    """Récupère les monuments classés UNESCO"""
    return [monument for monument in monuments if monument.is_unesco]

def get_monuments_by_period(period: str):
    """Récupère les monuments par période historique"""
    return [monument for monument in monuments if monument.historical_period == period]
