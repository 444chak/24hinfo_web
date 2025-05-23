from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.categories import Category
from app.db.categories import get_all_categories, get_category_by_id

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
