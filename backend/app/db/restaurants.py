from app.models.cultural_items import Restaurant
from app.models.base import Arrondissement

# Données d'exemple pour les restaurants (vide par défaut, mais structure prête)
restaurants = []

def get_all_restaurants():
    """Récupère tous les restaurants culturels"""
    return restaurants

def get_restaurant_by_id(restaurant_id: int):
    """Récupère un restaurant par son ID"""
    for restaurant in restaurants:
        if restaurant.id == restaurant_id:
            return restaurant
    return None

def get_restaurants_by_cuisine(cuisine_type: str):
    """Récupère les restaurants par type de cuisine"""
    return [restaurant for restaurant in restaurants if restaurant.cuisine_type.lower() == cuisine_type.lower()]

def get_restaurants_by_arrondissement(arrondissement: Arrondissement):
    """Récupère les restaurants par arrondissement"""
    return [restaurant for restaurant in restaurants if restaurant.arrondissement == arrondissement]

def get_restaurants_by_price_range(price_range: str):
    """Récupère les restaurants par fourchette de prix"""
    return [restaurant for restaurant in restaurants if restaurant.price_range == price_range]
