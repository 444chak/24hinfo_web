"""
Script de test pour vérifier l'intégration des données venues et events
"""
import sys
import os
from datetime import datetime

# Ajout du répertoire parent pour l'importation des modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import des modules nécessaires
from app.db.venues import get_all_venues, get_venue_by_id
from app.db.events import get_all_events, get_event_by_id
from app.db.categories import get_all_categories, get_category_by_id

# Test des venues
def test_venues():
    print("\n=== TEST DES LIEUX CULTURELS ===")
    venues = get_all_venues()
    print(f"Nombre total de lieux: {len(venues)}")
    
    # Affichage par catégorie
    for category_id in range(1, 7):  # Catégories 1 à 6
        category_venues = [v for v in venues if v.category_id == category_id]
        category = get_category_by_id(category_id)
        category_name = category.name if category else f"Catégorie {category_id}"
        print(f"Lieux de la catégorie '{category_name}': {len(category_venues)}")
    
    # Détails d'un lieu spécifique
    if venues:
        sample_venue = venues[0]
        print(f"\nDétail d'un lieu: {sample_venue.name}")
        print(f"Adresse: {sample_venue.address}")
        print(f"Arrondissement: {sample_venue.arrondissement}")
        print(f"Contact: {sample_venue.contact.telephone if sample_venue.contact.telephone else 'Non disponible'}")
        print(f"Site web: {sample_venue.contact.website if sample_venue.contact.website else 'Non disponible'}")
        
        if sample_venue.opening_hours:
            print("Horaires:")
            for hour in sample_venue.opening_hours:
                if hour.is_closed:
                    print(f"  {hour.day}: Fermé")
                else:
                    print(f"  {hour.day}: {hour.open_time} - {hour.close_time}")

# Test des événements
def test_events():
    print("\n=== TEST DES ÉVÉNEMENTS ===")
    events = get_all_events()
    print(f"Nombre total d'événements: {len(events)}")
    
    # Affichage par catégorie
    for category_id in range(1, 7):  # Catégories 1 à 6
        category_events = [e for e in events if e.category_id == category_id]
        category = get_category_by_id(category_id)
        category_name = category.name if category else f"Catégorie {category_id}"
        print(f"Événements de la catégorie '{category_name}': {len(category_events)}")
    
    # Événements à venir
    now = datetime.now()
    upcoming_events = [e for e in events if e.end_date >= now]
    print(f"Événements à venir: {len(upcoming_events)}")
    
    # Détails d'un événement spécifique
    if events:
        sample_event = events[0]
        print(f"\nDétail d'un événement: {sample_event.name}")
        print(f"Dates: {sample_event.start_date.strftime('%d/%m/%Y')} au {sample_event.end_date.strftime('%d/%m/%Y')}")
        print(f"Prix: {'Gratuit' if sample_event.is_free else f'{sample_event.price}€'}")
        print(f"Lieu: {sample_event.address}")
        
        if sample_event.booking_url:
            print(f"Réservation: {sample_event.booking_url}")

if __name__ == "__main__":
    print("Test d'intégration des données culturelles")
    
    # Test des catégories
    categories = get_all_categories()
    print(f"Nombre de catégories: {len(categories)}")
    for cat in categories:
        print(f"- {cat.id}: {cat.name}")
    
    # Test des venues
    test_venues()
    
    # Test des événements
    test_events()
    
    print("\nTest terminé.")
