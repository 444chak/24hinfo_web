import sqlite3
from app.models.categories import Category

DATABASE_PATH = 'Data/database.sqlite'

def get_db_connection():
    """Établit une connexion à la base de données SQLite"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_categories():
    """Récupère toutes les catégories depuis la base de données"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, description, icon FROM categories')
    categories_data = cursor.fetchall()
    conn.close()

    categories = []
    for category_data in categories_data:
        category = Category(
            id=category_data['id'],
            name=category_data['name'],
            description=category_data['description'],
            icon=category_data['icon'],
            primary="#3B82F6"  # Couleur bleue par défaut
        )
        categories.append(category)
    
    return categories

def get_category_by_id(category_id: int):
    """Récupère une catégorie par son ID depuis la base de données"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, description, icon FROM categories WHERE id = ?', (category_id,))
    category_data = cursor.fetchone()
    conn.close()
    
    if not category_data:
        return None
    
    return Category(
        id=category_data['id'],
        name=category_data['name'],
        description=category_data['description'],
        icon=category_data['icon'],
        primary="#3B82F6"  # Couleur bleue par défaut
    )

def delete_category(category_id: int):
    """Supprime une catégorie et tous ses éléments associés"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Supprimer d'abord tous les éléments culturels associés à cette catégorie
        cursor.execute("DELETE FROM cultural_items WHERE category_id = ?", (category_id,))
        
        # Ensuite supprimer la catégorie
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Erreur lors de la suppression de la catégorie: {e}")
        return False
    finally:
        conn.close()
