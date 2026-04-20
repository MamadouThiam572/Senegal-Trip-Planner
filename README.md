# Senegal Trip Planner

_application web de planification de voyage au Sénégal_

## Présentation du projet

Senegal Trip Planner est une application web développée dans le cadre d'un projet académique qui permet de planifier des voyages à travers les 14 régions du Sénégal. Elle propose deux fonctionnalités principales :

1. **Calcul d'itinéraire** — Trouve le chemin le plus court entre deux régions en utilisant l'algorithme de Dijkstra
2. **Circuit touristique (TSP)** — Calcule le parcours optimal pour visiter toutes les régions du Sénégal en utilisant une approche nearest neighbor combinée avec 2-opt

## Les 14 régions du Sénégal

| # | Région | Capitale | Latitude | Longitude |
|---|--------|----------|----------|-----------|
| 1 | Dakar | Dakar | 14.7167 | -17.4671 |
| 2 | Thiès | Thiès | 14.7941 | -16.9639 |
| 3 | Diourbel | Diourbel | 14.7167 | -16.2333 |
| 4 | Kaolack | Kaolack | 14.1500 | -16.0833 |
| 5 | Saint-Louis | Saint-Louis | 16.0333 | -16.5000 |
| 6 | Louga | Louga | 15.6333 | -15.6333 |
| 7 | Kolda | Kolda | 12.8833 | -14.9500 |
| 8 | Ziguinchor | Ziguinchor | 12.5833 | -16.2667 |
| 9 | Sédhiou | Sédhiou | 12.7167 | -15.1833 |
| 10 | Kaffrine | Kaffrine | 14.1000 | -15.4167 |
| 11 | Kédougou | Kédougou | 12.5667 | -12.1833 |
| 12 | Matam | Matam | 15.6667 | -13.2667 |
| 13 | Tambacounda | Tambacounda | 13.7667 | -13.6667 |
| 14 | Fatick | Fatick | 14.3333 | -16.0833 |

Chaque région possède des informations descriptives et des conseils pratiques pour les voyageurs.

## Types de routes

L'application propose deux modes de calcul d'itinéraire :

- **Route nationale** — Routes classiques empruntees
- **Autoroute** — Routes rapides et aeroports

Les distances sont-stockees dans deux matrices distinctes permettant de comparer les deux options.

## Algorithmes utilises

### Dijkstra (Itinéraire le plus court)

L'algorithme de Dijkstra est implémente pour trouver le chemin le plus court entre deux regions. Il utilise une approche gloutonne avec exploration des nœœuds par distance croissante.

Complexité : O(V²) où V = nombre de régions

### Two-Phase TSP (Problème du voyageur de commerce)

L'algorithme TSP utilise une approche en deux phases :

**Phase 1 : Nearest Neighbor (Construction)**
- Commencer depuis une région de départ
- Visite répété la région non visitée la plus proche
- Retour au point de départ une fois toutes les régions visitées

Complexité : O(n²) où n = nombre de régions

**Phase 2 : 2-opt (Optimisation locale)**
- Supprimer deux arêtes du parcours
- Les reconnecter en sens inverse
- Répéter jusqu'à aucune amélioration

Complexité : O(n² × itérations)

Cette approche hybride permet d'obtenir un bon compromis entre qualité de la solution et temps de calcul.

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal-Trip-Planner

# Installer les dépendances
pip install -r requirements.txt
```

## Lancement

```bash
python3 app.py
```

Puis ouvrir http://localhost:5000 dans votre navigateur.

## API Endpoints

| Endpoint | Methode | Description |
|----------|---------|-------------|
| `/api/regions` | GET | Liste toutes les régions avec leurs infos |
| `/api/dijkstra` | GET | Itinéraire entre deux régions |
| `/api/tsp` | GET | Circuit optimal depuis une région |

## Exemples d'utilisation API

```bash
# Itinéraire de Dakar à Ziguinchor (route nationale + autoroute)
curl "http://localhost:5000/api/dijkstra?start=dakar&destination=ziguinchor"

# Circuit touristique depuis Dakar
curl "http://localhost:5000/api/tsp?start=dakar"

# Liste des régions
curl "http://localhost:5000/api/regions"
```

## Structure du projet

```
Senegal_Trip_Planner/
├── app.py                 # Application Flask (API + routes)
├── templates/
│   └── index.html        # Interface utilisateur
├── requirements.txt      # Dépendances Python
└── README.md           # Documentation
```

## Interface utilisateur

L'application dispose d'une interface web interactive avec :
- Carte Leaflet displayant les 14 régions
- Liste déroulante pour sélectionner départ et destination
- Boutons pour calculerITINERAIRE ou circuit TSP
- Comparaison visuelle route nationale vs autoroute
- Informations sur chaque région

## Technologies

- **Backend** : Flask (Python 3)
- **Frontend** : HTML, CSS, JavaScript
- **Carte** : Leaflet + OpenStreetMap
- **Algorithmes** : Dijkstra, Nearest Neighbor, 2-opt

## Auteurs

Projet développé dans le cadre d'un projet académique.

---

Développé par Mamadou Thiam