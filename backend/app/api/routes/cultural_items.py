from app.db.cultural_items import (
    get_all_cultural_items,
    get_cultural_item_by_id,
    get_cultural_items_by_category,
)
from fastapi import APIRouter, Query

router = APIRouter(prefix="/cultural-items", tags=["Cultural Items"])


@router.get("/", response_model=list[dict])
async def get_all_items():
    """Route pour récupérer tous les monuments culturels"""
    items = get_all_cultural_items()
    result = [item.__dict__ for item in items]
    return result


@router.get("/", response_model=dict)
async def get_item(item_id: str = Query(..., description="ID of the cultural item")):
    """Route pour récupérer un monument culturel par son ID"""
    item = get_cultural_item_by_id(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'item culturel avec l'ID {item_id} n'a pas été trouvé"
        )
    return item
  

@router.get("/", response_model=list[dict])
async def get_items_by_category(
    category_id: str = Query(..., description="ID of the category"),
):
    """Route pour récupérer tous les monuments culturels d'une catégorie spécifique"""
    items = get_cultural_items_by_category(category_id)
    result = [item.__dict__ for item in items]
    return result
