# Senegal Trip Planner

Application Flask de planification de voyage au Sénégal avec calcul d'itinéraires et optimisation TSP.

## Fonctionnalités

- Liste des 14 régions du Sénégal avec infos et conseils
- Calcul d'itinéraire avec Dijkstra (route nationale ou autoroute)
- Optimisation TSP pour visiter toutes les régions

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python3 app.py
```

Serveur accessible sur http://localhost:5000

## API

- `GET /api/regions` - Liste des régions
- `GET /api/dijkstra?start=dakar&destination=ziguinchor` - Itinéraire
- `GET /api/tsp?start=dakar` - Circuit optimal

## Déployé

https://senegal-trip-planner.streamlit.app