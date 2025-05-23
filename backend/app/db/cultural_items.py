import sqlite3
from app.db.categories import get_db_connection

class CulturalItem:
    def __init__(self, id, category_id, name, description, address, arrondissement, 
                 latitude, longitude, preview_video, created_at, updated_at):
        self.id = id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.address = address
        self.arrondissement = arrondissement
        self.latitude = latitude
        self.longitude = longitude
        self.preview_video = preview_video
        self.created_at = created_at
        self.updated_at = updated_at

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

def get_cultural_items_by_category(category_id: int):
    """Récupère tous les monuments culturels d'une catégorie spécifique"""
    conn = get_db_connection()
    cursor = conn.cursor()
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
