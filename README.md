# Senegal Trip Planner 🧭

Application web de planification de voyage au Sénégal - Parcourt les 14 régions du Sénégal en optimisant vos trajets.

## Fonctionnalités

- **Carte interactive** - Visualisez les 14 régions du Sénégal
- **3 algorithmes** - Dijkstra, Bellman-Ford et TSP (Voyageur de Commerce)
- **Comparaison** - Route Nationale vs Autoroute
- **Mode hors ligne** - Fonctionne sans internet (PWA)
- **Itinéraires réels** - Routes avec virages (pas de lignes droites)

## Comment l'utiliser

1. Sélectionnez votre région de départ
2. Choisissez votre destination
3. Cliquez sur un algorithme pour calculer l'itinéraire
4. Consultez le résultat sur la carte et dans le panneau latéral

## Installation

```bash
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal_Trip_Planner
pip install -r requirements.txt
python3 app.py
```

L'application est accessible sur : **http://127.0.0.1:5000**

## Les 14 régions

| Région | Capitale |
|--------|----------|
| Dakar | Dakar |
| Thiès | Thiès |
| Diourbel | Diourbel |
| Kaolack | Kaolack |
| Saint-Louis | Saint-Louis |
| Louga | Louga |
| Kolda | Kolda |
| Ziguinchor | Ziguinchor |
| Sédhiou | Sédhiou |
| Kaffrine | Kaffrine |
| Kédougou | Kédougou |
| Matam | Matam |
| Tambacounda | Tambacounda |
| Fatick | Fatick |

## À propos

Projet académique - Algorithmes de routage  
Développé avec Python (Flask) et JavaScript (Leaflet)
