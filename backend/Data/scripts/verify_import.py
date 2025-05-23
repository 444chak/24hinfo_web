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

# Afficher les catégories
print("=== CATÉGORIES ===")
cursor.execute("SELECT id, name FROM categories ORDER BY id")
categories = cursor.fetchall()
for cat_id, name in categories:
    print(f"ID {cat_id}: {name}")

print("\n=== STATISTIQUES DES DONNÉES ===")
# Compter les éléments par catégorie
cursor.execute("""
    SELECT c.name, COUNT(ci.id) 
    FROM categories c
    LEFT JOIN cultural_items ci ON c.id = ci.category_id
    GROUP BY c.id
    ORDER BY c.id
""")
counts = cursor.fetchall()
for category, count in counts:
    print(f"{category}: {count} éléments")

print("\n=== EXEMPLES D'ÉLÉMENTS PAR CATÉGORIE ===")
# Afficher quelques exemples pour chaque catégorie nouvelle
for cat_id in [4, 5, 6]:  # IDs des nouvelles catégories
    cursor.execute("""
        SELECT name, description, address 
        FROM cultural_items 
        WHERE category_id = ?
        LIMIT 3
    """, (cat_id,))
    items = cursor.fetchall()
    
    cursor.execute("SELECT name FROM categories WHERE id = ?", (cat_id,))
    cat_name = cursor.fetchone()[0]
    
    print(f"\nCatégorie: {cat_name} (ID {cat_id})")
    for name, desc, addr in items:
        print(f"- {name}")
        print(f"  Adresse: {addr}")
        print(f"  Description: {desc[:100]}...")

# Fermer la connexion
conn.close()
