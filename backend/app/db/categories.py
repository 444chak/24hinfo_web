from app.models.categories import Category

# Données statiques pour les catégories
categories = []

def get_all_categories():
    """Récupère toutes les catégories"""
    return categories

def get_category_by_id(category_id: int):
    """Récupère une catégorie par son ID"""
    for category in categories:
        if category.id == category_id:
            return category
    return None
