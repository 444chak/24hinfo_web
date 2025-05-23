from datetime import datetime, time
from app.models.cultural_items import Event
from app.models.base import Arrondissement, Coordinates, OpeningHours, Contact, Image
from app.db.event_data import events

# Utilisation des données importées depuis event_data.py
# events = []

def get_all_events():
    """Récupère tous les événements"""
    return events

def get_event_by_id(event_id: int):
    """Récupère un événement par son ID"""
    for event in events:
        if event.id == event_id:
            return event
    return None

def get_events_by_category(category_id: int):
    """Récupère les événements par catégorie"""
    return [event for event in events if event.category_id == category_id]

def get_events_by_arrondissement(arrondissement: Arrondissement):
    """Récupère les événements par arrondissement"""
    return [event for event in events if event.arrondissement == arrondissement]

def get_upcoming_events():
    """Récupère les événements à venir"""
    now = datetime.now()
    return [event for event in events if event.start_date > now]

def get_events_by_category(category_id: int):
    """Récupère les événements par catégorie"""
    return [event for event in events if event.category_id == category_id]

def get_events_by_arrondissement(arrondissement: Arrondissement):
    """Récupère les événements par arrondissement"""
    return [event for event in events if event.arrondissement == arrondissement]

def get_upcoming_events():
    """Récupère les événements à venir"""
    now = datetime.now()
    return [event for event in events if event.start_date > now]
