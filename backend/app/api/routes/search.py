from fastapi import APIRouter, Query
from typing import Dict, List, Any, Optional
from app.db.search import search_all_items, get_map_items, get_items_by_arrondissement
from app.models.base import Arrondissement

router = APIRouter(tags=["Search"])

@router.get("/search", response_model=Dict[str, List])
async def search_items(q: str = Query(..., min_length=3)):
    """
    Recherche dans tous les éléments culturels
    """
    return search_all_items(q)

@router.get("/map", response_model=List[Dict[str, Any]])
async def get_map_points(
    category_id: Optional[int] = None,
    arrondissement: Optional[Arrondissement] = None,
    item_type: Optional[str] = None
):
    """
    Récupère tous les points d'intérêt pour la carte
    """
    items = get_map_items()
    
    # Filtrage optionnel
    if category_id is not None:
        items = [item for item in items if item["category_id"] == category_id]
    
    if arrondissement is not None:
        items = [item for item in items if item["arrondissement"] == arrondissement]
    
    if item_type is not None:
        items = [item for item in items if item["type"] == item_type]
    
    return items

@router.get("/arrondissements", response_model=Dict[str, Dict[str, List]])
async def get_arrondissements():
    """
    Récupère tous les éléments culturels regroupés par arrondissement
    """
    return get_items_by_arrondissement()
