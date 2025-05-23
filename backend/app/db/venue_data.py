"""
Module contenant les données pour les lieux culturels (venues) à Lyon.
Généré à partir des fichiers CSV existants.
"""
from datetime import datetime, time
from app.models.cultural_items import Venue
from app.models.base import Arrondissement, Coordinates, OpeningHours, Contact, Image

# Lieux de spectacle vivant (catégorie 1)
spectacle_venues = [
    Venue(
        id=101,
        category_id=1,  # Spectacle Vivant
        name="Opéra National de Lyon",
        description="Construit en 1831 sous le nom de « Grand Théâtre », il a été entièrement restructuré entre 1989 et 1993 par l'architecte Jean Nouvel, qui a ajouté une coupole en verre et acier.",
        address="1 Place de la Comédie",
        arrondissement=Arrondissement.LYON_1,
        coordinates=Coordinates(latitude=45.7677, longitude=4.8361),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(9, 0), close_time=time(17, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(12, 0), close_time=time(19, 0)),
            OpeningHours(day="Mercredi", open_time=time(12, 0), close_time=time(19, 0)),
            OpeningHours(day="Jeudi", open_time=time(12, 0), close_time=time(19, 0)),
            OpeningHours(day="Vendredi", open_time=time(12, 0), close_time=time(19, 0)),
            OpeningHours(day="Samedi", open_time=time(12, 0), close_time=time(19, 0)),
            OpeningHours(day="Dimanche", open_time=time(12, 0), close_time=time(17, 0))
        ],
        contact=Contact(
            telephone="04 69 85 54 54",
            email="opera@lyon.fr",
            website="https://www.opera-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/opera_lyon.jpg",
                alt="Façade de l'Opéra National de Lyon",
                is_main=True
            )
        ],
        founded_year=1831,
        accessibility=["Fauteuil roulant", "Aides auditives"],
        amenities=["Bar", "Boutique"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=102,
        category_id=1,  # Spectacle Vivant
        name="Théâtre des Célestins",
        description="Fondé en 1792, le théâtre a été reconstruit en 1877 par l'architecte Gaspard André après un incendie. Il est inscrit aux monuments historiques depuis 1997.",
        address="4 Rue Charles Dullin",
        arrondissement=Arrondissement.LYON_2,
        coordinates=Coordinates(latitude=45.7635, longitude=4.8338),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(13, 0), close_time=time(17, 0)),
            OpeningHours(day="Mardi", open_time=time(13, 0), close_time=time(18, 30)),
            OpeningHours(day="Mercredi", open_time=time(13, 0), close_time=time(18, 30)),
            OpeningHours(day="Jeudi", open_time=time(13, 0), close_time=time(18, 30)),
            OpeningHours(day="Vendredi", open_time=time(13, 0), close_time=time(18, 30)),
            OpeningHours(day="Samedi", open_time=time(11, 0), close_time=time(18, 30)),
            OpeningHours(day="Dimanche", open_time=time(11, 0), close_time=time(16, 0))
        ],
        contact=Contact(
            telephone="04 72 77 40 00",
            email="contact@celestins-lyon.org",
            website="https://www.theatredescelestins.com"
        ),
        images=[
            Image(
                url="https://example.com/images/celestins.jpg",
                alt="Façade du Théâtre des Célestins",
                is_main=True
            )
        ],
        founded_year=1792,
        accessibility=["Fauteuil roulant", "Aides auditives"],
        amenities=["Bar"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=103,
        category_id=1,  # Spectacle Vivant
        name="Théâtre Antique de Fourvière",
        description="Théâtre romain construit à la fin du Ier siècle après J.-C. qui accueille chaque été le festival des Nuits de Fourvière.",
        address="6 Rue de l'Antiquaille",
        arrondissement=Arrondissement.LYON_5,
        coordinates=Coordinates(latitude=45.7603, longitude=4.8196),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(9, 0), close_time=time(19, 0)),
            OpeningHours(day="Mardi", open_time=time(9, 0), close_time=time(19, 0)),
            OpeningHours(day="Mercredi", open_time=time(9, 0), close_time=time(19, 0)),
            OpeningHours(day="Jeudi", open_time=time(9, 0), close_time=time(19, 0)),
            OpeningHours(day="Vendredi", open_time=time(9, 0), close_time=time(19, 0)),
            OpeningHours(day="Samedi", open_time=time(9, 0), close_time=time(19, 0)),
            OpeningHours(day="Dimanche", open_time=time(9, 0), close_time=time(19, 0))
        ],
        contact=Contact(
            telephone="04 72 32 00 00",
            website="https://www.nuitsdefourviere.com"
        ),
        images=[
            Image(
                url="https://example.com/images/fourviere.jpg",
                alt="Théâtre antique de Fourvière",
                is_main=True
            )
        ],
        founded_year=100,  # Fin du Ier siècle
        accessibility=["Accès limité pour les fauteuils roulants"],
        amenities=["Toilettes"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=104,
        category_id=1,  # Spectacle Vivant
        name="Maison de la Danse",
        description="Fondée en 1980 par cinq chorégraphes lyonnais, elle déménage en 1992 dans l'ancien Théâtre du 8ème.",
        address="8 Avenue Jean Mermoz",
        arrondissement=Arrondissement.LYON_8,
        coordinates=Coordinates(latitude=45.7406, longitude=4.8722),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(10, 0), close_time=time(19, 0)),
            OpeningHours(day="Mercredi", open_time=time(10, 0), close_time=time(19, 0)),
            OpeningHours(day="Jeudi", open_time=time(10, 0), close_time=time(19, 0)),
            OpeningHours(day="Vendredi", open_time=time(10, 0), close_time=time(19, 0)),
            OpeningHours(day="Samedi", open_time=time(10, 0), close_time=time(19, 0), is_closed=True),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 72 78 18 00",
            email="info@maisondeladanse.com",
            website="https://www.maisondeladanse.com"
        ),
        images=[
            Image(
                url="https://example.com/images/maison_danse.jpg",
                alt="Entrée de la Maison de la Danse",
                is_main=True
            )
        ],
        founded_year=1980,
        accessibility=["Fauteuil roulant", "Aides auditives", "Places adaptées"],
        amenities=["Bar", "Vestiaire"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=105,
        category_id=1,  # Spectacle Vivant
        name="Théâtre Tête d'Or",
        description="Ouvert en 1980 dans une ancienne cartonnerie, il s'installe en 2001 dans l'ancienne salle La Cigale, datant de 1925.",
        address="60 Avenue du Maréchal de Saxe",
        arrondissement=Arrondissement.LYON_3,
        coordinates=Coordinates(latitude=45.7616, longitude=4.8453),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(13, 30), close_time=time(18, 30)),
            OpeningHours(day="Mercredi", open_time=time(13, 30), close_time=time(18, 30)),
            OpeningHours(day="Jeudi", open_time=time(13, 30), close_time=time(18, 30)),
            OpeningHours(day="Vendredi", open_time=time(13, 30), close_time=time(18, 30)),
            OpeningHours(day="Samedi", open_time=time(13, 30), close_time=time(18, 30)),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 78 62 96 73",
            email="billetterie@theatretetedor.com",
            website="https://www.theatretetedor.com"
        ),
        images=[
            Image(
                url="https://example.com/images/tete_dor.jpg",
                alt="Entrée du Théâtre Tête d'Or",
                is_main=True
            )
        ],
        founded_year=1980,
        accessibility=["Fauteuil roulant"],
        amenities=["Bar"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=106,
        category_id=1,  # Spectacle Vivant
        name="Cirque Imagine",
        description="Créé en 1999 par la famille Massot, le cirque s'est installé de manière permanente aux portes de Lyon, proposant un concept inédit de dîner-spectacle cabaret-cirque.",
        address="5 Avenue des Canuts, Carré de Soie",
        arrondissement=Arrondissement.VILLEURBANNE,
        coordinates=Coordinates(latitude=45.7664, longitude=4.9193),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Mardi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(18, 0), close_time=time(23, 59)),
            OpeningHours(day="Dimanche", open_time=time(12, 0), close_time=time(16, 0))
        ],
        contact=Contact(
            telephone="04 78 24 32 43",
            email="contact@cirqueimagine.com",
            website="https://www.cirqueimagine.com"
        ),
        images=[
            Image(
                url="https://example.com/images/cirque_imagine.jpg",
                alt="Chapiteau du Cirque Imagine",
                is_main=True
            )
        ],
        founded_year=1999,
        accessibility=["Fauteuil roulant", "Toilettes adaptées"],
        amenities=["Restaurant", "Parking"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Lieux des arts visuels (catégorie 2)
arts_venues = [
    Venue(
        id=201,
        category_id=2,  # Arts Visuels
        name="Musée des Beaux-Arts de Lyon",
        description="Installé dans une ancienne abbaye bénédictine du XVIIe siècle, le musée abrite une des plus riches collections d'art en France, couvrant 5 000 ans d'histoire, de l'Égypte antique à l'art moderne.",
        address="20 Place des Terreaux",
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
                url="https://example.com/images/mba_lyon.jpg",
                alt="Cour intérieure du Musée des Beaux-Arts de Lyon",
                is_main=True
            )
        ],
        founded_year=1801,
        accessibility=["Fauteuil roulant", "Ascenseurs", "Toilettes adaptées"],
        amenities=["Boutique", "Café", "Vestiaire", "Audioguides"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=202,
        category_id=2,  # Arts Visuels
        name="Musée d'Art Contemporain de Lyon (MAC Lyon)",
        description="Inauguré en 1995, le MAC Lyon est dédié à l'art contemporain sous toutes ses formes.",
        address="81 Quai Charles de Gaulle",
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
                url="https://example.com/images/mac_lyon.jpg",
                alt="Façade du Musée d'Art Contemporain de Lyon",
                is_main=True
            )
        ],
        founded_year=1995,
        accessibility=["Fauteuil roulant", "Ascenseurs"],
        amenities=["Boutique", "Café", "Librairie spécialisée"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=203,
        category_id=2,  # Arts Visuels
        name="Musée des Tissus et des Arts Décoratifs",
        description="Fondé en 1864, il possède l'une des plus importantes collections mondiales de textiles, avec plus de 2,5 millions de pièces.",
        address="34 Rue de la Charité",
        arrondissement=Arrondissement.LYON_2,
        coordinates=Coordinates(latitude=45.7535, longitude=4.8281),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(10, 0), close_time=time(18, 0)),
            OpeningHours(day="Dimanche", open_time=time(10, 0), close_time=time(18, 0))
        ],
        contact=Contact(
            telephone="04 78 38 42 00",
            email="contact@mtmad.fr",
            website="https://www.mtmad.fr"
        ),
        images=[
            Image(
                url="https://example.com/images/musee_tissus.jpg",
                alt="Façade du Musée des Tissus",
                is_main=True
            )
        ],
        founded_year=1864,
        accessibility=["Actuellement fermé pour rénovation"],
        amenities=["Boutique"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=204,
        category_id=2,  # Arts Visuels
        name="Musée des Moulages",
        description="Créé en 1899, il abrite environ 2 000 moulages d'œuvres antiques, médiévales, renaissance et modernes.",
        address="87 Cours Gambetta",
        arrondissement=Arrondissement.LYON_3,
        coordinates=Coordinates(latitude=45.7521, longitude=4.8617),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(14, 0), close_time=time(17, 0)),
            OpeningHours(day="Mercredi", open_time=time(14, 0), close_time=time(17, 0)),
            OpeningHours(day="Jeudi", open_time=time(14, 0), close_time=time(17, 0)),
            OpeningHours(day="Vendredi", open_time=time(14, 0), close_time=time(17, 0)),
            OpeningHours(day="Samedi", open_time=time(10, 0), close_time=time(17, 0)),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 72 84 81 12",
            email="musee.moulages@univ-lyon2.fr",
            website="https://www.musee-des-moulages.univ-lyon2.fr"
        ),
        images=[
            Image(
                url="https://example.com/images/musee_moulages.jpg",
                alt="Collection du Musée des Moulages",
                is_main=True
            )
        ],
        founded_year=1899,
        accessibility=["Accès limité pour les fauteuils roulants"],
        amenities=[],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Lieux de musique (catégorie 3)
