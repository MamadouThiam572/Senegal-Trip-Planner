# Senegal Trip Planner

## Cahier des Charges - Application de Planification de Voyage au Sénégal

---

## 1. Introduction et Contexte du Projet

### 1.1 Préambule

Le présent document constitue le cahier des charges de l'application **Senegal Trip Planner**, un projet développé dans le cadre d'un travail académique. Cette application web a pour vocation de permettre aux voyageurs de planifier leurs déplacements à travers les 14 régions administratives du Sénégal, en offrant des fonctionnalités de calcul d'itinéraires optimaux et de circuits touristiques.

### 1.2 Contexte Géographique

Le Sénégal est un pays de l'Afrique de l'Ouest, limité à l'ouest par l'océan Atlantique, couvrant une superficie d'environ 196 722 km². Le territoire sénégalais est subdivisé en 14 régions administratives, chacune ayant sa capitale régionale respective. Ces régions sont réparties selon un axe nord-sud, avec une diversité géographique allant du Sahel au nord à la Casamance au sud.

La connaissance des distances entre ces régions et l'identification des meilleurs itinéraires constituent des informations précieuses pour tout voyageur souhaitant explorer le pays, que ce soit pour des raisons touristiques, commerciales ou personnelles.

### 1.3 Problématique

Lors de la planification d'un voyage au Sénégal, plusieurs questions se posent naturellement :
- Quelle est la distance entre deux régions données ?
- Quel est l'itinéraire le plus court ?
- Comment optimiser un circuit touristique visita toutes les régions ?
- Quelles sont les routes nationales versus les autoroutes ?

Cette application vise à répondre à ces questions de manière interactive et visuelle.

### 1.4 Objectifs du Projet

**Objectif principal :**
Développer une application web permettant le calcul d'itinéraires optimaux entre les 14 régions du Sénégal.

**Objectifs spécifiques :**
1. Proposer deux types de routes : nationale et autoroute
2. Implémenter l'algorithme de Dijkstra pour le plus court chemin
3. Implémenter l'algorithme de Bellman-Ford comme alternatif
4. Résoudre le problème du voyageur de commerce (TSP) pour les circuits touristiques
5. Fournir une interface cartographique interactive
6. Afficher des informations pratiques pour chaque région

---

## 2. Spécifications Fonctionnelles

### 2.1 Description des Régions

L'application gère les 14 régions administratives du Sénégal, chacune caractérisée par :

| # | Région | Capitale | Latitude | Longitude | Description |
|---|--------|----------|----------|-----------|-------------|
| 1 | Dakar | Dakar | 14.7167 | -17.4671 | Capitale nationale, centre économique |
| 2 | Thiès | Thiès | 14.7941 | -16.9639 | Deuxième ville, pôle artisanal |
| 3 | Diourbel | Diourbel | 14.7167 | -16.2333 | Capitale religieuse Mboss |
| 4 | Kaolack | Kaolack | 14.1500 | -16.0833 | Centre économique arachidier |
| 5 | Saint-Louis | Saint-Louis | 16.0333 | -16.5000 | Ancienne capitale coloniale |
| 6 | Louga | Louga | 15.6333 | -15.6333 | Région sahélienne |
| 7 | Kolda | Kolda | 12.8833 | -14.9500 | Région sud verdoyante |
| 8 | Ziguinchor | Ziguinchor | 12.5833 | -16.2667 | Capitale du sud |
| 9 | Sédhiou | Sédhiou | 12.7167 | -15.1833 | Zone Sine-Saloum |
| 10 | Kaffrine | Kaffrine | 14.1000 | -15.4167 | Cœur pays Serer |
| 11 | Kédougou | Kédougou | 12.5667 | -12.1833 | Parc Niokolo-Koba |
| 12 | Matam | Matam | 15.6667 | -13.2667 | Vallée du Niger |
| 13 | Tambacounda | Tambacounda | 13.7667 | -13.6667 | Plus grande région |
| 14 | Fatick | Fatick | 14.3333 | -16.0833 | Delta Sine-Saloum |

### 2.2 Données Associées à Chaque Région

Chaque région contient les informations suivantes :

- **name** : Nom de la région
- **capital** : Nom de la capitale régionale
- **lat/lng** : Coordonnées géographiques (latitude/longitude)
- **info** : Description généraliste de la région
- **tips** : Conseils pratiques pour les voyageurs
- **security** : Consignes de sécurité
- **hebergement** : Informations d'hébergement et budget
- **tourisme** : Sites et activités touristiques

### 2.3 Types de Routes

L'application distingue deux catégories de routes :

**Route Nationale (RN)**
- Routes classiques empruntees
- Vitesse moyenne estimée : 80 km/h
- Distance généralement plus longue
- Traverse les villages et villes

**Autoroute**
- Routes rapides etayed
- Vitesse moyenne estimée : 100 km/h
- Distance généralement plus courte
- Moins de points de passage

### 2.4 Fonctionnalités Métier

#### 2.4.1 Calcul d'Itinéraire (Dijkstra)

