"""
Module contenant les données pour les événements culturels (events) à Lyon.
Généré à partir des fichiers CSV existants.
"""
from datetime import datetime, time
from app.models.cultural_items import Event
from app.models.base import Arrondissement, Coordinates, OpeningHours, Contact, Image

# Événements des arts visuels (catégorie 2)
art_events = [
    Event(
        id=401,
        category_id=2,  # Arts Visuels
        name="Échos du passé, promesses du futur",
        description="Exploration de la nature sublimée par le numérique à travers les œuvres de quinze artistes.",
        address="81 Quai Charles de Gaulle", # MAC Lyon
        arrondissement=Arrondissement.LYON_6,
        coordinates=Coordinates(latitude=45.7848, longitude=4.8553),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(11, 0), close_time=time(19, 0)),
            OpeningHours(day="Dimanche", open_time=time(11, 0), close_time=time(19, 0))
        ],
        contact=Contact(
            telephone="04 72 69 17 17",
            email="info@mac-lyon.com",
            website="https://www.mac-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/echos_passe.jpg",
                alt="Affiche de l'exposition Échos du passé, promesses du futur",
                is_main=True
            )
        ],
        start_date=datetime(2023, 9, 13),
        end_date=datetime(2025, 7, 13),
        price=10.0,
        is_free=False,
        booking_url="https://www.mac-lyon.com/billetterie",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=402,
        category_id=2,  # Arts Visuels
        name="Univers Programmés",
        description="Examen de l'évolution des pratiques artistiques avec le développement des technologies de l'information.",
        address="81 Quai Charles de Gaulle", # MAC Lyon
        arrondissement=Arrondissement.LYON_6,
        coordinates=Coordinates(latitude=45.7848, longitude=4.8553),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(11, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(11, 0), close_time=time(19, 0)),
            OpeningHours(day="Dimanche", open_time=time(11, 0), close_time=time(19, 0))
        ],
        contact=Contact(
            telephone="04 72 69 17 17",
            email="info@mac-lyon.com",
            website="https://www.mac-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/univers_programmes.jpg",
                alt="Affiche de l'exposition Univers Programmés",
                is_main=True
            )
        ],
        start_date=datetime(2023, 9, 13),
        end_date=datetime(2025, 7, 13),
        price=10.0,
        is_free=False,
        booking_url="https://www.mac-lyon.com/billetterie",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=403,
        category_id=2,  # Arts Visuels
        name="Zurbarán. Réinventer un chef-d'œuvre",
        description="Exposition réunissant pour la première fois trois tableaux de Zurbarán représentant Saint François d'Assise.",
        address="20 Place des Terreaux", # Musée des Beaux-Arts
        arrondissement=Arrondissement.LYON_1,
        coordinates=Coordinates(latitude=45.7671, longitude=4.8339),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(10, 0), close_time=time(18, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Dimanche", open_time=time(10, 0), close_time=time(18, 0))
        ],
        contact=Contact(
            telephone="04 72 10 17 40",
            email="contact@mba-lyon.fr",
            website="https://www.mba-lyon.fr"
        ),
        images=[
            Image(
                url="https://example.com/images/zurbaran.jpg",
                alt="Exposition Zurbarán",
                is_main=True
            )
        ],
        start_date=datetime(2024, 3, 15),
        end_date=datetime(2024, 8, 1),
        price=12.0,
        is_free=False,
        booking_url="https://www.mba-lyon.fr/billetterie",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=404,
        category_id=2,  # Arts Visuels
        name="Van Gogh, l'expérience immersive",
        description="Spectacle son et lumière sur plus de 1 000 m², avec des projections des œuvres les plus fascinantes de l'artiste, accompagnées d'une expérience en réalité virtuelle.",
        address="La Sucrière, 49-50 Quai Rambaud",
        arrondissement=Arrondissement.LYON_2,
        coordinates=Coordinates(latitude=45.7377, longitude=4.8156),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Mardi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(10, 0), close_time=time(19, 0)),
            OpeningHours(day="Dimanche", open_time=time(10, 0), close_time=time(19, 0))
        ],
        contact=Contact(
            telephone="09 83 49 85 87",
            website="https://www.vangogh-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/van_gogh_immersive.jpg",
                alt="Exposition immersive Van Gogh",
                is_main=True
            )
        ],
        start_date=datetime(2024, 2, 1),
        end_date=datetime(2024, 9, 30),
        price=14.5,
        is_free=False,
        booking_url="https://www.vangogh-lyon.com/tickets",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Événements de spectacle vivant (catégorie 1)
