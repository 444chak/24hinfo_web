from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.categories import Category
from app.db.categories import get_all_categories, get_category_by_id, delete_category as db_delete_category

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[Category])
async def get_categories():
    """
    Récupère toutes les catégories culturelles
    """
    return get_all_categories()


@router.get("/{category_id}", response_model=Category)
async def get_category(category_id: int):
    """
    Récupère une catégorie spécifique par son ID
    """
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La catégorie avec l'ID {category_id} n'a pas été trouvée",
        )
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int):
    """
    Supprime une catégorie et tous ses éléments associés
    """
    success = db_delete_category(category_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la suppression de la catégorie {category_id}"
        )
