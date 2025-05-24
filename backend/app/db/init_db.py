import sqlite3
import json
import os
from datetime import datetime

DATABASE_PATH = 'Data/database.sqlite'
DATA_PATH = 'Data/data.json'
CATEGORIES_PATH = 'Data/categories.json'

def init_db():
    """Initialise la base de données avec les données de data.json et categories.json"""
    # Vérifier si la base de données existe déjà
    if os.path.exists(DATABASE_PATH):
        print(f"La base de données existe déjà à {DATABASE_PATH}")
        return

    # Créer la connexion à la base de données
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Créer les tables nécessaires
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        icon TEXT,
        primary_color TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cultural_items (
        id INTEGER PRIMARY KEY,
        category_id INTEGER,
        name TEXT NOT NULL,
        description TEXT,
        address TEXT,
        arrondissement TEXT,
        images TEXT,
        gmaps TEXT,
        preview_video TEXT,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        cultural_item_id INTEGER,
        website TEXT,
        phone TEXT,
        email TEXT,
        FOREIGN KEY (cultural_item_id) REFERENCES cultural_items (id)
    )
    ''')

    # Lire les catégories depuis categories.json
    try:
        with open(CATEGORIES_PATH, 'r', encoding='utf-8') as f:
            categories = json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {CATEGORIES_PATH} n'existe pas")
        return
    except json.JSONDecodeError:
        print(f"Erreur lors de la lecture du fichier {CATEGORIES_PATH}")
        return

    # Insérer les catégories
    for category in categories:
        cursor.execute('''
        INSERT INTO categories (id, name, description, icon, primary_color)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            category['id'],
            category['name'],
            category['description'],
            category['icon'],
            category.get('primary', '#3B82F6')  # Utiliser la couleur par défaut si non spécifiée
        ))

    # Lire les données de data.json
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {DATA_PATH} n'existe pas")
        return
    except json.JSONDecodeError:
        print(f"Erreur lors de la lecture du fichier {DATA_PATH}")
        return

    # Insérer les données dans la base de données
    for item in data:
        # Insérer l'élément culturel
        cursor.execute('''
        INSERT INTO cultural_items (
            id, category_id, name, description, address, arrondissement,
            images, gmaps, preview_video, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['id'],
            item['category_id'],
            item['name'],
            item.get('description', ''),
            item.get('address', ''),
            item.get('arrondissement', ''),
            item.get('images', ''),
            item.get('gmaps', ''),
            item.get('preview_video'),
            item.get('created_at'),
            item.get('updated_at')
        ))

        # Insérer les contacts si présents
        if item.get('contact'):
            cursor.execute('''
            INSERT INTO contacts (cultural_item_id, website, phone, email)
            VALUES (?, ?, ?, ?)
            ''', (
                item['id'],
                item['contact'].get('website'),
                item['contact'].get('phone'),
                item['contact'].get('email')
            ))

    # Commit les changements et fermer la connexion
    conn.commit()
    conn.close()
    print(f"Base de données initialisée avec succès à {DATABASE_PATH}")

if __name__ == "__main__":
    init_db() 