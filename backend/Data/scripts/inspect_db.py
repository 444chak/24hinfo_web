import sqlite3
import os

# Chemin vers la base de données
db_path = r'c:\Users\adamp\Desktop\DevProject\24hINFO\Web\backend\Data\database.sqlite'

# Vérifier si le fichier existe
if not os.path.exists(db_path):
    print(f"La base de données n'existe pas au chemin: {db_path}")
    exit(1)

# Se connecter à la base de données
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Lister toutes les tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables dans la base de données:")
for table in tables:
    print(f"- {table[0]}")
    # Afficher les colonnes de chaque table
    cursor.execute(f"PRAGMA table_info({table[0]})")
    columns = cursor.fetchall()
    for column in columns:
        print(f"  - {column[1]} ({column[2]})")

# Fermer la connexion
conn.close()
