from app.models.cultural_items import Venue
from app.models.base import Arrondissement
from app.db.venue_data import venues

# Utilisation des données importées depuis venue_data.py
# venues = []

def get_all_venues():
    """Récupère tous les lieux culturels"""
    return venues

def get_venue_by_id(venue_id: int):
    """Récupère un lieu culturel par son ID"""
    for venue in venues:
        if venue.id == venue_id:
            return venue
    return None

def get_venues_by_category(category_id: int):
    """Récupère les lieux culturels par catégorie"""
    return [venue for venue in venues if venue.category_id == category_id]

def get_venues_by_arrondissement(arrondissement: Arrondissement):
    """Récupère les lieux culturels par arrondissement"""
    return [venue for venue in venues if venue.arrondissement == arrondissement]

def get_venues_by_category(category_id: int):
    """Récupère les lieux culturels par catégorie"""
    return [venue for venue in venues if venue.category_id == category_id]

def get_venues_by_arrondissement(arrondissement: Arrondissement):
    """Récupère les lieux culturels par arrondissement"""
    return [venue for venue in venues if venue.arrondissement == arrondissement]
