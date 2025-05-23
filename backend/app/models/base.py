from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional
from enum import Enum
from datetime import datetime, time

class Arrondissement(str, Enum):
    """Enum pour les arrondissements de Lyon"""
    LYON_1 = "Lyon 1er"
    LYON_2 = "Lyon 2ème"
    LYON_3 = "Lyon 3ème"
    LYON_4 = "Lyon 4ème"
    LYON_5 = "Lyon 5ème"
    LYON_6 = "Lyon 6ème"
    LYON_7 = "Lyon 7ème"
    LYON_8 = "Lyon 8ème"
    LYON_9 = "Lyon 9ème"
    VILLEURBANNE = "Villeurbanne"

class Coordinates(BaseModel):
    """Coordonnées géographiques"""
    latitude: float
    longitude: float

class OpeningHours(BaseModel):
    """Horaires d'ouverture"""
    day: str  # Lundi, Mardi, etc.
    open_time: time
    close_time: time
    is_closed: bool = False

class Contact(BaseModel):
    """Informations de contact"""
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    website: Optional[HttpUrl] = None

class Image(BaseModel):
    """Image pour un élément culturel"""
    url: HttpUrl
    alt: str
    is_main: bool = False
