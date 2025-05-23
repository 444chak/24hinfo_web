from fastapi import APIRouter
from app.api.routes import categories, cultural_items

# Créer un routeur API principal
api_router = APIRouter(prefix="/api")

# Inclure tous les sous-routeurs
api_router.include_router(categories.router)
api_router.include_router(cultural_items.router)