performance_events = [
    Event(
        id=501,
        category_id=1,  # Spectacle Vivant
        name="Wozzeck d'Alban Berg",
        description="Production saluée pour sa scénographie innovante. Opéra en trois actes d'Alban Berg, basé sur la pièce de théâtre inachevée de Georg Büchner.",
        address="1 Place de la Comédie", # Opéra National de Lyon
        arrondissement=Arrondissement.LYON_1,
        coordinates=Coordinates(latitude=45.7677, longitude=4.8361),
        opening_hours=[
            OpeningHours(day="Mardi", open_time=time(19, 30), close_time=time(22, 0)),
            OpeningHours(day="Jeudi", open_time=time(19, 30), close_time=time(22, 0)),
            OpeningHours(day="Samedi", open_time=time(19, 30), close_time=time(22, 0)),
        ],
        contact=Contact(
            telephone="04 69 85 54 54",
            email="opera@lyon.fr",
            website="https://www.opera-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/wozzeck.jpg",
                alt="Affiche de Wozzeck d'Alban Berg",
                is_main=True
            )
        ],
        start_date=datetime(2024, 11, 10),
        end_date=datetime(2024, 11, 22),
        price=45.0,
        is_free=False,
        booking_url="https://www.opera-lyon.com/fr/programmation/wozzeck",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=502,
        category_id=1,  # Spectacle Vivant
        name="Béatrice et Bénédict d'Hector Berlioz",
        description="Adaptation comique basée sur Beaucoup de bruit pour rien de Shakespeare. Une production qui mêle humour et romance.",
        address="1 Place de la Comédie", # Opéra National de Lyon
        arrondissement=Arrondissement.LYON_1,
        coordinates=Coordinates(latitude=45.7677, longitude=4.8361),
        opening_hours=[
            OpeningHours(day="Mercredi", open_time=time(19, 30), close_time=time(22, 0)),
            OpeningHours(day="Vendredi", open_time=time(19, 30), close_time=time(22, 0)),
            OpeningHours(day="Dimanche", open_time=time(16, 0), close_time=time(18, 30)),
        ],
        contact=Contact(
            telephone="04 69 85 54 54",
            email="opera@lyon.fr",
            website="https://www.opera-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/beatrice_benedict.jpg",
                alt="Affiche de Béatrice et Bénédict",
                is_main=True
            )
        ],
        start_date=datetime(2024, 5, 10),
        end_date=datetime(2024, 5, 20),
        price=40.0,
        is_free=False,
        booking_url="https://www.opera-lyon.com/fr/programmation/beatrice-benedict",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=503,
        category_id=1,  # Spectacle Vivant
        name="Partitions d'instincts de Louis Combeaud",
        description="Impliquant des jeunes suivis en psychiatrie, des proches et des soignants. Un spectacle expérimental qui explore la relation entre santé mentale et créativité.",
        address="8 Avenue Jean Mermoz", # Maison de la Danse
        arrondissement=Arrondissement.LYON_8,
        coordinates=Coordinates(latitude=45.7406, longitude=4.8722),
        opening_hours=[
            OpeningHours(day="Vendredi", open_time=time(20, 0), close_time=time(21, 30)),
            OpeningHours(day="Samedi", open_time=time(20, 0), close_time=time(21, 30)),
        ],
        contact=Contact(
            telephone="04 72 78 18 00",
            email="info@maisondeladanse.com",
            website="https://www.maisondeladanse.com"
        ),
        images=[
            Image(
                url="https://example.com/images/partitions_instincts.jpg",
                alt="Affiche de Partitions d'instincts",
                is_main=True
            )
        ],
        start_date=datetime(2024, 9, 15),
        end_date=datetime(2024, 9, 16),
        price=15.0,
        is_free=False,
        booking_url="https://www.maisondeladanse.com/programmation/partitions-dinstincts",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=504,
        category_id=1,  # Spectacle Vivant
        name="Fête des Lumières",
        description="Installations lumineuses, projections et performances artistiques dans toute la ville. Tradition née en 1852 pour célébrer la Vierge Marie.",
        address="Place des Terreaux", # Point central mais l'événement est dans toute la ville
        arrondissement=Arrondissement.LYON_1,
        coordinates=Coordinates(latitude=45.7675, longitude=4.8335),
        opening_hours=[
            OpeningHours(day="Jeudi", open_time=time(19, 0), close_time=time(23, 0)),
            OpeningHours(day="Vendredi", open_time=time(19, 0), close_time=time(23, 0)),
            OpeningHours(day="Samedi", open_time=time(19, 0), close_time=time(23, 0)),
            OpeningHours(day="Dimanche", open_time=time(19, 0), close_time=time(23, 0)),
        ],
        contact=Contact(
            website="https://www.fetedeslumieres.lyon.fr"
        ),
        images=[
            Image(
                url="https://example.com/images/fete_lumieres.jpg",
                alt="Fête des Lumières sur la Place des Terreaux",
                is_main=True
            )
        ],
        start_date=datetime(2024, 12, 5),
        end_date=datetime(2024, 12, 8),
        price=0.0,
        is_free=True,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Événements de musique (catégorie 3)
