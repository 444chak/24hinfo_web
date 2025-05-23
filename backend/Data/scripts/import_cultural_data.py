import sqlite3
import csv
import os
from datetime import datetime

# Configuration
DB_PATH = r'c:\Users\adamp\Desktop\DevProject\24hINFO\Web\backend\Data\database.sqlite'
DATA_DIR = r'c:\Users\adamp\Desktop\DevProject\24hINFO\Web\backend\Data'

# Mappage des catégories avec leurs IDs
CATEGORY_MAPPING = {
    'Spectacle': 4,  # Nous allons créer de nouvelles catégories
    'Arts': 5,
    'Musique': 6
}

def create_new_categories(conn):
    """Crée les nouvelles catégories dans la base de données"""
    
    cursor = conn.cursor()
    
    # Vérifier les IDs existants
    cursor.execute("SELECT MAX(id) FROM categories")
    max_id = cursor.fetchone()[0] or 0
    
    # Mettre à jour le mapping si nécessaire
    start_id = max_id + 1
    for i, (name, _) in enumerate(CATEGORY_MAPPING.items()):
        CATEGORY_MAPPING[name] = start_id + i
    
    # Données des nouvelles catégories
    new_categories = [
        (CATEGORY_MAPPING['Spectacle'], 'Spectacle Vivant', 'Théâtre, danse, performances et spectacles en direct', 'drama'),
        (CATEGORY_MAPPING['Arts'], 'Arts Visuels', 'Peinture, sculpture, photographie et arts plastiques', 'palette'),
        (CATEGORY_MAPPING['Musique'], 'Musique', 'Concerts, festivals et événements musicaux', 'music')
    ]
    
    # Insérer les nouvelles catégories
    for cat_id, name, description, icon in new_categories:
        cursor.execute(
            "INSERT OR IGNORE INTO categories (id, name, description, icon) VALUES (?, ?, ?, ?)",
            (cat_id, name, description, icon)
        )
    
    conn.commit()
    print(f"Catégories créées: {new_categories}")

def get_arrondissement_from_postal_code(postal_code):
    """Convertit un code postal en arrondissement"""
    
    postal_code = str(postal_code).strip()
    
    # Mapping des codes postaux vers les arrondissements
    arrondissement_mapping = {
        '69001': 'Lyon 1er',
        '69002': 'Lyon 2ème',
        '69003': 'Lyon 3ème',
        '69004': 'Lyon 4ème',
        '69005': 'Lyon 5ème',
        '69006': 'Lyon 6ème',
        '69007': 'Lyon 7ème',
        '69008': 'Lyon 8ème',
        '69009': 'Lyon 9ème',
        '69100': 'Villeurbanne'
    }
    
    return arrondissement_mapping.get(postal_code, 'Autres')

