from fastapi import APIRouter, HTTPException, status
from typing import List, Optional

from app.models.cultural_items import Venue
from app.models.base import Arrondissement
from app.db.venues import (
    get_all_venues,
    get_venue_by_id,
    get_venues_by_category,
    get_venues_by_arrondissement
)

router = APIRouter(prefix="/venues", tags=["Venues"])

@router.get("/", response_model=List[Venue])
async def get_venues(
    category_id: Optional[int] = None,
    arrondissement: Optional[Arrondissement] = None
):
    """
    Récupère les lieux culturels avec filtrage optionnel
    
    Exemples:
    - /api/venues?category_id=2 : lieux de la catégorie 2
    - /api/venues?arrondissement=Lyon%205ème : lieux dans Lyon 5ème
    - /api/venues?category_id=2&arrondissement=Lyon%205ème : combinaison de filtres
    """
    if category_id is not None:
        return get_venues_by_category(category_id)
    
    if arrondissement is not None:
        return get_venues_by_arrondissement(arrondissement)
    
    return get_all_venues()

@router.get("/{venue_id}", response_model=Venue)
async def get_venue(venue_id: int):
    """
    Récupère un lieu culturel spécifique par son ID
    """
    venue = get_venue_by_id(venue_id)
    if not venue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Le lieu culturel avec l'ID {venue_id} n'a pas été trouvé"
        )
    return venue
