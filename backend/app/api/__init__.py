from fastapi import APIRouter
from app.api.routes import categories, events, venues, monuments, restaurants, search

# Créer un routeur API principal
api_router = APIRouter(prefix="/api")

# Inclure tous les sous-routeurs
api_router.include_router(categories.router)
api_router.include_router(events.router)
api_router.include_router(venues.router)
api_router.include_router(monuments.router)
api_router.include_router(restaurants.router)
api_router.include_router(search.router)