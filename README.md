# Next.js + FastAPI Project

Ce projet est une application web moderne construite avec Next.js pour le frontend et FastAPI pour le backend.

## Technologies Utilisées

### Frontend

- Next.js 14 (Framework React)
- TypeScript
- Tailwind CSS
- PostCSS

### Backend

- FastAPI (Framework Python)
- Uvicorn (Serveur ASGI)

## Structure du Projet

```
.
├── frontend/          # Application Next.js
│   ├── app/          # Pages et routes de l'application
│   ├── components/   # Composants React réutilisables
│   └── public/       # Fichiers statiques
└── backend/          # Application FastAPI
    ├── main.py       # Point d'entrée de l'API
    └── requirements.txt # Dépendances Python
```

## Configuration du Frontend

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

Le frontend sera accessible à l'adresse <http://localhost:3000>

## Configuration du Backend

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

5. Lancez le serveur de développement :

```bash
uvicorn main:app --reload
```

L'API backend sera accessible à l'adresse <http://localhost:8000>
La documentation de l'API sera disponible à <http://localhost:8000/docs>

## Fonctionnalités

- Interface utilisateur moderne et réactive
- API RESTful avec documentation automatique
- Support TypeScript pour un développement plus robuste
- Styling avec Tailwind CSS pour un design responsive

## Contribution

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request
