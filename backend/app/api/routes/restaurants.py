from fastapi import APIRouter, HTTPException, status
from typing import List, Optional

from app.models.cultural_items import Restaurant
from app.models.base import Arrondissement
from app.db.restaurants import (
    get_all_restaurants,
    get_restaurant_by_id,
    get_restaurants_by_cuisine,
    get_restaurants_by_arrondissement,
    get_restaurants_by_price_range
)

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.get("/", response_model=List[Restaurant])
async def get_restaurants(
    cuisine_type: Optional[str] = None,
    arrondissement: Optional[Arrondissement] = None,
    price_range: Optional[str] = None
):
    """
    Récupère les restaurants culturels avec filtrage optionnel
    
    Exemples:
    - /api/restaurants?cuisine_type=Cuisine%20lyonnaise : restaurants de cuisine lyonnaise
    - /api/restaurants?arrondissement=Lyon%202ème : restaurants dans Lyon 2ème
    - /api/restaurants?price_range=€€ : restaurants dans la fourchette de prix €€
    - /api/restaurants?cuisine_type=Cuisine%20lyonnaise&price_range=€€ : combinaison de filtres
    """
    if cuisine_type is not None:
        return get_restaurants_by_cuisine(cuisine_type)
    
    if arrondissement is not None:
        return get_restaurants_by_arrondissement(arrondissement)
    
    if price_range is not None:
        return get_restaurants_by_price_range(price_range)
    
    return get_all_restaurants()

@router.get("/{restaurant_id}", response_model=Restaurant)
async def get_restaurant(restaurant_id: int):
    """
    Récupère un restaurant spécifique par son ID
    """
    restaurant = get_restaurant_by_id(restaurant_id)
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Le restaurant avec l'ID {restaurant_id} n'a pas été trouvé"
        )
    return restaurant
