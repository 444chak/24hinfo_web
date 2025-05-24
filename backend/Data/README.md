# Structure des données

Ce dossier contient les fichiers de données au format CSV pour l'application 24hinfo. Tous les fichiers suivent une structure standardisée pour assurer la cohérence des données.

## Structure standardisée

Tous les fichiers CSV doivent suivre cette structure de base :

### Champs obligatoires

- `id` : Identifiant unique (entier)
- `name` : Nom du lieu/événement (texte)
- `description` : Description détaillée (texte)
- `category_id` : ID de la catégorie (entier, référence à categories.csv)
- `address` : Adresse complète (texte)
- `arrondissement` : Arrondissement de Lyon (texte)
- `latitude` : Coordonnée géographique (nombre décimal)
- `longitude` : Coordonnée géographique (nombre décimal)
- `created_at` : Date de création (timestamp ISO 8601)
- `updated_at` : Date de dernière modification (timestamp ISO 8601)

### Champs optionnels

- `contact_telephone` : Numéro de téléphone (texte)
- `contact_email` : Adresse email (texte)
- `contact_website` : Site web (URL)
- `accessibility` : Informations sur l'accessibilité (texte)
- `amenities` : Équipements et services disponibles (texte, séparés par des points-virgules)

## Fichiers de données

### categories.csv

Contient les catégories principales avec les champs spécifiques :

- `icon` : Icône associée (texte)
- `primary` : Couleur principale (code hexadécimal)

### monuments_lyon.csv

Contient les monuments historiques avec les champs spécifiques :

- `built_year` : Année de construction (entier)
- `architectural_style` : Style architectural (texte)
- `historical_period` : Période historique (texte)
- `is_unesco` : Patrimoine UNESCO (booléen)

### musees_lyon.csv

Contient les musées et lieux culturels avec les champs spécifiques :

- `founded_year` : Année de création (entier)
- `accessibility` : Informations sur l'accessibilité (texte)
- `amenities` : Équipements et services (texte)

### bibliotheques_lyon.csv

Contient les bibliothèques et lieux de lecture avec les champs spécifiques :

- `founded_year` : Année de création (entier, optionnel)
- `accessibility` : Informations sur l'accessibilité (texte, ex: "Accès PMR; Ascenseur")
- `amenities` : Équipements et services (texte, ex: "Café; Collections numériques; Scanner")

### lieux_emblematiques.csv (Spectacle/Musique/Arts)

Contient les lieux culturels spécifiques à chaque catégorie avec les champs spécifiques :

- `type` : Type de lieu (texte, ex: "Théâtre", "Opéra", "Salle de concert")
- `capacity` : Capacité d'accueil (entier)
- `historical_info` : Informations historiques (texte)
- `accessibility` : Informations sur l'accessibilité (texte)
- `amenities` : Équipements et services (texte)

### evenements.csv (Spectacle)

Contient les événements de spectacle avec les champs spécifiques :

- `venue_id` : ID du lieu (entier, référence à lieux_emblematiques.csv)
- `start_date` : Date de début (timestamp ISO 8601)
- `end_date` : Date de fin (timestamp ISO 8601)
- `type` : Type d'événement (texte)
- `price_range` : Fourchette de prix (texte)
- `accessibility` : Informations sur l'accessibilité (texte)

### festivals.csv (Musique)

Contient les festivals musicaux avec les champs spécifiques :

- `venue_id` : ID du lieu (entier, référence à lieux_emblematiques.csv)
- `start_date` : Date de début (timestamp ISO 8601)
- `end_date` : Date de fin (timestamp ISO 8601)
- `genre` : Genre musical principal (texte)
- `price_range` : Fourchette de prix (texte)
- `accessibility` : Informations sur l'accessibilité (texte)

### expositions.csv (Arts)

Contient les expositions avec les champs spécifiques :

- `venue_id` : ID du lieu (entier, référence à lieux_emblematiques.csv)
- `start_date` : Date de début (timestamp ISO 8601)
- `end_date` : Date de fin (timestamp ISO 8601)
- `artistic_movement` : Mouvement artistique (texte)
- `price_range` : Fourchette de prix (texte)
- `accessibility` : Informations sur l'accessibilité (texte)

### artistes.csv (Musique)

Contient les artistes musicaux avec les champs spécifiques :

- `genre` : Genre musical (texte)
- `type` : Type d'artiste (texte, ex: "Emblématique", "Émergent")
- `particularity` : Particularités (texte)
- `website` : Site web (URL)
- `social_media` : Réseaux sociaux (texte, séparés par des points-virgules)

### initiatives_soutien.csv (Musique)

Contient les initiatives de soutien aux artistes avec les champs spécifiques :

- `type` : Type d'initiative (texte)
- `description` : Description détaillée (texte)
- `website` : Site web (URL)
- `contact_info` : Informations de contact (texte)

### contexte_historique.csv (Musique)

Contient le contexte historique musical avec les champs spécifiques :

- `period` : Période historique (texte)
- `description` : Description détaillée (texte)
- `key_events` : Événements clés (texte, séparés par des points-virgules)

## Format des données

- Les dates sont au format ISO 8601 : YYYY-MM-DDThh:mm:ss.ssssss
- Les coordonnées géographiques sont en degrés décimaux
- Les booléens sont représentés par "True" ou "False"
- Les listes sont séparées par des points-virgules
- Les textes contenant des virgules sont entourés de guillemets doubles
