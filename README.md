# Projet : Senegal Trip Planner

## 1. Introduction et Contexte

**Senegal Trip Planner** est une application web de planification de voyage au Sénégal, développée dans le cadre d'un projet académique. Elle permet à un utilisateur (touriste ou voyageur) de quitter Dakar pour traverser les 14 régions du Sénégal, tout en affichant la carte du Sénégal.

### 1.1 Problématique

Le voyageur doit se déplacer d'un point à un autre à travers le Sénégal. Comment optimiser ses déplacements ?

### 1.2 Objectif de l'Application

Créer une application en réseau basée sur l'algorithme de Dijkstra, permettant à un utilisateur (touriste ou voyageur) de quitter Dakar pour traverser les 14 régions du Sénégal, tout en affichant la carte du Sénégal.

---

## 2. Spécifications Fonctionnelles

### 2.1 Carte Interactive (Leaflet)

- Affichage des 14 régions sur une carte OpenStreetMap
- Chaque région est marquée avec sa capitale
- Possibilité de cliquer sur les régions pour voir les informations associées

### 2.2 Les 14 Régions du Sénégal

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

### 2.3 Algorithmes de Parcours

#### 2.3.1 Dijkstra

- Calcul du chemin le plus court vers n'importe quelle région
- Utilisation d'un graphe pondéré par distances

#### 2.3.2 Bellman-Ford

- Alternative à Dijkstra
- Même résultat pour des distances positives

#### 2.3.3 TSP (Voyageur de Commerce)

- Calcul d'un itinéraire optimal pour visiter toutes les régions sans repasser deux fois
- Approche en deux phases : Nearest Neighbor + 2-opt

### 2.4 Guidage / Planification

- **Point de départ par défaut** : Dakar
- Génération de l'itinéraire complet
- Affichage du temps estimé et de la distance totale
- Comparaison Route Nationale vs Autoroute

### 2.5 Types de Routes

| Type | Vitesse moyenne |
|------|----------------|
| Route Nationale | 80 km/h |
| Autoroute | 100 km/h |

### 2.6 Informations Utiles

Pour chaque région :
- Informations touristiques ou culturelles
- Conseils de voyage
- Consignes de sécurité
- Informations d'hébergement

---

## 3. Architecture Technique

### 3.1 Stack Technologique

```
┌─────────────────────────────────────────────┐
│           FRONTEND                        │
│  HTML5 + CSS3 + JavaScript              │
│  Leaflet.js (Carte)                   │
│  OpenStreetMap (Tuiles)              │
└──────────────────┬──────────────────────┘
                   │ HTTP
                   ▼
┌─────────────────────────────────────────────┐
│           BACKEND (Flask - Python)         │
│  ┌─────────────────────────────────┐    │
│  │  API REST                       │    │
│  │ - /api/regions                │    │
│  │ - /api/dijkstra               │    │
│  │ - /api/bellman               │    │
│  │ - /api/tsp                  │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │  Algorithmes                   │    │
│  │ - Dijkstra                    │    │
│  │ - Bellman-Ford               │    │
│  │ - TSP (NN + 2-opt)         │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

### 3.2 Structure du Projet

```
Senegal_Trip_Planner/
├── app.py                 # Application Flask (Backend)
├── README.md              # Documentation
├── requirements.txt       # Dépendances Python
└── templates/
    └── index.html        # Interface utilisateur (Frontend)
```

---

## 4. Installation et Lancement

### 4.1 Prérequis

- Python 3.8+
- pip (gestionnaire de paquets)

### 4.2 Installation

```bash
# Cloner le projet
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal-Trip-Planner

