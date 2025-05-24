import sqlite3
from app.db.categories import get_db_connection
from app.models.base import Coordinates, Contact, Arrondissement
from datetime import datetime

def normalize_arrondissement(arrondissement: str) -> str:
    """Convertit une valeur d'arrondissement en une valeur valide de l'enum Arrondissement"""
    if not arrondissement:
        return "Lyon 1er"  # Valeur par défaut
    
    arrondissement = arrondissement.strip()
    
    # Si c'est déjà une valeur valide, la retourner
    try:
        Arrondissement(arrondissement)
        return arrondissement
    except ValueError:
        pass
    
    # Mapping des valeurs invalides vers des valeurs valides
    mapping = {
        "Lyon": "Lyon 1er",
        "Lyon 1": "Lyon 1er",
        "Lyon 2": "Lyon 2ème",
        "Lyon 3": "Lyon 3ème",
        "Lyon 4": "Lyon 4ème",
        "Lyon 5": "Lyon 5ème",
        "Lyon 6": "Lyon 6ème",
        "Lyon 7": "Lyon 7ème",
        "Lyon 8": "Lyon 8ème",
        "Lyon 9": "Lyon 9ème",
        "69001": "Lyon 1er",
        "69002": "Lyon 2ème",
        "69003": "Lyon 3ème",
        "69004": "Lyon 4ème",
        "69005": "Lyon 5ème",
        "69006": "Lyon 6ème",
        "69007": "Lyon 7ème",
        "69008": "Lyon 8ème",
        "69009": "Lyon 9ème"
    }
    
    return mapping.get(arrondissement, "Lyon 1er")  # Retourne Lyon 1er si aucune correspondance n'est trouvée

class CulturalItem:
    def __init__(self, id, category_id, name, description, address, arrondissement, 
                 latitude=None, longitude=None, preview_video=None, created_at=None, updated_at=None):
        self.id = id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.address = address
        self.arrondissement = Arrondissement(normalize_arrondissement(arrondissement))
        self.coordinates = Coordinates(latitude=latitude, longitude=longitude) if latitude and longitude else None
        self.contact = None  # À implémenter si nécessaire
        self.preview_video = preview_video
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.opening_hours = []
        self.images = []

def get_all_cultural_items():
    """Récupère tous les monuments culturels"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, category_id, name, description, address, arrondissement,
                    latitude, longitude, preview_video, created_at, updated_at 
                    FROM cultural_items""")
    items_data = cursor.fetchall()
    conn.close()
    
    cultural_items = []
    for item_data in items_data:
        cultural_item = CulturalItem(
            id=item_data['id'],
            category_id=item_data['category_id'],
            name=item_data['name'],
            description=item_data['description'],
            address=item_data['address'],
            arrondissement=item_data['arrondissement'],
            latitude=item_data['latitude'],
            longitude=item_data['longitude'],
            preview_video=item_data['preview_video'],
            created_at=item_data['created_at'],
            updated_at=item_data['updated_at']
        )
        cultural_items.append(cultural_item)
    
    return cultural_items

def get_cultural_item_by_id(item_id: int):
    """Récupère un monument culturel par son ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, category_id, name, description, address, arrondissement,
                    latitude, longitude, preview_video, created_at, updated_at 
                    FROM cultural_items WHERE id = ?""", (item_id,))
    item_data = cursor.fetchone()
    conn.close()
    
    if not item_data:
        return None
    
    return CulturalItem(
        id=item_data['id'],
        category_id=item_data['category_id'],
        name=item_data['name'],
        description=item_data['description'],
        address=item_data['address'],
        arrondissement=item_data['arrondissement'],
        latitude=item_data['latitude'],
        longitude=item_data['longitude'],
        preview_video=item_data['preview_video'],
        created_at=item_data['created_at'],
        updated_at=item_data['updated_at']
    )

def get_cultural_items_by_category(category_id: str):
    """Récupère tous les monuments culturels d'une catégorie spécifique"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Vérifier d'abord si la catégorie existe
    cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
    if not cursor.fetchone():
        conn.close()
        return None
    
    cursor.execute("""SELECT id, category_id, name, description, address, arrondissement,
                    latitude, longitude, preview_video, created_at, updated_at 
                    FROM cultural_items WHERE category_id = ?""", (category_id,))
    items_data = cursor.fetchall()
    conn.close()
    
    cultural_items = []
    for item_data in items_data:
        cultural_item = CulturalItem(
            id=item_data['id'],
            category_id=item_data['category_id'],
            name=item_data['name'],
            description=item_data['description'],
            address=item_data['address'],
            arrondissement=item_data['arrondissement'],
            latitude=item_data['latitude'],
            longitude=item_data['longitude'],
            preview_video=item_data['preview_video'],
            created_at=item_data['created_at'],
            updated_at=item_data['updated_at']
        )
        cultural_items.append(cultural_item)
    
    return cultural_items
