from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime
from app.models.base import Arrondissement, Coordinates, OpeningHours, Contact, Image

class BaseCulturalItem(BaseModel):
    """Modèle de base pour tous les éléments culturels"""
    id: int
    category_id: int
    name: str
    description: str
    address: str
    arrondissement: Arrondissement
    coordinates: Optional[Coordinates] = None
    opening_hours: List[OpeningHours] = []
    contact: Optional[Contact] = None
    images: List[Image] = []
    preview_video: Optional[HttpUrl] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()