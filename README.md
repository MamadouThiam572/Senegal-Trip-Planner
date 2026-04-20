# Senegal Trip Planner

_application web de planification de voyage au Sénégal_

## Présentation

Senegal Trip Planner est une application Flask interactive qui permet de planifier des voyages à travers les 14 régions du Sénégal. Elle propose deux fonctionnalités principales :

1. **Calcul d'itinéraire** - Trouve le chemin le plus court entre deux régions en utilisant l'algorithme de Dijkstra
2. **Circuit touristique (TSP)** - Calcule le parcours optimal pour visiter toutes les régions du Sénégal

## Les 14 régions

| Région | Capitale | Particularité |
|--------|----------|---------------|
| Dakar | Dakar | Capitale du Sénégal |
| Thiès | Thiès | Deuxième ville, pôle industriel |
| Diourbel | Diourbel | Capitale du Mboss, région religieuse |
| Kaolack | Kaolack | Centre économique du bassin arachidier |
| Saint-Louis | Saint-Louis | Ancienne capitale coloniale, patrimoine UNESCO |
| Louga | Louga | Région sahélienne, élevage et commerce |
| Kolda | Kolda | Région verdoyante au sud |
| Ziguinchor | Ziguinchor | Capitale du sud, vibes caribéennes |
| Sédhiou | Sédhiou | Transition Sine et Saloum |
| Kaffrine | Kaffrine | Cœur du pays Serer |
| Kédougou | Kédougou | Plus orientale, reserve Niokolo-Koba |
| Matam | Matam | Sahélienne sur le fleuve Niger |
| Tambacounda | Tambacounda | Plus grande région, porte du Sahel |
| Fatick | Fatick | Sine-Saloum, lagunes et mangroves |

## Modes de route

- **Route nationale** - Roads classiques
- **Autoroute** - Aéroports et routes rapides

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal-Trip-Planner

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

```bash
python3 app.py
```

Puis ouvrir http://localhost:5000 dans votre navigateur.

## API Endpoints

| Endpoint | Description |
|---------|-------------|
| `GET /api/regions` | Liste toutes les régions avec leurs infos |
| `GET /api/dijkstra?start=X&destination=Y` | Itinéraire entre X et Y |
| `GET /api/tsp?start=X` | Circuit optimal depuis X |

## Exemple d'utilisation API

```bash
# Itinéraire de Dakar à Ziguinchor
curl "http://localhost:5000/api/dijkstra?start=dakar&destination=ziguinchor"

# Circuit touristique depuis Dakar
curl "http://localhost:5000/api/tsp?start=dakar"
```

## Déployé

Accessible en ligne : https://senegal-trip-planner.streamlit.app

## Technologie

- **Backend** : Flask (Python)
- **Frontend** : HTML, CSS, JavaScript
- **Algorithmes** : Dijkstra, Nearest Neighbor + 2-opt

---

Développé par Mamadou Thiam