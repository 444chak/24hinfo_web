# Lumyons - Mettre en Lumière la Ville de Lyon

Une application web moderne qui met en valeur la beauté et le dynamisme de la ville de Lyon, construite avec Next.js pour le frontend et FastAPI pour le backend. Ce projet a été développé dans le cadre des 24h de l'informatique des IUT 2025.

## 🌟 Fonctionnalités Principales

- 🏛️ Présentation des monuments et lieux emblématiques
- 🎭 Agenda culturel et événements
- 📸 Galerie photos des plus beaux endroits
- 🗺️ Cartographie interactive des points d'intérêt
- 🍽️ Guide des restaurants et commerces
- 🏨 Informations touristiques et pratiques
- 📱 Version mobile responsive

## 🛠️ Technologies Utilisées

### Frontend

- Next.js 14 (Framework React)
- TypeScript
- Tailwind CSS
- React Query (Gestion des données)

### Backend

- FastAPI (Framework Python)
- Uvicorn (Serveur ASGI)
- SQLite (Base de données)

## 📁 Structure du Projet

```txt
.
├── frontend/                 # Application Next.js
│   ├── app/                 # Pages et routes de l'application
│   ├── components/          # Composants React réutilisables
│   ├── lib/                 # Utilitaires et configurations
│   ├── public/              # Fichiers statiques
│   └── styles/              # Styles globaux
└── backend/                 # Application FastAPI
    ├── app/                 # Code source principal
    │   ├── api/            # Points d'entrée API
    │   ├── core/           # Configuration et utilitaires
    │   ├── models/         # Modèles de données
    │   └── services/       # Logique métier
    ├── alembic/            # Migrations de base de données
    └── tests/              # Tests unitaires et d'intégration
```

## 🚀 Installation

### Prérequis

- Node.js 18+
- Python 3.9+

### Configuration du Frontend

1. Naviguez vers le dossier frontend :

```bash
cd frontend
```

2. Installez les dépendances :

```bash
npm install
```

3. Lancez le serveur de développement :

```bash
npm run dev
```

Le frontend sera accessible à l'adresse [http://localhost:3000](http://localhost:3000)

### Configuration du Backend

1. Naviguez vers le dossier backend :

```bash
cd backend
```

2. Créez un environnement virtuel :

```bash
python -m venv venv
```

3. Activez l'environnement virtuel :

- Windows :

```bash
.\venv\Scripts\activate
```

- Unix/MacOS :

```bash
source venv/bin/activate
```

4. Installez les dépendances :

```bash
pip install -r requirements.txt
```

5. Configurez les variables d'environnement :

```bash
cp .env.example .env
```

6. Lancez le serveur de développement :

```bash
uvicorn app.main:app --reload
```

L'API backend sera accessible à l'adresse [http://localhost:8001](http://localhost:8001)
La documentation de l'API sera disponible à [http://localhost:8001/docs](http://localhost:8001/docs)

## 📝 Documentation

- [Documentation API](http://localhost:8001/docs)

## 🤝 Contribution

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
