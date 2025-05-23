from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from datetime import datetime

from app.models.cultural_items import Event
from app.models.base import Arrondissement
from app.db.events import (
    get_all_events, 
    get_event_by_id, 
    get_events_by_category,
    get_events_by_arrondissement,
    get_upcoming_events
)

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=List[Event])
async def get_events(
    category_id: Optional[int] = None,
    arrondissement: Optional[Arrondissement] = None,
    upcoming_only: bool = False
):
    """
    Récupère les événements avec filtrage optionnel
    
    Exemples:
    - /api/events?category_id=3 : événements de la catégorie 3
    - /api/events?arrondissement=Lyon%201er : événements dans Lyon 1er
    - /api/events?upcoming_only=true : événements à venir
    - /api/events?category_id=3&arrondissement=Lyon%201er : combinaison de filtres
    """
    if category_id is not None:
        return get_events_by_category(category_id)
    
    if arrondissement is not None:
        return get_events_by_arrondissement(arrondissement)
    
    if upcoming_only:
        return get_upcoming_events()
    
    return get_all_events()

@router.get("/{event_id}", response_model=Event)
async def get_event(event_id: int):
    """
    Récupère un événement spécifique par son ID
    """
    event = get_event_by_id(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'événement avec l'ID {event_id} n'a pas été trouvé"
        )
    return event