Cette fonctionnalité permet de trouver le chemin le plus court entre une région de départ et une région d'arrivée.

**Entrees :**
- Région de départ (par défaut : Dakar)
- Région de destination

**Sorties :**
- Chemin optimal (liste des régions)
- Distance totale en km
- Durée estimée du trajet
- Comparaison route nationale vs autoroute

#### 2.4.2 Calcul d'Itinéraire (Bellman-Ford)

Alternative à Dijkstra, cet algorithme permet également de trouver le plus court chemin. Bien que plus lent (O(V*E) vs O(V²)), il支持 les poids négatifs hypothétiques.

#### 2.4.3 Circuit Touristique (TSP)

Cette fonctionnalité génère un parcours optimal visita toutes les régions du Sénégal, en partance d'une région sélectionnée.

**Approche en deux phases :**
1. **Nearest Neighbor** : Construction d'une solution initiale
2. **2-opt** : Optimisation locale itérative

**Entrees :**
- Région de départ

**Sorties :**
- Ordre de visita des 14 régions
- Distance totale du circuit
- Durée estimée

### 2.5 Interface Utilisateur

L'interface web propose :

1. **Carte interactive** - Affichage des 14 régions avec Leaflet/OpenStreetMap
2. **Panneau de contrôle** - Sélection départ/destination et algorithmes
3. **Panneau de résultats** - Affichage des itinéraires calculés
4. **Panneau d'information** - Détails sur les régions
5. **Légende** - Choix d'affichage national/autoroute/les deux

---

## 3. Spécifications Techniques

### 3.1 Architecture Applicative

L'application suit une architecture client-serveur simple :

```
┌─────────────────────────────────────┐
│           Navigateur Web            │
│  ┌─────────────────────────────┐     │
│  │    Interface HTML/JS      │     │
│  │ - Carte Leaflet           │     │
│  │ - Contrôles utilisateur  │     │
│  │ - Affichage résultats    │     │
│  └─────────────────────────────┘     │
└──────────────┬──────────────────────┘
               │ HTTP
               ▼
┌─────────────────────────────────────┐
│         Serveur Flask               │
│  ┌─────────────────────────────┐     │
│  │   API REST                  │     │
│  │ - /api/regions             │     │
│  │ - /api/dijkstra            │     │
│  │ - /api/bellman            │     │
│  │ - /api/tsp                │     │
│  └─────────────────────────────┘     │
│  ┌─────────────────────────────┐     │
│  │  Algorithmes               │     │
│  │ - Dijkstra                │     │
│  │ - Bellman-Ford            │     │
│  │ - TSP (NN + 2-opt)       │     │
│  └─────────────────────────────┘     │
└─────────────────────────────────────┘
```

### 3.2 Structure des Données

#### 3.2.1 Matrices de Distances

L'application utilise deux matrices de distances :

- **distances_national** : Distances via routes nationales
- **distances_autoroute** : Distances via autoroutes

Chaque matrice est un dictionnaire de dictionnaires :
```python
{
    "dakar": {"thies": 46, "fatick": 148, "kaolack": 188},
    "thies": {"dakar": 46, "diourbel": 77, ...},
    ...
}
```

#### 3.2.2 Matrices d'Adjacence

Pour les algorithmes, ces données sont converties en matrices d'adjacence complètes (14x14) où les cellules manquantes sont calculées via la formule haversine.

### 3.3 Implémentation des Algorithmes

#### 3.3.1 Algorithme de Dijkstra

**Principe :**
1. Initialiser les distances à l'infini, sauf départ = 0
2. Explorer les nœuds par distance croissante
3. Mettre à jour les distances des voisins
4. Reconstruire le chemin via les précurseurs

**Complexité :** O(V²) où V = 14 régions

