# Senegal Trip Planner 🧭

Application web de planification de voyage au Sénégal. Elle permet de calculer des itinéraires entre les 14 régions du Sénégal en utilisant différents algorithmes.

## Fonctionnalités

- **Carte interactive** - Visualisez les 14 régions avec leurs capitales
- **3 algorithmes de routage**
  - **Dijkstra** - Plus court chemin
  - **Bellman-Ford** - Alternative à Dijkstra
  - **TSP** - Circuit optimal pour visiter toutes les régions
- **Comparaison** - Route Nationale (80 km/h) vs Autoroute (100 km/h)
- **Mode hors ligne** - Fonctionne sans connexion internet (PWA)
- **Itinéraires réels** - Routes avec virages et checkpoints

## Comment l'utiliser

1. Sélectionnez votre région de départ dans la liste
2. Choisissez votre destination
3. Cliquez sur un bouton d'algorithme :
   - **Dijkstra** : Calcule le chemin le plus court
   - **Bellman-Ford** : Même résultat, méthode différente
   - **TSP** : Crée un circuit touristiquevisit toutes les régions
4. Consultez le résultat sur la carte et dans le panneau latéral

Cliquez sur les marqueurs de la carte pour voir les informations de chaque région (conseils, hébergement, etc.).

## Installation

```bash
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal_Trip_Planner
pip install -r requirements.txt
python3 app.py
```

Puis ouvrez **http://127.0.0.1:5000** dans votre navigateur.

## Les 14 régions du Sénégal

| # | Région | Capitale |
|---|--------|----------|
| 1 | Dakar | Dakar |
| 2 | Thiès | Thiès |
| 3 | Diourbel | Diourbel |
| 4 | Kaolack | Kaolack |
| 5 | Saint-Louis | Saint-Louis |
| 6 | Louga | Louga |
| 7 | Kolda | Kolda |
| 8 | Ziguinchor | Ziguinchor |
| 9 | Sédhiou | Sédhiou |
| 10 | Kaffrine | Kaffrine |
| 11 | Kédougou | Kédougou |
| 12 | Matam | Matam |
| 13 | Tambacounda | Tambacounda |
| 14 | Fatick | Fatick |

## À propos

Projet académique realizado dans le cadre d'un cours sur les algorithmes de graphe.

- **Backend** : Python (Flask)
- **Frontend** : HTML, CSS, JavaScript
- **Carte** : Leaflet + OpenStreetMap
- **Routage** : OSRM pour les itinéraires réels
