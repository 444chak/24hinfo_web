from fastapi import FastAPI
from app.db.init_db import init_db

app = FastAPI()

# Initialiser la base de données au démarrage
init_db()

# Importer et inclure les routes
from app.api.routes import cultural_items, categories

app.include_router(cultural_items.router, prefix="/api")
app.include_router(categories.router, prefix="/api")