def import_arts_data(conn):
    """Importe les données des arts visuels"""
    
    cursor = conn.cursor()
    
    # Lire les lieux emblématiques des arts
    arts_venues_path = os.path.join(DATA_DIR, 'Arts', 'lieux_emblematiques.csv')
    
    if not os.path.exists(arts_venues_path):
        print(f"Fichier non trouvé: {arts_venues_path}")
        return
    
    print(f"Importation des lieux d'arts visuels depuis {arts_venues_path}")
    
    with open(arts_venues_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for i, row in enumerate(reader, start=1):
            # Créer l'élément culturel principal
            cursor.execute("""
                INSERT INTO cultural_items 
                (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                CATEGORY_MAPPING['Arts'],
                row['Nom'].strip('"'),
                f"{row['Type_Musee']} - {row['Historique']}".strip('"'),
                row['Adresse'].strip('"'),
                get_arrondissement_from_postal_code(row['Code_Postal'].strip('"')),
                45.75 + i*0.001,  # Latitude approximative (à remplacer par des coordonnées réelles)
                4.85 + i*0.001,   # Longitude approximative
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))
            
            item_id = cursor.lastrowid
            
            # Ajouter les contacts
            cursor.execute("""
                INSERT INTO contacts (cultural_item_id, website)
                VALUES (?, ?)
            """, (
                item_id,
                f"https://www.musee-{row['Nom'].lower().replace(' ', '-').replace('(', '').replace(')', '')}.fr"
            ))
            
            # Ajouter une image par défaut
            cursor.execute("""
                INSERT INTO images (cultural_item_id, url, alt_text, is_primary)
                VALUES (?, ?, ?, ?)
            """, (
                item_id,
                f"https://example.com/images/{row['Nom'].lower().replace(' ', '_')}.jpg",
                f"Image de {row['Nom']}",
                1
            ))
    
    # Ajouter les expositions comme éléments culturels
    exhibitions_path = os.path.join(DATA_DIR, 'Arts', 'expositions.csv')
    
    if os.path.exists(exhibitions_path):
        print(f"Importation des expositions d'art depuis {exhibitions_path}")
        
        with open(exhibitions_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for i, row in enumerate(reader, start=1):
                museum_name = row['Musee'].strip('"')
                
                # Trouver l'adresse et l'arrondissement du musée
                cursor.execute("""
                    SELECT address, arrondissement FROM cultural_items 
                    WHERE name LIKE ? AND category_id = ?
                """, (f"%{museum_name}%", CATEGORY_MAPPING['Arts']))
                
                result = cursor.fetchone()
                address = result[0] if result else "Adresse inconnue"
                arrondissement = result[1] if result else "Lyon"
                
                # Créer l'élément culturel pour l'exposition
                cursor.execute("""
                    INSERT INTO cultural_items 
                    (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    CATEGORY_MAPPING['Arts'],
                    row['Nom_Exposition'].strip('"'),
                    row['Description'].strip('"') + f" (Au {museum_name})",
                    address,
                    arrondissement,
                    45.76 + i*0.001,  # Latitude approximative
                    4.83 + i*0.001,   # Longitude approximative
                    datetime.now().isoformat(),
                    datetime.now().isoformat()
                ))
    
    conn.commit()
    print("Importation des données d'arts terminée")

def import_music_data(conn):
    """Importe les données de musique"""
    
    cursor = conn.cursor()
    
    # Lire les lieux emblématiques de musique
    music_venues_path = os.path.join(DATA_DIR, 'Musique', 'lieux_emblematiques.csv')
    
    if not os.path.exists(music_venues_path):
        print(f"Fichier non trouvé: {music_venues_path}")
        return
    
    print(f"Importation des lieux de musique depuis {music_venues_path}")
    
    with open(music_venues_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for i, row in enumerate(reader, start=1):
            # Créer l'élément culturel principal
            cursor.execute("""
                INSERT INTO cultural_items 
                (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                CATEGORY_MAPPING['Musique'],
                row['Nom'].strip('"'),
                f"Lieu de musique | Genres: {row['Genre_principal']} | {row['Particularite']}".strip('"'),
                row['Adresse'].strip('"'),
                get_arrondissement_from_postal_code(row['Code_Postal'].strip('"')),
                45.74 + i*0.002,  # Latitude approximative
                4.84 + i*0.002,   # Longitude approximative
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))
            
            item_id = cursor.lastrowid
            
            # Ajouter les contacts
            cursor.execute("""
                INSERT INTO contacts (cultural_item_id, website)
                VALUES (?, ?)
            """, (
                item_id,
                f"https://www.{row['Nom'].lower().replace(' ', '-').replace('/', '-')}.fr"
            ))
            
            # Ajouter une image par défaut
            cursor.execute("""
                INSERT INTO images (cultural_item_id, url, alt_text, is_primary)
                VALUES (?, ?, ?, ?)
            """, (
                item_id,
                f"https://example.com/images/music_{row['Nom'].lower().replace(' ', '_').replace('/', '_')}.jpg",
                f"Image de {row['Nom']}",
                1
            ))
    
    # Ajouter les festivals comme éléments culturels
    festivals_path = os.path.join(DATA_DIR, 'Musique', 'festivals.csv')
    
    if os.path.exists(festivals_path):
        print(f"Importation des festivals de musique depuis {festivals_path}")
        
        with open(festivals_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for i, row in enumerate(reader, start=1):
                # Créer l'élément culturel pour le festival
                cursor.execute("""
                    INSERT INTO cultural_items 
                    (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    CATEGORY_MAPPING['Musique'],
                    row['Nom'].strip('"'),
                    f"Festival de musique | Période: {row['Periode']} | Styles: {row['Style']} | {row['Particularite']}".strip('"'),
                    "Divers lieux à Lyon",
                    "Lyon",
                    45.75 + i*0.002,  # Latitude approximative
                    4.85 + i*0.002,   # Longitude approximative
                    datetime.now().isoformat(),
                    datetime.now().isoformat()
                ))
                
                item_id = cursor.lastrowid
                
                # Ajouter les contacts
                cursor.execute("""
                    INSERT INTO contacts (cultural_item_id, website)
                    VALUES (?, ?)
                """, (
                    item_id,
                    f"https://www.{row['Nom'].lower().replace(' ', '-').replace('à', 'a')}.fr"
                ))
    
    # Ajouter les artistes comme éléments culturels
    artists_path = os.path.join(DATA_DIR, 'Musique', 'artistes.csv')
    
    if os.path.exists(artists_path):
        print(f"Importation des artistes de musique depuis {artists_path}")
        
        with open(artists_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for i, row in enumerate(reader, start=1):
                # Créer l'élément culturel pour l'artiste
                cursor.execute("""
                    INSERT INTO cultural_items 
                    (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    CATEGORY_MAPPING['Musique'],
                    row['Nom'].strip('"'),
                    f"Artiste musical lyonnais | Genre: {row['Genre']} | {row['Particularite']} | Type: {row['Type']}".strip('"'),
                    "Lyon",
                    "Lyon",
                    45.76 + i*0.001,  # Latitude approximative
                    4.86 + i*0.001,   # Longitude approximative
                    datetime.now().isoformat(),
                    datetime.now().isoformat()
                ))
    
    conn.commit()
    print("Importation des données de musique terminée")

def import_performance_data(conn):
    """Importe les données de spectacle vivant"""
    
    cursor = conn.cursor()
    
    # Lire les lieux emblématiques de spectacle
    performance_venues_path = os.path.join(DATA_DIR, 'Spectacle', 'lieux_emblematiques.csv')
    
    if not os.path.exists(performance_venues_path):
        print(f"Fichier non trouvé: {performance_venues_path}")
        return
    
    print(f"Importation des lieux de spectacle depuis {performance_venues_path}")
    
    with open(performance_venues_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for i, row in enumerate(reader, start=1):
            # Créer l'élément culturel principal
            cursor.execute("""
                INSERT INTO cultural_items 
                (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                CATEGORY_MAPPING['Spectacle'],
                row['Nom'].strip('"'),
                f"Lieu de spectacle | Type: {row['Type']} | Capacité: {row['Capacite']} | {row['Historique']}".strip('"'),
                row['Adresse'].strip('"') or "Adresse non précisée",
                get_arrondissement_from_postal_code(row['Code_Postal'].strip('"')),
                45.77 + i*0.001,  # Latitude approximative
                4.84 + i*0.001,   # Longitude approximative
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))
            
            item_id = cursor.lastrowid
            
            # Ajouter les contacts
            cursor.execute("""
                INSERT INTO contacts (cultural_item_id, website)
                VALUES (?, ?)
            """, (
                item_id,
                f"https://www.{row['Nom'].lower().replace(' ', '-').replace('é', 'e')}.fr"
            ))
            
            # Ajouter une image par défaut
            cursor.execute("""
                INSERT INTO images (cultural_item_id, url, alt_text, is_primary)
                VALUES (?, ?, ?, ?)
            """, (
                item_id,
                f"https://example.com/images/spectacle_{row['Nom'].lower().replace(' ', '_').replace('é', 'e')}.jpg",
                f"Image de {row['Nom']}",
                1
            ))
    
    # Ajouter les événements comme éléments culturels
    events_path = os.path.join(DATA_DIR, 'Spectacle', 'evenements.csv')
    
    if os.path.exists(events_path):
        print(f"Importation des événements de spectacle depuis {events_path}")
        
        with open(events_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for i, row in enumerate(reader, start=1):
                venue_name = row['Lieu'].strip('"')
                
                # Trouver l'adresse et l'arrondissement du lieu
                cursor.execute("""
                    SELECT address, arrondissement FROM cultural_items 
                    WHERE name LIKE ? AND category_id = ?
                """, (f"%{venue_name}%", CATEGORY_MAPPING['Spectacle']))
                
                result = cursor.fetchone()
                address = result[0] if result else "Adresse inconnue"
                arrondissement = result[1] if result else "Lyon"
                
                # Créer l'élément culturel pour l'événement
                cursor.execute("""
                    INSERT INTO cultural_items 
                    (category_id, name, description, address, arrondissement, latitude, longitude, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    CATEGORY_MAPPING['Spectacle'],
                    row['Nom_Evenement'].strip('"'),
                    f"{row['Type']} | {row['Description']} | Date: {row['Date']} | Lieu: {venue_name}".strip('"'),
                    address,
                    arrondissement,
                    45.75 + i*0.001,  # Latitude approximative
                    4.85 + i*0.001,   # Longitude approximative
                    datetime.now().isoformat(),
                    datetime.now().isoformat()
                ))
    
    conn.commit()
    print("Importation des données de spectacle terminée")

def main():
    print("Début de l'importation des données culturelles dans la base SQLite...")
    
    # Vérifier si la base de données existe
    if not os.path.exists(DB_PATH):
        print(f"La base de données n'existe pas au chemin: {DB_PATH}")
        return
    
    # Se connecter à la base de données
    conn = sqlite3.connect(DB_PATH)
    
    try:
        # Créer les nouvelles catégories
        create_new_categories(conn)
        
        # Importer les données pour chaque catégorie
        import_arts_data(conn)
        import_music_data(conn)
        import_performance_data(conn)
        
        print("Importation terminée avec succès!")
        
    except Exception as e:
        print(f"Erreur lors de l'importation des données: {e}")
        conn.rollback()
    
    finally:
        # Fermer la connexion
        conn.close()

if __name__ == "__main__":
    main()
