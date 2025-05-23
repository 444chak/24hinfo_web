from app.models.categories import Category

# Données statiques pour les catégories
categories = [
    Category(
        id=1,
        name="Spectacle Vivant",
        description="Théâtre, danse, performances et spectacles en direct",
        icon="drama",
        primary="#3B82F6"
    ),
    Category(
        id=2,
        name="Arts Visuels",
        description="Peinture, sculpture, photographie et arts plastiques",
        icon="palette",
        primary="#EC4899"
    ),
    Category(
        id=3,
        name="Musique",
        description="Concerts, festivals et événements musicaux",
        icon="music",
        primary="#8B5CF6"
    ),
    Category(
        id=4,
        name="Littérature",
        description="Livres, poésie, lectures et événements littéraires",
        icon="book-open",
        primary="#10B981"
    ),
    Category(
        id=5,
        name="Cinéma",
        description="Films, projections et événements cinématographiques des Frères Lumière",
        icon="film",
        primary="#F59E0B"
    ),
    Category(
        id=6,
        name="Architecture",
        description="Patrimoine architectural, visites et découvertes urbaines",
        icon="building-2",
        primary="#EF4444"
    )
]

def get_all_categories():
    """Récupère toutes les catégories"""
    return categories

def get_category_by_id(category_id: int):
    """Récupère une catégorie par son ID"""
    for category in categories:
        if category.id == category_id:
            return category
    return None
