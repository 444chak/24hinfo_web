# Organisation des données culturelles de Lyon

## Structure des fichiers CSV

### Musique
- **lieux_emblematiques.csv**: Lieux culturels dédiés à la musique à Lyon
  - *Colonnes*: Nom, Adresse, Code_Postal, Ville, Genre_principal, Particularite
- **artistes.csv**: Artistes lyonnais emblématiques et émergents
  - *Colonnes*: Nom, Genre, Particularite, Type (Emblématique/Émergent)
- **festivals.csv**: Festivals musicaux à Lyon et alentours
  - *Colonnes*: Nom, Periode, Style, Particularite
- **initiatives_soutien.csv**: Organisations de soutien aux artistes émergents
  - *Colonnes*: Nom, Description
- **contexte_historique.csv**: Contexte historique musical lyonnais
  - *Colonnes*: Periode, Description

### Arts
- **lieux_emblematiques.csv**: Musées et lieux d'exposition à Lyon
  - *Colonnes*: Nom, Adresse, Code_Postal, Type_Musee, Historique, Collections, Particularite
- **expositions.csv**: Expositions récentes et à venir
  - *Colonnes*: Musee, Nom_Exposition, Date_Debut, Date_Fin, Description

### Spectacle
- **lieux_emblematiques.csv**: Lieux dédiés aux spectacles vivants
  - *Colonnes*: Nom, Adresse, Code_Postal, Ville, Type, Historique, Capacite
- **evenements.csv**: Événements et spectacles notables
  - *Colonnes*: Lieu, Nom_Evenement, Date, Type, Description

## Notes d'utilisation
- Tous les fichiers sont encodés en UTF-8 pour prendre en charge les caractères accentués
- Le séparateur utilisé dans les CSV est le point-virgule (;)
- Les champs de texte contenant des points-virgules ou des virgules sont entourés de guillemets doubles
- Les dates sont au format JJ/MM/AAAA lorsque disponibles
- Certains champs peuvent être vides lorsque l'information n'est pas disponible