# Installer les dépendances
pip install -r requirements.txt
```

### 4.3 Lancement

```bash
python3 app.py
```

L'application est accessible sur : **http://127.0.0.1:5000**

---

## 5. Guide Utilisation

### 5.1 Interface

L'interface se compose de :

1. **Carte** - Affichage des 14 régions avec Leaflet
2. **Contrôles** - Sélection départ/destination et boutons算法
3. **Résultats** - Itinéraire calculé avec distance et durée

### 5.2 Calcul d'Itinéraire

1. Sélectionner la région de départ
2. Sélectionner la région de destination
3. Cliquer sur **"Dijkstra"**, **"Bellman-Ford"** ou **"TSP"**
4. Consulter les résultats sur la carte et dans le panneau latéral

### 5.3 Informations des Régions

Cliquer sur un marqueur de la carte pour voir :
- Nom de la capitale
- Description de la région
- Conseils de voyage
- Informations d'hébergement

---

## 6. Documentation Technique

### 6.1 API Endpoints

| Endpoint | Méthode | Parameters | Description |
|----------|--------|-----------|------------|
| `/` | GET | - | Page principale |
| `/api/regions` | GET | - | Liste des 14 régions |
| `/api/dijkstra` | GET | start, destination | Plus court chemin |
| `/api/bellman` | GET | start, destination | Plus court chemin |
| `/api/tsp` | GET | start | Circuit touristique |

### 6.2 Exemples API

```bash
# Liste des régions
curl http://localhost:5000/api/regions

# Itinéraire Dakar → Ziguinchor
curl "http://localhost:5000/api/dijkstra?start=dakar&destination=ziguinchor"

# Circuit depuis Dakar
curl "http://localhost:5000/api/tsp?start=dakar"
```

---

## 7. Implémentation des Algorithmes

### 7.1 Dijkstra

```python
def dijkstra(start, end, matrix):
    """
    Algorithme de Dijkstra - Plus court chemin
    
    Principe:
    1. Initialiser distances à ∞, sauf départ = 0
    2. Explorer les nóudd par distance croissante
    3. Mettre à jour les distances des voisins
    4. Reconstruire le chemin
    
    Complexité: O(V²) où V = 14
    """
    dist = {r: 9999 for r in all_regions}
    prev = {r: None for r in all_regions}
    dist[start] = 0
    unvisited = set(all_regions)
    
    while unvisited:
        current = min(unvisited, key=lambda x: dist[x])
        if current == end or dist[current] >= 9999:
            break
        unvisited.remove(current)
        
        for neighbor in all_regions:
            if neighbor in unvisited and 0 < matrix[current][neighbor] < 9999:
                new_dist = dist[current] + matrix[current][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current
    
    # Reconstruire le chemin
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = prev[current]
    
    return path, round(dist[end])
```

### 7.2 TSP (Nearest Neighbor + 2-opt)

```python
def tsp_nearest_neighbor(matrix, start):
    """
    Phase 1: Construction du circuit
    Complexité: O(n²)
    """
    visited = {start}
    path = [start]
    current = start
    unvisited = set(all_regions) - {start}
    
    while unvisited:
        candidates = [(x, matrix[current][x]) for x in unvisited 
                   if 0 < matrix[current][x] < 9999]
        if not candidates:
            break
        nearest = min(candidates, key=lambda x: x[1])[0]
        path.append(nearest)
        visited.add(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    if 0 < matrix[current][start] < 9999:
        path.append(start)
    return path


def two_opt_optimize(path, matrix):
    """
    Phase 2: Optimisation locale
    Complexité: O(n² × itérations)
    """
    best_path = path[:-1].copy()
    improved = True
    
    while improved:
        improved = False
        best_distance = sum(matrix[best_path[i]][best_path[i+1]] 
                        for i in range(len(best_path)-1))
        
        for i in range(1, len(best_path) - 1):
            for j in range(i + 1, len(best_path)):
                new_path = best_path[:i] + best_path[i:j+1][::-1] + best_path[j+1:]
                new_distance = sum(matrix[new_path[i]][new_path[i+1]] 
                                for i in range(len(new_path)-1))
                
                if new_distance < best_distance:
                    best_path = new_path
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break
    
    best_path.append(best_path[0])
    return best_path
```

---

## 8. Conclusion

Senegal Trip Planner est une application complète qui répond aux objectifs du projet :

✓ Affichage des 14 régions sur une carte interactive  
✓ Algorithme de Dijkstra pour le plus court chemin  
✓ Algorithme TSP pour le circuit touristique  
✓ Comparaison Route Nationale vs Autoroute  
✓ Informations utiles pour chaque région  
✓ Interface adaptée aux mobiles  

Ce projet démontre la maîtrise des algorithmes de graphes et du développement web avec Python/Flask.

---

## 9. Auteurs et Informations

- **Projet** : Senegal Trip Planner
- **Auteur** : Mamadou Thiam
- **Technologie** : Python (Flask) + HTML/JS (Leaflet)
- **Date** : Avril 2026

---

*Document généré dans le cadre du projet académique*