**Implementation :**
```python
def dijkstra(start, end, matrix):
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

#### 3.3.2 Algorithme TSP (Nearest Neighbor + 2-opt)

**Phase 1 - Nearest Neighbor :**
```python
def tsp_nearest_neighbor(matrix, start):
    visited = {start}
    path = [start]
    current = start
    unvisited = set(all_regions) - {start}
    
    while unvisited:
        candidates = [(x, matrix[current][x]) for x in unvisited if 0 < matrix[current][x] < 9999]
        nearest = min(candidates, key=lambda x: x[1])[0]
        path.append(nearest)
        visited.add(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    path.append(start)  # Retour au point de départ
    return path
```

**Phase 2 - 2-opt :**
```python
def two_opt_optimize(path, matrix, max_iterations=300):
    best_path = path[:-1].copy()
    
    improved = True
    while improved:
        improved = False
        best_distance = calculate_path_distance(best_path, matrix)
        
        for i in range(1, len(best_path) - 1):
            for j in range(i + 1, len(best_path)):
                new_path = best_path[:i] + best_path[i:j+1][::-1] + best_path[j+1:]
                new_distance = calculate_path_distance(new_path, matrix)
                
                if new_distance < best_distance:
                    best_path = new_path
                    best_distance = new_distance
                    improved = True
                    break
    
    best_path.append(best_path[0])
    return best_path
```

### 3.4 Service Web et API

#### 3.4.1 Endpoints Disponibles

| Endpoint | Méthode | Paramètres | R��ponse |
|----------|---------|------------|--------|
| `/` | GET | - | Page HTML principale |
| `/api/regions` | GET | - | JSON de toutes les régions |
| `/api/routes` | GET | - | Données routes hors-ligne |
| `/api/dijkstra` | GET | start, destination | Itinéraire calculé |
| `/api/bellman` | GET | start, destination | Itinéraire calculé |
| `/api/tsp` | GET | start | Circuit touristique |

#### 3.4.2 Format de Réponse API

```json
{
    "national": {
        "path": ["dakar", "thies", "kaolack", "ziguinchor"],
        "distance": 380,
        "time": "4h 45min"
    },
    "autoroute": {
        "path": ["dakar", "thies", "kaolack", "ziguinchor"],
        "distance": 362,
        "time": "3h 37min"
    }
}
```

### 3.5 Technologies Utilisées

**Backend :**
- Python 3
- Flask (framework web)
- math (calculs haversine)

**Frontend :**
- HTML5
- CSS3 (design moderne sombre)
- JavaScript (Leaflet.js)
- Leaflet (cartographie)
- OpenStreetMap (tuiles)

**Outils :**
- Git (gestion de version)
- Python-dotenv (configuration)

---

## 4. Installation et Déploiement

### 4.1 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets)
- Navigateur web moderne

### 4.2 Installation

```bash
# Cloner le dépôt
git clone https://github.com/MamadouThiam572/Senegal-Trip-Planner.git
cd Senegal-Trip-Planner

# Créer un environnement virtuel (optionnel)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

### 4.3 Lancement

```bash
# Démarrer le serveur
python3 app.py
```

L'application sera accessible à l'adresse : **http://127.0.0.1:5000**

### 4.4 Utilisation API en Ligne de Commandes

```bash
# Obtenir toutes les régions
curl http://localhost:5000/api/regions

# Itinéraire de Dakar à Ziguinchor
curl "http://localhost:5000/api/dijkstra?start=dakar&destination=ziguinchor"

# Circuit touristique depuis Thiès
curl "http://localhost:5000/api/tsp?start=thies"
```

---

## 5. Guide Utilisateur

### 5.1 Interface Principale

L'interface se compose de plusieurs éléments :

1. **En-tête** : Titre de l'application
2. **Panneau de contrôle** : Sélection des paramètres
3. **Carte** : Visualisation géographique
4. **Panneau latéral** : Résultats et informations

### 5.2 Utilisation des Fonctionnalités

**Pour calculer un itinéraire :**
1. Sélectionner la région de départ
2. Sélectionner la région de destination
3. Cliquer sur "Dijkstra" ou "Bellman-Ford"
4. Consulter les résultats

**Pour un circuit touristique :**
1. Sélectionner la région de départ
2. Cliquer sur "TSP"
3. visualiser le circuit sur la carte

**Pour afficher les informations d'une région :**
1. Cliquer sur un marqueur de la carte
2. Consulter le popup d'information
3. Ou cliquer sur un élément de la liste des résultats

### 5.3 Options d'Affichage

- **Les deux** : Affiche routes nationales et autoroutes
- **Route Nationale** : Affiche uniquement les routes nationales
- **Autoroute** : Affiche uniquement les autoroutes

---

## 6. Améliorations Futures

### 6.1 Améliorations Prévues

1. **Données temps réel** : Intégration d'API de trafic
2. **Calcul multimodal** : Trains, bus, avions
3. **Points d'intérêt** : Hôtels, restaurants, cliniques
4. **Mode hors-ligne** : Progressive Web App
5. **Suggestions** : IA basée sur les préférences utilisateur

### 6.2 Évolutions Techniques

1. **Base de données** : PostgreSQL pour les données persistantes
2. **Cache** : Redis pour les itinéraires fréquents
3. **API REST étendue** :.endpoints CRUD complets
4. **Frontend framework** : React ou Vue.js

---

## 7. Conclusion

Senegal Trip Planner représente une solution complète pour la planification de voyages au Sénégal. Les fonctionnalités implémentées (Dijkstra, Bellman-Ford, TSP) permettent de répondre aux besoins fondamentaux des voyageurs, tandis que l'interface cartographique offre une visualisation intuitive des itinéraires.

Ce projet démontre la maîtrise des algorithmes de graphes et le développement d'applications web avec Python/Flask.

---

## Annexe A : Matrice des Distances Nationales

| | Dakar | Thiès | Diourbel | Kaolack | St-Louis | Louga | Kolda | Ziguinchor | Sédhiou | Kaffrine | Kédougou | Matam | Tamba | Fatick |
|------|------|--------|----------|---------|--------|------|-----------|---------|---------|----------|-------|-------|-------|
| Dakar | 0 | 46 | - | 188 | - | - | - | - | - | - | - | - | - | 148 |
| Thiès | 46 | 0 | 77 | 116 | 146 | 155 | - | - | - | 90 | - | - | - | 75 |
| Diourbel | - | 77 | 0 | 85 | 120 | 90 | - | - | - | 65 | - | - | - | - |
| Kaolack | 188 | 116 | 85 | 0 | - | - | 185 | 205 | 135 | 58 | - | - | 285 | 65 |
| St-Louis | - | 146 | 120 | 0 | 0 | 85 | - | - | - | - | - | 180 | - | - |
| Louga | - | 155 | 90 | - | 85 | 0 | - | - | - | - | - | 110 | - | - |
| Kolda | - | - | - | 185 | - | - | 0 | 105 | 65 | - | 305 | - | 145 | - |
| Ziguinchor | - | - | - | 205 | - | - | 105 | 0 | 85 | - | - | - | - | - |
| Sédhiou | - | - | - | 135 | - | - | 65 | 85 | 0 | - | - | - | - | 115 |
| Kaffrine | - | 90 | 65 | 58 | - | - | - | - | - | 0 | - | - | 105 | - | 78 |
| Kédougou | - | - | - | - | - | - | 305 | - | - | - | 0 | - | 185 | - |
| Matam | - | - | - | - | 180 | 110 | - | - | - | - | - | 0 | 160 | - |
| Tamba | - | - | - | 285 | - | - | 145 | - | - | 105 | 185 | 160 | 0 | - |
| Fatick | 148 | 75 | - | 65 | - | - | - | - | 115 | 78 | - | - | - | 0 |

*Note : Les cellules vides indiquent qu'il n'y a pas de connexion directe dans la matrice. L'algorithme haversine est utilisé comme fallback.*

---

## Annexe B : Glossaire

| Terme | Définition |
|-------|------------|
| TSP | Traveling Salesman Problem - Problème du voyageur de commerce |
| Dijkstra | Algorithme de plus court chemin à coût positif |
| Bellman-Ford | Algorithme de plus court chemin supportant les coûts négatifs |
| Nearest Neighbor | Algorithme glouton de construction de circuit |
| 2-opt | Algorithme d'optimisation locale par échanges |
| API | Application Programming Interface |
| REST | Representational State Transfer |
| Flask | Framework web Python |
| Leaflet | Bibliothèque JavaScript de cartographie |

---

## 8. Structure du Projet et Explication du Code

### 8.1 Organisation des Fichiers

```
Senegal_Trip_Planner/
├── app.py                 # Application principale (Flask)
├── README.md              # Documentation du projet
├── requirements.txt       # Dépendances Python
└── templates/
    └── index.html        # Interface utilisateur
```

### 8.2 Architecture du Code Python (app.py)

Le fichier `app.py` est le cœur de l'application. Il contient toutes les fonctionnalités server-side.

#### 8.2.1 Structure Globale

```python
# ===========================================
# 1. IMPORTS ET CONFIGURATION
# ===========================================

from flask import Flask, render_template, jsonify, request
import math

app = Flask(__name__)

# ===========================================
# 2. DONNÉES DES RÉGIONS
# ===========================================

regions = {
    "dakar": { ... },
    "thies": { ... },
    # ... 14 régions
}

# Liste des clés pour itération
all_regions = list(regions.keys())

# ===========================================
# 3. MATRICES DE DISTANCES
# ===========================================

distances_national = { ... }   # Routes classiques
distances_autoroute = { ... }  # Routes rapides

# ===========================================
# 4. FONCTIONS UTILITAIRES
# ===========================================

def haversine(lat1, lon1, lat2, lon2):
    """Calcule distance entre deux points géographiques"""

def get_distance(r1, r2, dist_matrix):
    """Récupère distance entre deux régions"""

def build_matrix(distances):
    """Convertit distances en matrice d'adjacence"""

# ===========================================
# 5. ALGORITHMES DE GRAPHES
# ===========================================

def dijkstra(start, end, matrix):
    """Plus court chemin (Dijkstra)"""

def bellman_ford(start, end, matrix):
    """Plus court chemin (Bellman-Ford)"""

def tsp_nearest_neighbor(matrix, start):
    """Construction TSP (Nearest Neighbor)"""

def two_opt_optimize(path, matrix):
    """Optimisation locale TSP (2-opt)"""

def two_phase_tsp(matrix, start):
    """TSP en deux phases"""

# ===========================================
# 6. FONCTIONS API
# ===========================================

@app.route('/')
def index():
    """Page d'accueil"""

@app.route('/api/regions')
def get_regions():
    """API: liste des régions"""

@app.route('/api/dijkstra')
def api_dijkstra():
    """API: calcul Dijkstra"""

@app.route('/api/bellman')
def api_bellman():
    """API: calcul Bellman-Ford"""

@app.route('/api/tsp')
def api_tsp():
    """API: calcul TSP"""

# ===========================================
# 7. POINT D'ENTRÉE
# ===========================================

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 8.3 Détail des Fonctions

#### 8.3.1 Fonctions de Calculs Géographiques

**`haversine(lat1, lon1, lat2, lon2)`**

Calcule la distance orthodromique (vol d'oiseau) entre deux points géographiques sur la sphère terrestre.

```python
def haversine(lat1, lon1, lat2, lon2):
    """
    Calcule la distance en km entre deux points GPS
    utilisant la formule haversine.
    
    Paramètres:
        lat1, lon1: Coordonnées point de départ
        lat2, lon2: Coordonnées point d'arrivée
    
    Retourne:
        Distance en kilomètres
    """
    R = 6371  # Rayon moyen de la Terre (km)
    
    # Conversion en radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    # Formule haversine
    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c
```

**Explication mathématique :**
- La formule haversine donne la distance minimale sur une sphère
- Elle utilise le grand cercle reliant les deux points
- `R = 6371 km` est le rayon moyen terrestre

---

**`get_distance(r1, r2, dist_matrix)`**

Récupère la distance entre deux régions, avec fallback haversine.

```python
def get_distance(r1, r2, dist_matrix):
    """
    Récupère la distance entre deux régions.
    
    Ordre de recherche:
    1. Vérifier si connexion directe existe
    2. Utiliser haversine comme fallback
    3. Retourner 999 si aucune connexion
    """
    # Même région = distance zéro
    if r1 == r2:
        return 0
    
    # Chercher dans la matrice
    if r1 in dist_matrix and r2 in dist_matrix[r1]:
        return dist_matrix[r1][r2]
    if r2 in dist_matrix and r1 in dist_matrix[r2]:
        return dist_matrix[r2][r1]
    
    # Fallback: calcul haversine
    d = haversine(
        regions[r1]['lat'], regions[r1]['lng'],
        regions[r2]['lat'], regions[r2]['lng']
    )
    return d if d > 0 else 999
```

---

**`build_matrix(distances)`**

Construit une matrice d'adjacence complète.

```python
def build_matrix(distances):
    """
    Construit une matrice 14x14 des distances.
    
    Chaque cellule [r1][r2] contient la distance
    entre les régions r1 et r2.
    
    Valeurs spéciales:
    - 0: même région
    - 999: pas de connexion
    """
    matrix = {}
    for r1 in all_regions:
        matrix[r1] = {}
        for r2 in all_regions:
            d = get_distance(r1, r2, distances)
            matrix[r1][r2] = d if d > 0 else 999
    return matrix
```

---

#### 8.3.2 Algorithmes de Plus Court Chemin

**`dijkstra(start, end, matrix)`**

Implémente l'algorithme de Dijkstra pour trouver le plus court chemin.

```python
def dijkstra(start, end, matrix):
    """
    Algorithme de Dijkstra - Plus court chemin
    
    Principe (approche gloutonne):
    1. Initialiser distances à ∞, sauf départ = 0
    2. Tant que des nœuds non visités:
       -Sélectionner le nœud avec distance minimale
       -Mettre à jour les distances des voisins
       -Enregistrer le prédecesseur
    3. Reconstruire le chemin à rebours
    
    Complexité: O(V²) = O(14²) = trivial
    
    Paramètres:
        start: Région de départ
        end: Région d'arrivée
        matrix: Matrice des distances
    
    Retourne:
        (path, distance) - Chemin et distance totale
    """
    # Initialisation
    dist = {r: 9999 for r in all_regions}
    prev = {r: None for r in all_regions}
    dist[start] = 0
    unvisited = set(all_regions)
    
    # Boucle principale
    while unvisited:
        # Sélectionner le nœud non visité avec distance minimale
        current = min(unvisited, key=lambda x: dist[x])
        
        # Arrêt anticipé si destination atteinte
        if current == end or dist[current] >= 9999:
            break
            
        unvisited.remove(current)
        
        # Mise à jour des voisins
        for neighbor in all_regions:
            if neighbor in unvisited and 0 < matrix[current][neighbor] < 9999:
                new_dist = dist[current] + matrix[current][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current
    
    # Reconstruire le chemin (à l'envers)
    path = []
    current = end
    while current and prev[current]:
        path.insert(0, current)  # Insérer au début
        current = prev[current]
    
    # Ajouter le point de départ
    if path and path[0] != start:
        path.insert(0, start)
    
    # Validation
    if not path or path[0] != start:
        return [start], 0
    
    return path, round(dist[end]) if dist[end] < 9999 else 0
```

**Points clés de Dijkstra :**
- **Glouton** : Choisi toujours le nœud le plus proche
- **Optimal** : Garantit le chemin le plus court
- **局限性** : Ne support pas les poids négatifs

---

**`bellman_ford(start, end, matrix)`**

Alternative à Dijkstra, peut gérer les poids négatifs.

```python
def bellman_ford(start, end, matrix):
    """
    Algorithme de Bellman-Ford - Plus court chemin
    
    Différences avec Dijkstra:
    - Supporte les poids négatifs
    - Plus lent: O(V*E)
    - Peut détecter les cycles négatifs
    
    Pour notre cas (distances positives):
    - Donne les mêmes résultats que Dijkstra
    - Plus lisible pour compréhension
    """
    # Initialisation
    dist = {r: float('inf') for r in all_regions}
    prev = {r: None for r in all_regions}
    dist[start] = 0
    
    # Relaxation (V-1) fois
    for _ in range(len(all_regions) - 1):
        for u in all_regions:
            for v in all_regions:
                if matrix[u][v] < 9999:
                    if dist[u] + matrix[u][v] < dist[v]:
                        dist[v] = dist[u] + matrix[u][v]
                        prev[v] = u
    
    # Reconstruire le chemin
    path = []
    current = end
    while current and prev[current]:
        path.insert(0, current)
        current = prev[current]
    
    if path and path[0] != start:
        path.insert(0, start)
    
    if not path or path[0] != start:
        return [start], 0
    
    return path, round(dist[end]) if dist[end] < float('inf') else 0
```

---

#### 8.3.3 Algorithmes TSP (Problème du Voyageur de Commerce)

**`tsp_nearest_neighbor(matrix, start)`**

Phase 1: Construction rapide d'un circuit.

```python
def tsp_nearest_neighbor(matrix, start):
    """
    Nearest Neighbor - Construction TSP
    
    Principe:
    1. Commencer au point de départ
    2. À chaque étape, aller à la région non visitée la plus proche
    3. Répéter jusqu'à tout visiter
    4. Retour au point de départ
    
    Complexité: O(n²)
    
    Avantage: Rapide
    Inconvénient: Pas toujours optimal
    """
    visited = {start}
    path = [start]
    current = start
    unvisited = set(all_regions) - {start}
    
    while unvisited:
        # Trouver les candidats valides
        candidates = [
            (x, matrix[current][x]) 
            for x in unvisited 
            if 0 < matrix[current][x] < 9999
        ]
        
        # Fallback si pas de connexion directe
        if not candidates:
            candidates = [
                (x, matrix[x][current]) 
                for x in unvisited 
                if 0 < matrix[x][current] < 9999
            ]
        
        if not candidates:
            break
            
        # Choisir le plus proche
        nearest = min(candidates, key=lambda x: x[1])[0]
        
        path.append(nearest)
        visited.add(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    # Retour au point de départ
    if 0 < matrix[current][start] < 9999:
        path.append(start)
    
    return path
```

**Exemple d'exécution :**
```
Start: Dakar
1. Dakar → Thiès (46 km plus proche)
2. Thiès → Fatick (75 km plus proche)
3. Fatick → Kaolack (65 km plus proche)
...
14. Retour à Dakar
```

---

**`two_opt_optimize(path, matrix)`**

Phase 2: Amélioration locale itérative.

```python
def two_opt_optimize(path, matrix, max_iterations=300):
    """
    2-opt - Optimisation locale
    
    Principe:
    1. Prendre deux arêtes du circuit
    2. Les inverser (swap)
    3. Si amélioration → garder
    4. Répéter jusqu'à stabilisation
    
    Échange effectué:
    A---B   devient   A---C
    |    |            |    |
    D---C              D---B
    
    Complexité: O(n² × itérations)
    """
    if len(path) < 4:
        return path
    
    improved = True
    iteration = 0
    best_path = path[:-1].copy()  # Sans le retour final
    
    while improved and iteration < max_iterations:
        improved = False
        iteration += 1
        best_distance = calculate_path_distance(best_path, matrix)
        
        # Tester tous les échanges possibles
        for i in range(1, len(best_path) - 1):
            for j in range(i + 1, len(best_path)):
                # Créer nouveau chemin avec inversion
                new_path = (
                    best_path[:i] + 
                    best_path[i:j+1][::-1] + 
                    best_path[j+1:]
                )
                new_distance = calculate_path_distance(new_path, matrix)
                
                if new_distance < best_distance:
                    best_path = new_path
                    best_distance = new_distance
                    improved = True
                    break  # Sortir pour recommencer
            if improved:
                break
    
    best_path.append(best_path[0])  # Retour au départ
    return best_path
```

**Visualisation 2-opt :**
```
Avant:     Dakar → Thiès → Kaolack → Ziguinchor → Kolda → Dakar
                   ↓ (échanger Kaolack et Kolda)
Après:    Dakar → Thiès → Kolda → Ziguinchor → Kaolack → Dakar
```

---

**`two_phase_tsp(matrix, start)`**

Combine les deux phases.

```python
def two_phase_tsp(matrix, start):
    """
    TSP en deux phases
    
    Phase 1: Nearest Neighbor (solution initiale rapide)
    Phase 2: 2-opt (optimisation)
    
    Résultat:
    - Solution initiale sous-optimale
    - Améliorée localement jusqu'au maximum local
    """
    # Phase 1: Constructeur
    initial_path = tsp_nearest_neighbor(matrix, start)
    
    # Phase 2: Optimisation
    optimized_path = two_opt_optimize(initial_path, matrix)
    total_distance = calculate_path_distance(optimized_path, matrix)
    
    return optimized_path, round(total_distance)
```

---

#### 8.3.4 Routes API Flask

**Architecture REST:**

```python
@app.route('/')
def index():
    """Affiche la page HTML principale"""
    return render_template('index.html', regions=regions)

@app.route('/api/regions')
def get_regions():
    """Retourne toutes les régions en JSON"""
    return jsonify(regions)

@app.route('/api/dijkstra')
def api_dijkstra():
    """
    API Dijkstra - Paramètres GET:
    - start: Région de départ (défaut: dakar)
    - destination: Région d'arrivée (obligatoire)
    
    Retourne: { national: {...}, autoroute: {...} }
    """
    destination = request.args.get('destination')
    start = request.args.get('start', 'dakar')
    
    # Validation
    if not destination or start not in all_regions or destination not in all_regions:
        return jsonify({"error": "Paramètres invalides"}), 400
    
    # Calculs
    path_national, dist_national = dijkstra(start, destination, road_matrix_national)
    path_autoroute, dist_autoroute = dijkstra(start, destination, road_matrix_autoroute)
    
    # Formatage réponse
    return jsonify({
        "national": {
            "path": path_national,
            "distance": dist_national,
            "time": format_time(dist_national / 80)  # 80 km/h
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / 100)  # 100 km/h
        }
    })
```

---

### 8.4 Structure du Frontend (index.html)

#### 8.4.1 Organisation HTML

```html
<!-- ========================================= -->
<!-- EN-TÊTE -->
<!-- ========================================= -->
<head>
    <meta charset="UTF-8">
    <title>Senegal Trip Planner</title>
    
    <!-- Feuilles de style -->
    <link rel="stylesheet" href="leaflet.css">
    <link href="fonts.googleapis.com...">
    
    <!-- CSS personnalisé -->
    <style>
        /* Variables CSS */
        :root { --bg-dark: #1a1a2e; ... }
        
        /* Styles génériques */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        /* Layout */
        .container { max-width: 1400px; margin: 0 auto; }
        .main-content { display: grid; grid-template-columns: 1fr 350px; }
    </style>
</head>

<!-- ========================================= -->
<!-- CORPS -->
<!-- ========================================= -->
<body>
    <div class="container">
        <!-- En-tête -->
        <header>
            <h1>Senegal Trip Planner</h1>
            <p>Planificateur d'itinéraire - 14 régions</p>
        </header>
        
        <!-- Contrôles -->
        <div class="controls">
            <select id="startSelect"></select>
            <select id="destinationSelect"></select>
            <button onclick="calculateDijkstra()">Dijkstra</button>
            <button onclick="calculateBellman()">Bellman-Ford</button>
            <button onclick="calculateTSP()">TSP</button>
        </div>
        
        <!-- Carte -->
        <div class="map-container">
            <div id="map"></div>
        </div>
        
        <!-- Résultats -->
        <div class="results">
            <div class="route-section national">...</div>
            <div class="route-section autoroute">...</div>
        </div>
    </div>
    
    <!-- Scripts -->
    <script src="leaflet.js"></script>
    <script>
        // =========================================
        // 1. INITIALISATION
        // =========================================
        let map, markers = {}, routeLayers = {}, regions = {};
        
        async function initMap() {
            map = L.map('map').setView([14.4974, -14.4524], 7);
            L.tileLayer('https://{s}.tile.openstreetmap.org/...').addTo(map);
            
            // Charger les régions
            const res = await fetch('/api/regions');
            regions = await res.json();
            
            // Créer les marqueurs
            Object.keys(regions).forEach(key => {
                const r = regions[key];
                const popupContent = `<div>...${r.name}...</div>`;
                markers[key] = L.marker([r.lat, r.lng])
                    .addTo(map)
                    .bindPopup(popupContent);
            });
        }
        
        // =========================================
        // 2. CALCULS API
        // =========================================
        async function calculateDijkstra() {
            const start = document.getElementById('startSelect').value;
            const dest = document.getElementById('destinationSelect').value;
            
            const res = await fetch(`/api/dijkstra?start=${start}&destination=${dest}`);
            const data = await res.json();
            
            displayResults(data);
        }
        
        // =========================================
        // 3. AFFICHAGE CARTE
        // =========================================
        async function drawSingleRoute(path, color, key) {
            // Tracé de la route sur la carte
            const coordinates = path.map(k => [regions[k].lat, regions[k].lng]);
            routeLayers[key] = L.polyline(coordinates, {
                color: color,
                weight: 4,
                opacity: 0.8
            }).addTo(map);
        }
    </script>
</body>
```

#### 8.4.2 Flux de Données Frontend

```
┌─────────────────────────────────────────────────────────────┐
│                  INTERFACE UTILISATEUR                      │
│                                                          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │ startSelect │    │ destSelect │    │ Buttons   │ │
│  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘ │
│        │                  │                  │          │
│        ▼                  ▼                  ▼          │
│  ┌─────────────────────────────────────┐                │
│  │      calculateDijkstra()              │                │
│  │   (JavaScript)                    │                │
│  └──────────────┬──────────────────┘                │
└────────────────┼─────────────��─��──────────────────────────┘
                   │ fetch()
                   ▼
┌────────────────────────────────────────────┐
│         SERVEUR FLASK                    │
│                                     │
│  /api/dijkstra?start=X&dest=Y        │
│           │                         │
│           ▼                       │
│  ┌─────────────────────────┐       │
│  │    dijkstra()          │       │
│  │    (Python)           │       │
│  └──────────┬────────────┘       │
│             │                   │
│             ▼                   │
│  ┌─────────────────────┐         │
│  │ Résultats JSON     │         │
│  │ {path, dist, time}│         │
│  └──────────┬────────┘         │
└─────────────┼────────────────────┘
             │ response JSON
             ▼
┌─────────────────────────────────────────┐
│         AFFICHAGE RÉSULTATS              │
│                                         │
│  • displayResults(data)                   │
│  • drawSingleRoute(path, color)           │
│  • map.fitBounds()                      │
│  • Popups informations                 │
└────────────────────────────────────────┘
```

---

### 8.5 Flux Complet d'une Requête

#### Exemple: Itinéraire Dakar → Ziguinchor

```
1. UTILISATEUR
   └── Sélectionne: Dakar (depart), Ziguinchor (destination)
   └── Clique sur: "Dijkstra"

2. FIREFOX/CHROME
   └── fetch('/api/dijkstra?start=dakar&destination=ziguinchor')
   └── Requête HTTP GET

3. SERVEUR FLASK (app.py)
   ├── Route '/api/dijkstra' appelée
   ├── request.args.get('start') → 'dakar'
   ├── request.args.get('destination') → 'ziguinchor'
   ├── Validation: 'dakar' et 'ziguinchor' dans all_regions ✓
   │
   ├── dijkstra('dakar', 'ziguinchor', road_matrix_national)
   │   ├── dist initiales: {dakar: 0, others: 9999}
   │   ├── Itération 1: Dakar → thies (46 km)
   │   ├── Itération 2: thies → kaolack (116+46=162)
   │   ├── Itération 3: kaolack → ziguinchor (205+162=367)
   │   └── Chemin: ['dakar', 'thies', 'kaolack', 'ziguinchor']
   │
   ├── dijkstra('dakar', 'ziguinchor', road_matrix_autoroute)
   │   └── Chemin: ['dakar', 'thies', 'kaolack', 'ziguinchor']
   │
   ├── format_time(367/80) → "4h 35min"
   │
   └── Réponse JSON:
       {
         "national": {
           "path": ["dakar", "thies", "kaolack", "ziguinchor"],
           "distance": 367,
           "time": "4h 35min"
         },
         "autoroute": {
           "path": ["dakar", "thies", "kaolack", "ziguinchor"],
           "distance": 348,
           "time": "3h 29min"
         }
       }

4. FRONTEND
   ├── Réception JSON
   ├── displayResults(data)
   │   ├── Mise à jour des distances et durées
   │   ├── Affichage des listes de régions
   │   └── Affichage popup région destination
   ├── drawRoutes(nationalPath, autoroutePath)
   │   ├── Tracé ligne bleue (national)
   │   └── Tracé ligne orange (autoroute)
   └── map.fitBounds()
       └── Zoom automatique sur l'itinéraire
```

---

### 8.6 Points Clés du Code

| Fonction | Rôle | Complexité |
|----------|------|------------|
| `haversine` | DistanceGPS | O(1) |
| `get_distance` | Distance régions | O(1) |
| `build_matrix` | Matrice adjacence | O(V²) |
| `dijkstra` | Plus court chemin | O(V²) |
| `bellman_ford` | Plus court chemin | O(V×E) |
| `tsp_nearest_neighbor` | Circuit initial | O(n²) |
| `two_opt_optimize` | Optimisation | O(n²×iter) |
| `two_phase_tsp` | Circuit complet | O(n²) |

---

### 8.7 Débogage et Tests

#### Tests manuels

```bash
# Tester une région
curl http://localhost:5000/api/regions | python3 -m json.tool

# Tester Dijkstra
curl "http://localhost:5000/api/dijkstra?start=dakar&destination=ziguinchor"

# Tester l'application entière
python3 app.py
# Puis ouvrir http://127.0.0.1:5000
```

#### Points de vérification

1. **Démarrage** : `python3 app.py` sans erreur
2. **API Regions** : Retourne 14 régions
3. **API Dijkstra** : Retourne chemin + temps
4. **Carte** : Affichage 14 marqueurs
5. **Itinéraire** : Tracé sur la carte

---

## 9. Glossaire Technique

| Terme | Signification |
|-------|--------------|
| **API** | Application Programming Interface |
| **Flask** | Framework web Python |
| **Leaflet** | Bibliothèque cartographique JS |
| **Matrice d'adjacence** | Représentation graphe |
| **Complexité O()** | Mesure performance |
| **Fallback** | Solution alternative |
| **Relaxation** | Mise à jour distance |
| **Cycle** | Chemin qui retourne au départ |

---

## Informations du Projet

- **Version :** 1.0
- **Date de création :** Avril 2026
- **Auteur :** Mamadou Thiam
- **Technologie :** Python Flask + HTML/JS Leaflet
- **Inspiré par :** Problèmes académiques d'algorithmie

---

*Document généré dans le cadre du projet académique Senegal Trip Planner*