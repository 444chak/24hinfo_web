from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.cultural_items import BaseCulturalItem
from app.db.cultural_items import get_all_cultural_items, get_cultural_item_by_id, get_cultural_items_by_category

router = APIRouter(prefix="/cultural-items", tags=["Cultural Items"])

@router.get("/", response_model=List[BaseCulturalItem])
async def get_items(category_id: int = None):
    """
    Récupère tous les items culturels, optionnellement filtrés par catégorie
    """
    if category_id:
        items = get_cultural_items_by_category(category_id)
    else:
        items = get_all_cultural_items()
    
    if not items:
        return []
    
    return items

@router.get("/{item_id}", response_model=BaseCulturalItem)
async def get_item(item_id: int):
    """
    Récupère un item culturel spécifique par son ID
    """
    item = get_cultural_item_by_id(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'item culturel avec l'ID {item_id} n'a pas été trouvé"
        )
    return item
