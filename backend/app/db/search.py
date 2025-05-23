from typing import Dict, List, Any
from app.db.events import get_all_events
from app.db.venues import get_all_venues
from app.db.monuments import get_all_monuments
from app.db.restaurants import get_all_restaurants
from app.models.base import Arrondissement

def search_all_items(query: str):
    """
    Recherche dans tous les éléments culturels
    """
    query = query.lower()
    results = {
        "events": [],
        "venues": [],
        "monuments": [],
        "restaurants": []
    }
    
    # Recherche dans les événements
    for event in get_all_events():
        if query in event.name.lower() or query in event.description.lower():
            results["events"].append(event)
    
    # Recherche dans les lieux
    for venue in get_all_venues():
        if query in venue.name.lower() or query in venue.description.lower():
            results["venues"].append(venue)
    
    # Recherche dans les monuments
    for monument in get_all_monuments():
        if query in monument.name.lower() or query in monument.description.lower():
            results["monuments"].append(monument)
    
    # Recherche dans les restaurants
    for restaurant in get_all_restaurants():
        if query in restaurant.name.lower() or query in restaurant.description.lower():
            results["restaurants"].append(restaurant)
    
    return results

def get_map_items():
    """
    Récupère tous les points d'intérêt pour la carte
    """
    map_items = []
    
    # Ajouter les événements
    for item in get_all_events():
        map_items.append({
            "type": "event",
            "id": item.id,
            "name": item.name,
            "category_id": item.category_id,
            "coordinates": {"latitude": item.coordinates.latitude, "longitude": item.coordinates.longitude},
            "arrondissement": item.arrondissement
        })
    
    # Ajouter les lieux
    for item in get_all_venues():
        map_items.append({
            "type": "venue",
            "id": item.id,
            "name": item.name,
            "category_id": item.category_id,
            "coordinates": {"latitude": item.coordinates.latitude, "longitude": item.coordinates.longitude},
            "arrondissement": item.arrondissement
        })
    
    # Ajouter les monuments
    for item in get_all_monuments():
        map_items.append({
            "type": "monument",
            "id": item.id,
            "name": item.name,
            "category_id": item.category_id,
            "coordinates": {"latitude": item.coordinates.latitude, "longitude": item.coordinates.longitude},
            "arrondissement": item.arrondissement
        })
    
    # Ajouter les restaurants
    for item in get_all_restaurants():
        map_items.append({
            "type": "restaurant",
            "id": item.id,
            "name": item.name,
            "category_id": item.category_id,
            "coordinates": {"latitude": item.coordinates.latitude, "longitude": item.coordinates.longitude},
            "arrondissement": item.arrondissement
        })
    
    return map_items

def get_items_by_arrondissement():
    """
    Récupère tous les éléments culturels regroupés par arrondissement
    """
    result = {}
    
    # Initialiser les arrondissements
    for arrondissement in Arrondissement:
        result[arrondissement] = {
            "events": [],
            "venues": [],
            "monuments": [],
            "restaurants": []
        }
    
    # Classer les événements par arrondissement
    for event in get_all_events():
        result[event.arrondissement]["events"].append(event)
    
    # Classer les lieux par arrondissement
    for venue in get_all_venues():
        result[venue.arrondissement]["venues"].append(venue)
    
    # Classer les monuments par arrondissement
    for monument in get_all_monuments():
        result[monument.arrondissement]["monuments"].append(monument)
    
    # Classer les restaurants par arrondissement
    for restaurant in get_all_restaurants():
        result[restaurant.arrondissement]["restaurants"].append(restaurant)
    
    return result
