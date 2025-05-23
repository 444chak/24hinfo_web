# API Culturelle de Lyon

Cette API recense des informations culturelles essentielles sur la ville de Lyon, organisées en 6 catégories principales : Spectacle Vivant, Arts Visuels, Musique, Littérature, Cinéma et Architecture.

## Structure des données

L'API organise les données culturelles en 4 types principaux :

- **Événements** : Événements temporaires comme les festivals, concerts, expositions temporaires
- **Lieux culturels** : Lieux permanents comme les musées, théâtres, salles de concert
- **Monuments** : Sites historiques et architecturaux
- **Restaurants culturels** : Restaurants et cafés à thème culturel

## Points d'accès (Endpoints)

### Catégories

- `GET /api/categories` - Liste de toutes les catégories culturelles
- `GET /api/categories/{category_id}` - Détails d'une catégorie spécifique

### Événements

- `GET /api/events` - Liste de tous les événements
- `GET /api/events?category_id={id}` - Événements filtrés par catégorie
- `GET /api/events?arrondissement={arrondissement}` - Événements filtrés par arrondissement
- `GET /api/events?upcoming_only=true` - Événements à venir uniquement
- `GET /api/events/{event_id}` - Détails d'un événement spécifique
- `GET /api/events/category/{category_id}` - Événements par catégorie
- `GET /api/events/arrondissement/{arrondissement}` - Événements par arrondissement
- `GET /api/events/upcoming` - Événements à venir

### Lieux culturels

- `GET /api/venues` - Liste de tous les lieux culturels
- `GET /api/venues?category_id={id}` - Lieux filtrés par catégorie
- `GET /api/venues?arrondissement={arrondissement}` - Lieux filtrés par arrondissement
- `GET /api/venues/{venue_id}` - Détails d'un lieu spécifique
- `GET /api/venues/category/{category_id}` - Lieux par catégorie
- `GET /api/venues/arrondissement/{arrondissement}` - Lieux par arrondissement

### Monuments

- `GET /api/monuments` - Liste de tous les monuments
- `GET /api/monuments?arrondissement={arrondissement}` - Monuments filtrés par arrondissement
- `GET /api/monuments?is_unesco=true` - Monuments classés UNESCO
- `GET /api/monuments?historical_period={period}` - Monuments filtrés par période historique
- `GET /api/monuments/{monument_id}` - Détails d'un monument spécifique
- `GET /api/monuments/unesco` - Monuments classés UNESCO
- `GET /api/monuments/arrondissement/{arrondissement}` - Monuments par arrondissement
- `GET /api/monuments/period/{period}` - Monuments par période historique

### Restaurants

- `GET /api/restaurants` - Liste de tous les restaurants culturels
- `GET /api/restaurants?cuisine_type={type}` - Restaurants filtrés par type de cuisine
- `GET /api/restaurants?arrondissement={arrondissement}` - Restaurants filtrés par arrondissement
- `GET /api/restaurants?price_range={range}` - Restaurants filtrés par fourchette de prix
- `GET /api/restaurants/{restaurant_id}` - Détails d'un restaurant spécifique
- `GET /api/restaurants/cuisine/{cuisine_type}` - Restaurants par type de cuisine
- `GET /api/restaurants/arrondissement/{arrondissement}` - Restaurants par arrondissement
- `GET /api/restaurants/price/{price_range}` - Restaurants par fourchette de prix

### Recherche

- `GET /api/search?q={query}` - Recherche globale dans tous les éléments culturels
- `GET /api/map` - Points pour la carte interactive
- `GET /api/map?category_id={id}` - Points filtrés par catégorie
- `GET /api/map?arrondissement={arrondissement}` - Points filtrés par arrondissement
- `GET /api/map?item_type={type}` - Points filtrés par type (event, venue, monument, restaurant)
- `GET /api/arrondissements` - Éléments culturels groupés par arrondissement

## Installation et démarrage

1. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```

2. Lancer l'application :
   ```
   python main.py
   ```

L'API sera disponible à l'adresse http://localhost:8000
La documentation interactive sera disponible à l'adresse http://localhost:8000/docs
