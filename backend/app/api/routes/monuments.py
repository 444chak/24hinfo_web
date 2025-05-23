from fastapi import APIRouter, HTTPException, status
from typing import List, Optional

from app.models.cultural_items import Monument
from app.models.base import Arrondissement
from app.db.monuments import (
    get_all_monuments,
    get_monument_by_id,
    get_monuments_by_arrondissement,
    get_unesco_monuments,
    get_monuments_by_period
)

router = APIRouter(prefix="/monuments", tags=["Monuments"])

@router.get("/", response_model=List[Monument])
async def get_monuments(
    arrondissement: Optional[Arrondissement] = None,
    is_unesco: Optional[bool] = None,
    historical_period: Optional[str] = None
):
    """
    Récupère les monuments avec filtrage optionnel
    """
    if arrondissement is not None:
        return get_monuments_by_arrondissement(arrondissement)
    
    if is_unesco is not None and is_unesco:
        return get_unesco_monuments()
    
    if historical_period is not None:
        return get_monuments_by_period(historical_period)
    
    return get_all_monuments()

@router.get("/{monument_id}", response_model=Monument)
async def get_monument(monument_id: int):
    """
    Récupère un monument spécifique par son ID
    """
    monument = get_monument_by_id(monument_id)
    if not monument:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Le monument avec l'ID {monument_id} n'a pas été trouvé"
        )
    return monument

@router.get("/unesco/", response_model=List[Monument])
async def get_unesco_monuments_route():
    """
    Récupère tous les monuments classés UNESCO
    """
    return get_unesco_monuments()

@router.get("/arrondissement/{arrondissement}", response_model=List[Monument])
async def get_monuments_for_arrondissement(arrondissement: Arrondissement):
    """
    Récupère tous les monuments pour un arrondissement spécifique
    """
    return get_monuments_by_arrondissement(arrondissement)

@router.get("/period/{period}", response_model=List[Monument])
async def get_monuments_for_period(period: str):
    """
    Récupère tous les monuments pour une période historique spécifique
    """
    return get_monuments_by_period(period)
