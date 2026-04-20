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

## Informations du Projet

- **Version :** 1.0
- **Date de création :** Avril 2026
- **Auteur :** Mamadou Thiam
- **Technologie :** Python Flask + HTML/JS Leaflet

---

*Document généré dans le cadre du projet académique Senegal Trip Planner*