music_venues = [
    Venue(
        id=301,
        category_id=3,  # Musique
        name="Auditorium-Orchestre National de Lyon",
        description="Inauguré en 1975, c'est la première salle en France construite exclusivement pour la musique. Acoustique exceptionnelle, lieu de prestige.",
        address="149 Rue Garibaldi",
        arrondissement=Arrondissement.LYON_3,
        coordinates=Coordinates(latitude=45.7621, longitude=4.8513),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(12, 0), close_time=time(18, 0)),
            OpeningHours(day="Mercredi", open_time=time(12, 0), close_time=time(18, 0)),
            OpeningHours(day="Jeudi", open_time=time(12, 0), close_time=time(18, 0)),
            OpeningHours(day="Vendredi", open_time=time(12, 0), close_time=time(18, 0)),
            OpeningHours(day="Samedi", open_time=time(12, 0), close_time=time(18, 0)),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 78 95 95 95",
            email="contact@auditorium-lyon.com",
            website="https://www.auditorium-lyon.com"
        ),
        images=[
            Image(
                url="https://example.com/images/auditorium_lyon.jpg",
                alt="Auditorium de Lyon",
                is_main=True
            )
        ],
        founded_year=1975,
        accessibility=["Fauteuil roulant", "Aides auditives", "Places adaptées"],
        amenities=["Bar", "Vestiaire", "Parking"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=302,
        category_id=3,  # Musique
        name="Le Transbordeur",
        description="Grande salle (1800 places) avec programmation internationale de musiques actuelles (rock, électro, rap).",
        address="3 Bd Stalingrad",
        arrondissement=Arrondissement.VILLEURBANNE,
        coordinates=Coordinates(latitude=45.7835, longitude=4.8626),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mercredi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Jeudi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Vendredi", open_time=time(19, 0), close_time=time(5, 0)),
            OpeningHours(day="Samedi", open_time=time(19, 0), close_time=time(5, 0)),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 78 93 08 33",
            email="info@transbordeur.fr",
            website="https://www.transbordeur.fr"
        ),
        images=[
            Image(
                url="https://example.com/images/transbordeur.jpg",
                alt="Le Transbordeur",
                is_main=True
            )
        ],
        founded_year=1989,
        accessibility=["Fauteuil roulant"],
        amenities=["Bar", "Vestiaire"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=303,
        category_id=3,  # Musique
        name="L'Épicerie Moderne",
        description="Salle de concert dédiée aux musiques indé, électro et rock, avec un soutien aux artistes émergents.",
        address="Place René Lescot",
        arrondissement=Arrondissement.LYON_9,  # En réalité à Feyzin, mais proche de Lyon
        coordinates=Coordinates(latitude=45.6773, longitude=4.8589),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mercredi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Jeudi", open_time=time(19, 0), close_time=time(23, 0)),
            OpeningHours(day="Vendredi", open_time=time(20, 0), close_time=time(1, 0)),
            OpeningHours(day="Samedi", open_time=time(20, 0), close_time=time(1, 0)),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 72 89 98 70",
            email="contact@epiceriemoderne.com",
            website="https://www.epiceriemoderne.com"
        ),
        images=[
            Image(
                url="https://example.com/images/epicerie_moderne.jpg",
                alt="L'Épicerie Moderne",
                is_main=True
            )
        ],
        founded_year=1995,
        accessibility=["Fauteuil roulant"],
        amenities=["Bar"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Venue(
        id=304,
        category_id=3,  # Musique
        name="Marché Gare",
        description="Salle underground très active proposant de la musique rock, hip-hop, électro et world.",
        address="34 Rue Casimir Périer",
        arrondissement=Arrondissement.LYON_2,
        coordinates=Coordinates(latitude=45.7433, longitude=4.8241),
        opening_hours=[
            OpeningHours(day="Lundi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mardi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Mercredi", open_time=time(0, 0), close_time=time(0, 0), is_closed=True),
            OpeningHours(day="Jeudi", open_time=time(20, 0), close_time=time(1, 0)),
            OpeningHours(day="Vendredi", open_time=time(20, 0), close_time=time(3, 0)),
            OpeningHours(day="Samedi", open_time=time(20, 0), close_time=time(3, 0)),
            OpeningHours(day="Dimanche", open_time=time(0, 0), close_time=time(0, 0), is_closed=True)
        ],
        contact=Contact(
            telephone="04 72 40 97 13",
            email="info@marchegare.fr",
            website="https://www.marchegare.fr"
        ),
        images=[
            Image(
                url="https://example.com/images/marche_gare.jpg",
                alt="Marché Gare",
                is_main=True
            )
        ],
        founded_year=1988,
        accessibility=["Accès limité pour les fauteuils roulants"],
        amenities=["Bar"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Combinaison de tous les lieux
venues = spectacle_venues + arts_venues + music_venues

# Export simplifié pour intégration avec db/venues.py
venues_json = [venue.dict() for venue in venues]