music_events = [
    Event(
        id=601,
        category_id=3,  # Musique
        name="Nuits de Fourvière",
        description="Performances de James Blake, Patti Smith, et autres artistes internationaux dans un cadre historique exceptionnel.",
        address="6 Rue de l'Antiquaille", # Théâtre Antique de Fourvière
        arrondissement=Arrondissement.LYON_5,
        coordinates=Coordinates(latitude=45.7603, longitude=4.8196),
        opening_hours=[
            # Heures variables selon les spectacles, généralement 20h30
            OpeningHours(day="Lundi", open_time=time(20, 30), close_time=time(23, 30)),
            OpeningHours(day="Mardi", open_time=time(20, 30), close_time=time(23, 30)),
            OpeningHours(day="Mercredi", open_time=time(20, 30), close_time=time(23, 30)),
            OpeningHours(day="Jeudi", open_time=time(20, 30), close_time=time(23, 30)),
            OpeningHours(day="Vendredi", open_time=time(20, 30), close_time=time(23, 30)),
            OpeningHours(day="Samedi", open_time=time(20, 30), close_time=time(23, 30)),
            OpeningHours(day="Dimanche", open_time=time(20, 30), close_time=time(23, 30))
        ],
        contact=Contact(
            telephone="04 72 32 00 00",
            website="https://www.nuitsdefourviere.com"
        ),
        images=[
            Image(
                url="https://example.com/images/nuits_fourviere.jpg",
                alt="Concert aux Nuits de Fourvière",
                is_main=True
            )
        ],
        start_date=datetime(2024, 6, 1),
        end_date=datetime(2024, 8, 31),
        price=35.0, # Prix moyen, variable selon les spectacles
        is_free=False,
        booking_url="https://www.nuitsdefourviere.com/billetterie",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=602,
        category_id=3,  # Musique
        name="Nuits Sonores",
        description="Référence européenne des festivals électroniques, avec des artistes de renommée internationale et une programmation variée.",
        address="Divers lieux à Lyon", 
        arrondissement=Arrondissement.LYON_2, # Principalement dans le 2ème arrondissement
        coordinates=Coordinates(latitude=45.7464, longitude=4.8210), # Approximatif pour Les Subsistances
        opening_hours=[
            OpeningHours(day="Mercredi", open_time=time(19, 0), close_time=time(5, 0)),
            OpeningHours(day="Jeudi", open_time=time(19, 0), close_time=time(5, 0)),
            OpeningHours(day="Vendredi", open_time=time(19, 0), close_time=time(5, 0)),
            OpeningHours(day="Samedi", open_time=time(19, 0), close_time=time(5, 0)),
            OpeningHours(day="Dimanche", open_time=time(16, 0), close_time=time(0, 0))
        ],
        contact=Contact(
            telephone="04 78 27 86 04",
            email="info@nuits-sonores.com",
            website="https://www.nuits-sonores.com"
        ),
        images=[
            Image(
                url="https://example.com/images/nuits_sonores.jpg",
                alt="Foule au festival Nuits Sonores",
                is_main=True
            )
        ],
        start_date=datetime(2024, 5, 22),
        end_date=datetime(2024, 5, 26),
        price=30.0, # Prix moyen, variable selon les soirées
        is_free=False,
        booking_url="https://www.nuits-sonores.com/billetterie",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Event(
        id=603,
        category_id=3,  # Musique
        name="Woodstower",
        description="Festival engagé au Grand Parc Miribel proposant rap, électro et sensibilisation à l'écologie.",
        address="Grand Parc de Miribel-Jonage",
        arrondissement=Arrondissement.LYON_9, # En réalité à Vaulx-en-Velin, à l'est de Lyon
        coordinates=Coordinates(latitude=45.8006, longitude=4.9518),
        opening_hours=[
            OpeningHours(day="Jeudi", open_time=time(18, 0), close_time=time(2, 0)),
            OpeningHours(day="Vendredi", open_time=time(16, 0), close_time=time(4, 0)),
            OpeningHours(day="Samedi", open_time=time(14, 0), close_time=time(4, 0)),
            OpeningHours(day="Dimanche", open_time=time(14, 0), close_time=time(0, 0))
        ],
        contact=Contact(
            telephone="04 78 03 85 00",
            email="contact@woodstower.com",
            website="https://www.woodstower.com"
        ),
        images=[
            Image(
                url="https://example.com/images/woodstower.jpg",
                alt="Festival Woodstower",
                is_main=True
            )
        ],
        start_date=datetime(2024, 8, 29),
        end_date=datetime(2024, 9, 1),
        price=28.0, # Prix moyen, variable selon les jours
        is_free=False,
        booking_url="https://www.woodstower.com/billetterie",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Combinaison de tous les événements
events = art_events + performance_events + music_events

# Export simplifié pour intégration avec db/events.py
events_json = [event.dict() for event in events]
