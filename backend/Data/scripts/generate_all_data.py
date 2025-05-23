import csv
from datetime import datetime

def create_categories():
    """Crée le fichier CSV des catégories"""
    
    print("Création des catégories...")
    
    categories_data = [
        {
            'id': 1,
            'name': 'Littérature',
            'description': 'Bibliothèques, librairies, centres de documentation et lieux dédiés à la lecture et à l\'écriture à Lyon.',
            'icon': 'book-open',
            'primary': '#3B82F6'
        },
        {
            'id': 2,
            'name': 'Cinéma (Frères Lumière)',
            'description': 'Musées, cinémas, lieux d\'exposition et événements liés au cinéma et à l\'héritage des frères Lumière.',
            'icon': 'film',
            'primary': '#EF4444'
        },
        {
            'id': 3,
            'name': 'Architecture',
            'description': 'Monuments historiques, édifices remarquables et patrimoine architectural de Lyon.',
            'icon': 'building',
            'primary': '#10B981'
        }
    ]
    
    output_file = 'C:/Users/Sky/Downloads/backend/Data/categories.csv'
    
    fieldnames = ['id', 'name', 'description', 'icon', 'primary']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(categories_data)
    
    print(f"Catégories sauvegardées dans {output_file}")
    print(f"Nombre de catégories créées : {len(categories_data)}")

def run_all_scripts():
    """Lance tous les scripts de génération de données"""
    
    print("=== GÉNÉRATION COMPLÈTE DES DATASETS CULTURELS DE LYON ===")
    print()
    
    # Catégories
    create_categories()
    print()
    
    # Import et lancement des autres scripts
    import subprocess
    import sys
    
    scripts = [
        'fetch_bibliotheques_lyon.py',
        'fetch_musees_lyon.py',
        'fetch_monuments_lyon.py'
    ]
    
    for script in scripts:
        print(f"Lancement de {script}...")
        try:
            result = subprocess.run([sys.executable, script], 
                                  capture_output=True, text=True, 
                                  cwd='C:/Users/Sky/Downloads/backend/Data/scripts')
            if result.returncode == 0:
                print(f"[OK] {script} terminé avec succès")
                print(result.stdout)
            else:
                print(f"[ERREUR] Erreur dans {script}:")
                print(result.stderr)
        except Exception as e:
            print(f"[ERREUR] Erreur lors du lancement de {script}: {e}")
        print()
    
    print("=== RÉSUMÉ DES DATASETS GÉNÉRÉS ===")
    
    # Vérification des fichiers générés
    import os
    
    files_to_check = [
        ('categories.csv', 'Catégories'),
        ('bibliotheques_lyon.csv', 'Lieux littéraires'),
        ('musees_lyon.csv', 'Cinémas et musées'),
        ('monuments_lyon.csv', 'Architecture et monuments')
    ]
    
    for filename, description in files_to_check:
        filepath = f'C:/Users/Sky/Downloads/backend/Data/{filename}'
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                row_count = sum(1 for row in reader) - 1  # -1 pour l'en-tête
            print(f"✓ {description}: {row_count} entrées dans {filename}")
        else:
            print(f"✗ {description}: fichier {filename} non trouvé")
    
    print()
    print("Tous les datasets sont prêts à être utilisés dans votre application FastAPI !")

if __name__ == "__main__":
    run_all_scripts()
