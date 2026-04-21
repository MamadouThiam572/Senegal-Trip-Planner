# Senegal Trip Planner 🧭

## Présentation du Projet

**Senegal Trip Planner** est une application web de planification de voyage au Sénégal. Elle permet de calculer des itinéraires optimaux entre les 14 régions du Sénégal en utilisant des algorithmes de graphe.

### Problématique

Comment optimiser les déplacements d'un voyageur à travers les 14 régions du Sénégal ?

### Objectifs

- Calculer le plus court chemin entre deux régions
- Comparer différents algorithmes (Dijkstra, Bellman-Ford, TSP)
- Afficher les itinéraires sur une carte interactive
- Proposer un mode hors ligne

---

## Fonctionnalités

### 1. Carte Interactive
- Affichage des 14 régions sur une carte OpenStreetMap
- Marqueurs personnalisés pour chaque capitale régionale
- Popup avec informations (conseils, hébergement, tourisme)

### 2. Algorithmes de Routage

| Algorithme | Description |
|------------|-------------|
| **Dijkstra** | Plus court chemin - complexité O(V²) |
| **Bellman-Ford** | Alternative à Dijkstra |
| **TSP** | Voyageur de Commerce - Nearest Neighbor + 2-opt |

### 3. Types de Routes
- **Route Nationale** : vitesse moyenne 80 km/h
- **Autoroute** : vitesse moyenne 100 km/h

### 4. Mode Hors Ligne (PWA)
- Service Worker pour le cache
- Itinéraires pré-enregistrés
- Fonctionne sans internet

### 5. Itinéraires Réels
- Utilisation d'OSRM pour les routes réelles
- Pas de lignes droites -真实的道路

---

## Architecture Technique

```
┌─────────────────────────────────────┐
│         FRONTEND                    │
│  HTML5 + CSS3 + JavaScript          │
│  Leaflet.js (Carte)                │
│  Service Worker (Offline)            │
└──────────────┬──────────────────────┘
               │ HTTP
               ▼
┌─────────────────────────────────────┐
│       BACKEND (Flask - Python)     │
│  API REST                           │
│  Algorithmes de graphe              │
└─────────────────────────────────────┘
```

### Structure des fichiers

```
Senegal_Trip_Planner/
├── app.py              # Backend Flask + Algorithmes
├── requirements.txt    # Dépendances Python
├── templates/
│   └── index.html     # Frontend (HTML/CSS/JS)
└── static/
    ├── sw.js          # Service Worker
    ├── offline_engine.js
    └── offline_routes.js
```

---

## Les 14 Régions du Sénégal

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

---

## Détails des Algorithmes

### Dijkstra
- **Principe** : Explorer les nœuds par distance croissante
- **Complexité** : O(V²) où V = 14 régions
- **Résultat** : Plus court chemin unique

### Bellman-Ford
- **Principe** : Relaxation progressive des arêtes
- **Complexité** : O(V×E)
- **Avantage** : Détecte les cycles négatifs (non applicable ici)

### TSP (Voyageur de Commerce)
- **Phase 1** : Nearest Neighbor - construction rapide
- **Phase 2** : 2-opt - optimisation locale
- **Résultat** : Circuit optimal visitant toutes les régions

---

## Installation et Lancement

```bash
# Cloner le projet
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal_Trip_Planner

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python3 app.py
```

L'application est accessible sur : **http://127.0.0.1:5000**

---

## Utilisation

1. **Sélectionner départ** - Choisir une région de départ
2. **Sélectionner destination** - Choisir la destination
3. **Choisir algorithme** - Cliquer sur Dijkstra, Bellman-Ford ou TSP
4. **Voir résultat** - Itinéraire affiché sur la carte et dans le panneau

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/regions` | Liste des 14 régions |
| `/api/dijkstra?start=X&destination=Y` | Plus court chemin |
| `/api/bellman?start=X&destination=Y` | Plus court chemin |
| `/api/tsp?start=X` | Circuit touristique |

---

## Compétences Démontrées

✓ Développement web (Flask, HTML/CSS/JS)  
✓ Algorithmes de graphes (Dijkstra, Bellman-Ford, TSP)  
✓ Programmation Python  
✓ Cartographie (Leaflet, OpenStreetMap)  
✓ Mode hors ligne (PWA, Service Worker)  
✓ Intégration API externe (OSRM)  

---

## À propos

- **Projet** : Senegal Trip Planner
- **Auteur** : Mamadou Thiam
- **Date** : Avril 2026
- **Technologies** : Python (Flask), JavaScript (Leaflet), HTML/CSS
