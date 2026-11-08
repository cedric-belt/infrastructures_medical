# Documentation API

## Base URL

```text
http://localhost:5000/api/v1
```

## Endpoints

### GET /health

Retourne l'état du service.

Exemple :

```bash
curl http://localhost:5000/health
```

### GET /equipment

Récupère la liste de tous les équipements.

### POST /equipment

Créer un équipement.

Exemple :

```bash
curl -X POST http://localhost:5000/api/v1/equipment \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Scanner IRM",
    "category": "imagerie",
    "location": "Bloc 2",
    "status": "operational",
    "serial_number": "IRM-2045"
  }'
```

### GET /equipment/<id>

Récupère les détails d'un équipement spécifique.

### GET /alerts

Renvoie les équipements concernés par une alerte ou une maintenance requise.

### GET /patients

Liste les patients connus par le système.

### POST /patients

Crée un patient dans le système.

### Exemple de réponse

```json
{
  "id": 1,
  "message": "Équipement ajouté"
}
```
