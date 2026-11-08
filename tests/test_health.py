# Guide de déploiement

## Environnement de développement

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

## Environnement Docker

```bash
docker compose up --build
```

## Variables d'environnement

- `SECRET_KEY` : clé secrète Flask
- `DATABASE_URL` : chaîne SQLite ou PostgreSQL

Exemple :

```env
SECRET_KEY=super-secret-key
DATABASE_URL=sqlite:////app/data/app.db
```

## Production

Pour un environnement de production, il est conseillé de :
- migrer vers PostgreSQL ;
- utiliser un serveur WSGI tel que Gunicorn ;
- mettre en place un reverse proxy nginx ou Traefik ;
- sécuriser les accès à la base de données ;
- activer la supervision et la journalisation ;
- définir des règles de sauvegarde.

## Sauvegarde

```bash
cp data/app.db data/app.db.backup
```

## Vérifications

```bash
curl http://localhost:5000/health
```
