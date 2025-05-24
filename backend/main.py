from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api import api_router

# Créer l'application FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    description="API pour les informations culturelles essentielles de Lyon",
)

# Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure le routeur API principal
app.include_router(api_router)


@app.get("/")
async def root():
    """
    Racine de l'API
    """
    return {
        "message": "Bienvenue sur l'API Culturelle de Lyon!",
        "version": settings.API_VERSION,
        "documentation": "/docs",
    }


# Pour démarrer l'application avec uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
