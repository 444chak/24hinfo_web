from app.db.cultural_items import (
    get_all_cultural_items,
    get_cultural_item_by_id,
    get_cultural_items_by_category,
)
from fastapi import APIRouter, Query, HTTPException, status

router = APIRouter(prefix="/cultural-items", tags=["Cultural Items"])


@router.get("/", response_model=list[dict])
async def get_all_items():
    """Route pour récupérer tous les monuments culturels"""
    items = get_all_cultural_items()
    result = [item.__dict__ for item in items]
    return result


@router.get("/{item_id}", response_model=dict)
async def get_item(item_id: str):
    """Route pour récupérer un monument culturel par son ID"""
    item = get_cultural_item_by_id(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'item culturel avec l'ID {item_id} n'a pas été trouvé"
        )
    return item.__dict__


@router.get("/category/{category_id}", response_model=list[dict])
async def get_items_by_category(category_id: str):
    """Route pour récupérer tous les monuments culturels d'une catégorie spécifique"""
    items = get_cultural_items_by_category(category_id)
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aucun item culturel trouvé pour la catégorie {category_id}"
        )
    result = [item.__dict__ for item in items]
    return result
