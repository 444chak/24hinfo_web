import csv
from datetime import datetime
import random

def generate_coordinates(arrondissement: str) -> tuple:
    coords_map = {
        "Lyon 1er": (45.7640, 4.8357, 0.01),
        "Lyon 2ème": (45.7540, 4.8320, 0.01),
        "Lyon 3ème": (45.7580, 4.8460, 0.01),
        "Lyon 4ème": (45.7750, 4.8300, 0.01),
        "Lyon 5ème": (45.7600, 4.8200, 0.01),
        "Lyon 6ème": (45.7700, 4.8500, 0.01),
        "Lyon 7ème": (45.7400, 4.8400, 0.01),
        "Lyon 8ème": (45.7300, 4.8600, 0.01),
        "Lyon 9ème": (45.7800, 4.8000, 0.01)
    }
    
    base_lat, base_lon, variation = coords_map.get(arrondissement, (45.7640, 4.8357, 0.01))
    lat = base_lat + random.uniform(-variation, variation)
    lon = base_lon + random.uniform(-variation, variation)
    return round(lat, 6), round(lon, 6)

def fetch_extended_cinema_musees():
    """Génère un dataset étendu de cinémas, musées et lieux culturels"""
    
    print("Création d'un dataset étendu des lieux cinéma/musées de Lyon...")
    
    # Vrais lieux + fictifs réalistes
    lieux_cinema_musees = [
        # Musées réels
        ("Musée des Beaux-Arts de Lyon", "20 place des Terreaux", "Lyon 1er", "Venue", 1801),
        ("Musée Lumière", "25 rue du Premier-Film", "Lyon 8ème", "Venue", 1982),
        ("Musée d'art contemporain", "81 quai Charles de Gaulle", "Lyon 6ème", "Venue", 1984),
        ("Musée Gadagne", "1 place du Petit Collège", "Lyon 5ème", "Venue", 2009),
        ("Centre d'Histoire de la Résistance", "14 avenue Berthelot", "Lyon 7ème", "Venue", 1992),
        ("Musée de l'Imprimerie", "13 rue de la Poulaillerie", "Lyon 2ème", "Venue", 1964),
        ("Musée Henri Malartre", "645 rue du Musée", "Lyon 6ème", "Venue", 1960),
        
        # Cinémas réels et Institut Lumière
        ("Institut Lumière - Hangar du Premier Film", "25 rue du Premier-Film", "Lyon 8ème", "Venue", 1982),
        ("Cinéma Lumière Terreaux", "40 rue du Président Herriot", "Lyon 1er", "Venue", 2020),
        ("Cinéma Lumière Bellecour", "12 rue de la Barre", "Lyon 2ème", "Venue", 2020),
        ("Cinéma Lumière Fourmi", "68 rue Pierre Corneille", "Lyon 3ème", "Venue", 2020),
        ("UGC Ciné Cité Internationale", "60 quai Charles de Gaulle", "Lyon 6ème", "Venue", 1998),
        ("Cinéma Comoedia", "13 avenue Berthelot", "Lyon 7ème", "Venue", 1924),
        ("Le Zola", "89 rue Sébastien Gryphe", "Lyon 7ème", "Venue", 1988),
        
        # Lieux d'exposition et galeries
        ("Galerie Le Réverbère", "", "Lyon 1er", "Venue", 1995),
        ("Espace d'art contemporain Confluence", "", "Lyon 2ème", "Venue", 2010),
        ("Centre culturel Charlie Chaplin", "", "Lyon 8ème", "Venue", 1985),
        ("Maison de la Danse", "", "Lyon 8ème", "Venue", 1980),
        ("Théâtre National Populaire", "", "Lyon 9ème", "Venue", 1972),
        ("Le Sucre", "", "Lyon 7ème", "Venue", 2011)
    ]
    
    # Événements liés au cinéma et aux Frères Lumière
    evenements_cinema = [
        ("Festival Lumière", "Various locations", "Lyon center", "Event"),
        ("Nuits de Fourvière - Cinéma", "Théâtres Romains", "Lyon 5ème", "Event"),
        ("Rencontres du cinéma italien", "Institut Lumière", "Lyon 8ème", "Event"),
        ("Écrans Mixtes", "Various cinemas", "Lyon center", "Event"),
        ("Festival Regards Croisés", "MAC Lyon", "Lyon 6ème", "Event"),
        ("Quinzaine du cinéma français", "Cinémas Lumière", "Lyon center", "Event"),
        ("Soirées Première", "UGC Ciné Cité", "Lyon 6ème", "Event"),
        ("Ciné-concert Lumière", "Hangar Premier Film", "Lyon 8ème", "Event"),
        ("Projection en plein air", "Parc de la Tête d'Or", "Lyon 6ème", "Event"),
        ("Marathon cinéma Kubrick", "Comoedia", "Lyon 7ème", "Event")
    ]
    
    venues_data = []
    id_counter = 1
    
    # Traitement venues
    for nom, adresse, arrondissement, type_lieu, annee in lieux_cinema_musees:
        lat, lon = generate_coordinates(arrondissement)
        
        if not adresse:
            adresse = f"{random.randint(1, 100)} rue {random.choice(['Victor Hugo', 'de la République', 'Garibaldi', 'des Arts'])}"
        
        descriptions_musee = [
            "Musée présentant des collections permanentes et expositions temporaires d'art et culture.",
            "Espace culturel dédié à la préservation et diffusion du patrimoine artistique lyonnais.",
            "Institution muséale offrant parcours thématiques et médiation culturelle innovante.",
            "Centre d'art proposant découverte d'œuvres et rencontres avec les artistes.",
            "Lieu d'exposition mettant en valeur l'art contemporain et les créations émergentes."
        ]
        
        descriptions_cinema = [
            "Salle de cinéma art et essai programmant films d'auteur et cinéma indépendant.",
            "Cinéma proposant programmation éclectique entre blockbusters et films de patrimoine.",
            "Espace cinématographique dédié à la découverte et à l'innovation filmique.",
            "Lieu de projection offrant expérience cinéma premium avec technologies de pointe.",
            "Cinéma engagé dans la promotion du 7ème art sous toutes ses formes."
        ]
        
        if "Musée" in nom or "Centre" in nom or "Galerie" in nom or "Espace" in nom:
            description = random.choice(descriptions_musee)
            amenities_pool = ['Boutique', 'Café', 'Bibliothèque', 'Auditorium', 'Ateliers pédagogiques', 'Visites guidées', 'Audioguides', 'Jardin']
        else:
            description = random.choice(descriptions_cinema)
            amenities_pool = ['Bar', 'Confiserie', 'Parking', 'Réservation en ligne', 'Tarifs réduits', 'Séances VF/VOST', 'Écran géant', 'Son Dolby']
        
        venue_data = {
            'id': id_counter,
            'category_id': 2,  # Cinéma
            'name': nom,
            'description': description,
            'address': f"{adresse}, {arrondissement}",
            'arrondissement': arrondissement,
            'latitude': lat,
            'longitude': lon,
            'contact_telephone': f"04 {random.randint(72, 78)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}",
            'contact_email': None,
            'contact_website': f"http://www.{nom.lower().replace(' ', '-').replace('è', 'e').replace('é', 'e').replace('ç', 'c')}-lyon.fr",
            'founded_year': annee,
            'accessibility': random.choice(['Accès PMR', 'Accès PMR; Ascenseur', 'Accès PMR; Places réservées']),
            'amenities': '; '.join(random.sample(amenities_pool, random.randint(3, 5))),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        venues_data.append(venue_data)
        id_counter += 1
    
    # Traitement événements
    for nom, lieu, arrondissement, type_lieu in evenements_cinema:
        lat, lon = generate_coordinates(arrondissement)
        
        event_data = {
            'id': id_counter,
            'category_id': 2,  # Cinéma 
            'name': nom,
            'description': f"Événement cinématographique majeur de Lyon, programmation d'exception et rencontres avec professionnels du cinéma.",
            'address': f"{lieu}, {arrondissement}",
            'arrondissement': arrondissement,
            'latitude': lat,
            'longitude': lon,
            'contact_telephone': f"04 {random.randint(72, 78)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}",
            'contact_email': None,
            'contact_website': f"http://www.{nom.lower().replace(' ', '-').replace('è', 'e').replace('é', 'e')}.com",
            'founded_year': random.randint(1990, 2020),
            'accessibility': 'Accès PMR',
            'amenities': 'Événement; Rencontres; Projections',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        venues_data.append(event_data)
        id_counter += 1
    
    # Ajout de lieux supplémentaires fictifs mais réalistes
    autres_lieux = [
        "Médiathèque du Bachut", "Centre culturel Œcuménique", "Espace Pandora",
        "Galerie Slika", "Le Périscope", "Atelier des Beaux-Arts", "Studio 24",
        "Café-Théâtre du Bord de Scène", "Salle Molière", "L'Épicerie Moderne",
        "Cinéma Les Alizés", "Projection Room", "Ciné-Club Universitaire",
        "Maison du Livre et de l'Image", "Centre Culturel Communal",
        "Espace Artistes Émergents", "Galerie Underground", "Le Cube d'Art",
        "Cinémathèque Amateur", "Studio Indépendant"
    ]
    
    for nom in autres_lieux:
        arrondissement = random.choice(["Lyon 1er", "Lyon 2ème", "Lyon 3ème", "Lyon 4ème", "Lyon 5ème", "Lyon 6ème", "Lyon 7ème", "Lyon 8ème", "Lyon 9ème"])
        lat, lon = generate_coordinates(arrondissement)
        
        venue_data = {
            'id': id_counter,
            'category_id': 2,
            'name': nom,
            'description': f"Lieu culturel proposant programmation artistique variée et soutien à la création contemporaine.",
            'address': f"{random.randint(1, 150)} rue {random.choice(['de la Paix', 'Victor Hugo', 'Garibaldi', 'des Martyrs'])}, {arrondissement}",
            'arrondissement': arrondissement,
            'latitude': lat,
            'longitude': lon,
            'contact_telephone': f"04 {random.randint(72, 78)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}",
            'contact_email': None,
            'contact_website': f"http://www.{nom.lower().replace(' ', '-').replace('è', 'e')}.fr",
            'founded_year': random.randint(1980, 2020),
            'accessibility': 'Accès PMR',
            'amenities': '; '.join(random.sample(['Bar', 'Exposition', 'Atelier', 'Scène ouverte', 'Résidence artiste'], 3)),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        venues_data.append(venue_data)
        id_counter += 1
    
    # Sauvegarde
    output_file = 'C:/Users/Sky/Downloads/backend/Data/musees_lyon.csv'
    
    fieldnames = [
        'id', 'category_id', 'name', 'description', 'address', 'arrondissement',
        'latitude', 'longitude', 'contact_telephone', 'contact_email', 'contact_website',
        'founded_year', 'accessibility', 'amenities', 'created_at', 'updated_at'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(venues_data)
    
    print(f"Données sauvegardées dans {output_file}")
    print(f"Nombre total de lieux cinéma/musées créés : {len(venues_data)}")

if __name__ == "__main__":
    fetch_extended_cinema_musees()
