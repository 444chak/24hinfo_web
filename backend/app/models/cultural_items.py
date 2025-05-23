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
    coordinates: Coordinates
    opening_hours: List[OpeningHours] = []
    contact: Contact
    images: List[Image] = []
    preview_video: Optional[HttpUrl] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class Event(BaseCulturalItem):
    """Événement culturel (concerts, expositions, etc.)"""
    start_date: datetime
    end_date: datetime
    price: Optional[float] = None
    is_free: bool = False
    booking_url: Optional[HttpUrl] = None

class Venue(BaseCulturalItem):
    """Lieu culturel permanent (musées, théâtres, bibliothèques, etc.)"""
    founded_year: Optional[int] = None
    accessibility: List[str] = []  # Fauteuil roulant, aides auditives, etc.
    amenities: List[str] = []  # Café, boutique de souvenirs, etc.

class Monument(BaseCulturalItem):
    """Monument historique ou site architectural"""
    built_year: Optional[int] = None
    architectural_style: Optional[str] = None
    historical_period: Optional[str] = None
    is_unesco: bool = False

class Restaurant(BaseCulturalItem):
    """Restaurants et lieux de restauration culturels"""
    cuisine_type: str
    price_range: str  # €, €€, €€€
    specialties: List[str] = []
    reservation_url: Optional[HttpUrl] = None
