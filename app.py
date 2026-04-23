"""
Application Flask - Senegal Trip Planner
Planificateur d'itinéraire pour les 14 régions du Sénégal.
Implémente les algorithmes de Dijkstra, Bellman-Ford et TSP (Two-Phase).
"""

# Imports des modules Flask et utilitaires
from flask import Flask, render_template, jsonify, request, send_from_directory
from typing import Dict, List, Optional, Any, Union
import math
import os

# Configuration de l'application Flask avec dossier static
app = Flask(__name__, static_folder='static')

# Route pour servir les fichiers statiques (manifest, icons, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# =============================================================================
# DONNÉES DES RÉGIONS
# =============================================================================
# Dictionary contenant les informations de chaque région:
# - name: Nom de la région
# - capital: Ville capitale
# - lat/lng: Coordonnées GPS
# - info: Description générale
# - tips: Conseils pratiques pour les voyageurs
# - security: Consignes de sécurité
# - hebergement: Options d'hébergement et budget
# - tourisme: Sites et attractions touristiques
regions = {
    "dakar": {
        "name": "Dakar", "capital": "Dakar", "lat": 14.7167, "lng": -17.4671,
        "info": "Capitale du Sénégal, plus grande ville et centre économique.",
        "tips": "Préférez les taxis officiels. Évitez les nuits tardives.",
        "security": "Zone sécurisée, mais vigilance recommandée la nuit.",
        "hebergement": "Hôtels: Radisson, Terrou Bi. Budget: 15000-150000 CFA/nuit.",
        "tourisme": "Île de Gorée, Musée Théodore Monod, Plateau."
    },
    "thies": {
        "name": "Thiès", "capital": "Thiès", "lat": 14.7941, "lng": -16.9639,
        "info": "Deuxième ville, pôle industriel et artisanale.",
        "tips": "Visitez les villages artisanaux de Rufisque.",
        "security": "Zone calme, respectez les us et coutumes locaux.",
        "hebergement": "Hôtel La Résidence. Budget: 8000-50000 CFA/nuit.",
        "tourisme": "Artisanat du tissu, villages traditionnels."
    },
    "diourbel": {
        "name": "Diourbel", "capital": "Diourbel", "lat": 14.7167, "lng": -16.2333,
        "info": "Capitale du Mboss, importante région religieuse.",
        "tips": "Respectez les lieux saints et horaires de prière.",
        "security": "Zone très pieuse, habillez-vous convenablement.",
        "hebergement": "Auberge du Roi. Budget: 5000-25000 CFA/nuit.",
        "tourisme": "Tombe de Bayam Nguidjam, marché central."
    },
    "kaolack": {
        "name": "Kaolack", "capital": "Kaolack", "lat": 14.1500, "lng": -16.0833,
        "info": "Centre économique du bassin arachidier.",
        "tips": "Marchandez dans les marchés, négociez les prix.",
        "security": "Zone commerciale animée, surveillez vos affaires.",
        "hebergement": "Hôtel Le Kaolack. Budget: 6000-30000 CFA/nuit.",
        "tourisme": "Marché hebdomadaire, agriculture arachidière."
    },
    "saintlouis": {
        "name": "Saint-Louis", "capital": "Saint-Louis", "lat": 16.0333, "lng": -16.5000,
        "info": "Ancienne capitale coloniale, patrimoine UNESCO.",
        "tips": "Explorez l'architecture coloniale française.",
        "security": "Zone historique sécurisée, mais prudence près du fleuve.",
        "hebergement": "Hôtel Mermoz, Maison Bleue. Budget: 10000-80000 CFA/nuit.",
        "tourisme": "Île Saint-Louis, Rue Gradolphe, Palais Ghadene."
    },
    "louga": {
        "name": "Louga", "capital": "Louga", "lat": 15.6333, "lng": -15.6333,
        "info": "Région sahélienne, élevage et commerce.",
        "tips": "Découvrez la culture peule traditionnelle.",
        "security": "Zone reculée, évitez les zones frontalières.",
        "hebergement": "Hôtel de Louga. Budget: 4000-15000 CFA/nuit.",
        "tourisme": "Marché pastoral, villages peuls."
    },
    "kolda": {
        "name": "Kolda", "capital": "Kolda", "lat": 12.8833, "lng": -14.9500,
        "info": "Région verdoyante au sud du pays.",
        "tips": "Préférez la saison sèche (Nov-Mai) pour visiter.",
        "security": "Zone rurale, restreignez vos déplacements la nuit.",
        "hebergement": "Auberge de Kolda. Budget: 5000-20000 CFA/nuit.",
        "tourisme": "Nature, fleuve Casamance."
    },
    "ziguinchor": {
        "name": "Ziguinchor", "capital": "Ziguinchor", "lat": 12.5833, "lng": -16.2667,
        "info": "Capitale du sud, vibes caribéennes.",
        "tips": "Prenez le bateau pour les îles du Saloum.",
        "security": "Zone touristique sécurisée, mais évitez les zones frontalières.",
        "hebergement": "Hôtel Kadiandouane, Auberge du Sud. Budget: 10000-60000 CFA/nuit.",
        "tourisme": "Plages, Île de Carabane, mangrove."
    },
    "sedhiou": {
        "name": "Sédhiou", "capital": "Sédhiou", "lat": 12.7167, "lng": -15.1833,
        "info": "Zone de transition entre Sine et Saloum.",
        "tips": "Visitez les villages historiques de la région.",
        "security": "Zone calme, respectez les coutumes locales.",
        "hebergement": "Hôtel de Sédhiou. Budget: 4000-15000 CFA/nuit.",
        "tourisme": "Villages traditionnels, histoire locale."
    },
    "kaffrine": {
        "name": "Kaffrine", "capital": "Kaffrine", "lat": 14.1000, "lng": -15.4167,
        "info": "Région agricole du bassin arachidier, cœur du pays Serer.",
        "tips": "Découvrez la culture Serer traditionnelle.",
        "security": "Zone rurale paisible.",
        "hebergement": "Auberge de Kaffrine. Budget: 3000-10000 CFA/nuit.",
        "tourisme": "Sites sacrés Serer, agriculture."
    },
    "kedougou": {
        "name": "Kédougou", "capital": "Kédougou", "lat": 12.5667, "lng": -12.1833,
        "info": "Plus orientale, réserve nationale Niokolo-Koba.",
        "tips": "Parc National pour safari photos. Réservez un guide.",
        "security": "Zone de parc, accompagnés toujours d'un guide.",
        "hebergement": "Lodge Campement. Budget: 15000-60000 CFA/nuit.",
        "tourisme": "Safari, éléphants, lions, parc Niokolo-Koba."
    },
    "matam": {
        "name": "Matam", "capital": "Matam", "lat": 15.6667, "lng": -13.2667,
        "info": "Région sahélienne sur le fleuve Niger.",
        "tips": "Essayez la traversée en pirogue sur le fleuve.",
        "security": "Zone reculée, évitez les déplacements nocturnes.",
        "hebergement": "Hôtel de Matam. Budget: 5000-20000 CFA/nuit.",
        "tourisme": "Fleuve Niger, pirogues, culture Peul."
    },
    "tamba": {
        "name": "Tambacounda", "capital": "Tambacounda", "lat": 13.7667, "lng": -13.6667,
        "info": "Plus grande région, porte du Sahel.",
        "tips": "Prévoyez un 4x4 pour les pistes rurales.",
        "security": "Zone vaste, restez sur les routes principales.",
        "hebergement": "Hôtel TAM. Budget: 6000-25000 CFA/nuit.",
        "tourisme": "Parc Niokolo-Koba, brousse, faune."
    },
    "fatick": {
        "name": "Fatick", "capital": "Fatick", "lat": 14.3333, "lng": -16.0833,
        "info": "Région Sine-Saloum, lagunes et mangroves.",
        "tips": "Visitez l'île de Joal-Fadiouth. Mélangez-vous à la population.",
        "security": "Zone touristique calme.",
        "hebergement": "Auberge de Fatick. Budget: 5000-30000 CFA/nuit.",
        "tourisme": "Île de Joal-Fadiouth, mangroves, ossature de poisson."
    }
}

# Liste de toutes les clés de régions (pour itération)
all_regions = list(regions.keys())

# =============================================================================
# MATRICES DE DISTANCES
# =============================================================================
# distances_national: Distances en km via routes nationales (vitesse max: 80 km/h)
# distances_autoroute: Distances en km via autoroutes (vitesse max: 100 km/h)
# Structure: {region_depart: {region_arrivee: distance_km}}
# =============================================================================
# MATRICES DE DISTANCES (valeurs Google Maps - routes réelles)
# =============================================================================
# Distances routières en km basées sur Google Maps (route en voiture)
# Ces distances représentent le trajet réel sur route, pas vol d'oiseau

distances_national = {
    # Dakar - connections directes
    "dakar": {"thies": 65, "fatick": 148, "kaolack": 192, "saintlouis": 256, "louga": 189, "diourbel": 122, "matam": 529, "kaffrine": 210, "tamba": 461, "ziguinchor": 454, "kolda": 658, "sedhiou": 410, "kedougou": 695},
    
    # Thiès
    "thies": {"dakar": 65, "diourbel": 77, "kaolack": 116, "fatick": 75, "kaffrine": 168, "louga": 122, "saintlouis": 195, "matam": 420, "tamba": 370, "ziguinchor": 258, "kolda": 320, "sedhiou": 276, "kedougou": 450},
    
    # Diourbel
    "diourbel": {"thies": 77, "kaolack": 57, "fatick": 40, "saintlouis": 155, "louga": 107, "kaffrine": 97, "matam": 338, "tamba": 293, "ziguinchor": 233, "kolda": 239, "sedhiou": 229, "kedougou": 497},
    
    # Kaolack
    "kaolack": {"thies": 116, "diourbel": 57, "fatick": 47, "kaffrine": 58, "saintlouis": 258, "louga": 160, "matam": 450, "tamba": 294, "ziguinchor": 271, "kolda": 516, "sedhiou": 172, "kedougou": 528, "dakar": 192},
    
    # Fatick
    "fatick": {"kaolack": 47, "kaffrine": 97, "thies": 75, "diourbel": 40, "saintlouis": 200, "louga": 155, "matam": 380, "tamba": 318, "ziguinchor": 200, "kolda": 547, "sedhiou": 204, "dakar": 148},
    
    # Saint-Louis
    "saintlouis": {"diourbel": 155, "louga": 73, "matam": 419, "thies": 195, "kaolack": 258, "fatick": 200, "kaffrine": 237, "tamba": 509, "ziguinchor": 539, "kolda": 694, "sedhiou": 383, "dakar": 256},
    
    # Louga
    "louga": {"saintlouis": 73, "diourbel": 107, "matam": 353, "thies": 122, "fatick": 155, "kaffrine": 183, "tamba": 343, "ziguinchor": 338, "kolda": 657, "sedhiou": 332, "dakar": 189},
    
    # Matam
    "matam": {"saintlouis": 419, "louga": 353, "tamba": 251, "diourbel": 338, "kaolack": 450, "kaffrine": 300, "thies": 420, "fatick": 380, "ziguinchor": 654, "kolda": 465, "sedhiou": 412, "dakar": 529},
    
    # Kaffrine
    "kaffrine": {"thies": 168, "diourbel": 97, "kaolack": 58, "fatick": 97, "tamba": 215, "matam": 300, "saintlouis": 237, "louga": 183, "ziguinchor": 188, "kolda": 147, "sedhiou": 156, "dakar": 210},
    
    # Tambacounda
    "tamba": {"kaffrine": 215, "matam": 251, "kolda": 224, "kedougou": 234, "kaolack": 294, "diourbel": 293, "thies": 370, "fatick": 318, "ziguinchor": 295, "saintlouis": 509, "louga": 343, "sedhiou": 307, "dakar": 461},
    
    # Kolda
    "kolda": {"ziguinchor": 186, "sedhiou": 85, "tamba": 224, "kaolack": 516, "kaffrine": 147, "fatick": 547, "thies": 320, "diourbel": 239, "matam": 465, "kedougou": 417, "dakar": 658},
    
    # Ziguinchor
    "ziguinchor": {"kolda": 186, "sedhiou": 78, "kaolack": 271, "fatick": 200, "tamba": 295, "kaffrine": 188, "thies": 258, "diourbel": 233, "dakar": 454},
    
    # Sédhiou
    "sedhiou": {"kaolack": 172, "kolda": 85, "ziguinchor": 78, "fatick": 204, "tamba": 307, "kaffrine": 156, "diourbel": 229, "thies": 276, "dakar": 410},
    
    # Kédougou
    "kedougou": {"tamba": 234, "kolda": 417, "matam": 474, "kaolack": 528, "thies": 450, "diourbel": 497, "dakar": 695}
}

# =============================================================================
# MATRICE AUTOROUTE (routes via autoroute, légèrement plus courtes)
# =============================================================================

distances_autoroute = {
    # Dakar - via autoroute
    "dakar": {"thies": 60, "fatick": 140, "kaolack": 185, "saintlouis": 245, "louga": 180, "diourbel": 115, "matam": 510, "kaffrine": 200, "tamba": 445, "ziguinchor": 440, "kolda": 630, "sedhiou": 395, "kedougou": 670},
    
    # Thiès
    "thies": {"dakar": 60, "diourbel": 72, "kaolack": 110, "fatick": 70, "kaffrine": 160, "louga": 115, "saintlouis": 185, "matam": 405, "tamba": 355, "ziguinchor": 250, "kolda": 305, "sedhiou": 265, "kedougou": 435},
    
    # Diourbel
    "diourbel": {"thies": 72, "kaolack": 54, "fatick": 38, "saintlouis": 148, "louga": 100, "kaffrine": 92, "matam": 325, "tamba": 280, "ziguinchor": 225, "kolda": 230, "sedhiou": 220, "kedougou": 480},
    
    # Kaolack
    "kaolack": {"thies": 110, "diourbel": 54, "fatick": 44, "kaffrine": 55, "saintlouis": 250, "louga": 152, "matam": 435, "tamba": 282, "ziguinchor": 262, "kolda": 498, "sedhiou": 165, "kedougou": 510, "dakar": 185},
    
    # Fatick
    "fatick": {"kaolack": 44, "kaffrine": 92, "thies": 70, "diourbel": 38, "saintlouis": 192, "louga": 148, "matam": 365, "tamba": 305, "ziguinchor": 192, "kolda": 528, "sedhiou": 196, "dakar": 140},
    
    # Saint-Louis
    "saintlouis": {"diourbel": 148, "louga": 70, "matam": 405, "thies": 185, "kaolack": 250, "fatick": 192, "kaffrine": 228, "tamba": 490, "ziguinchor": 520, "kolda": 668, "sedhiou": 368, "dakar": 245},
    
    # Louga
    "louga": {"saintlouis": 70, "diourbel": 100, "matam": 340, "thies": 115, "fatick": 148, "kaffrine": 175, "tamba": 330, "ziguinchor": 325, "kolda": 632, "sedhiou": 318, "dakar": 180},
    
    # Matam
    "matam": {"saintlouis": 405, "louga": 340, "tamba": 242, "diourbel": 325, "kaolack": 435, "kaffrine": 288, "thies": 405, "fatick": 365, "ziguinchor": 630, "kolda": 448, "sedhiou": 395, "dakar": 510},
    
    # Kaffrine
    "kaffrine": {"thies": 160, "diourbel": 92, "kaolack": 55, "fatick": 92, "tamba": 205, "matam": 288, "saintlouis": 228, "louga": 175, "ziguinchor": 180, "kolda": 140, "sedhiou": 150, "dakar": 200},
    
    # Tambacounda
    "tamba": {"kaffrine": 205, "matam": 242, "kolda": 215, "kedougou": 225, "kaolack": 282, "diourbel": 280, "thies": 355, "fatick": 305, "ziguinchor": 285, "saintlouis": 490, "louga": 330, "sedhiou": 295, "dakar": 445},
    
    # Kolda
    "kolda": {"ziguinchor": 178, "sedhiou": 82, "tamba": 215, "kaolack": 498, "kaffrine": 140, "fatick": 528, "thies": 305, "diourbel": 230, "matam": 448, "kedougou": 400, "dakar": 630},
    
    # Ziguinchor
    "ziguinchor": {"kolda": 178, "sedhiou": 75, "kaolack": 262, "fatick": 192, "tamba": 285, "kaffrine": 180, "thies": 250, "diourbel": 225, "dakar": 440},
    
    # Sédhiou
    "sedhiou": {"kaolack": 165, "kolda": 82, "ziguinchor": 75, "fatick": 196, "tamba": 295, "kaffrine": 150, "diourbel": 220, "thies": 265, "dakar": 395},
    
    # Kédougou
    "kedougou": {"tamba": 225, "kolda": 400, "matam": 458, "kaolack": 510, "thies": 435, "diourbel": 480, "dakar": 670}
}


# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================

def haversine(lat1, lon1, lat2, lon2):
    """
    Formule de Haversine pour calculer la distance entre deux points GPS.
    Utilisée comme fallback quand une route directe n'existe pas.
    Retourne la distance en km.
    """
    R = 6371  # Rayon de la Terre en km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.asin(math.sqrt(a))


def get_distance(r1, r2, dist_matrix):
    """
    Récupère la distance entre deux régions depuis la matrice.
    Retourne 0 si même région, sinon cherche dans la matrice.
    Utilise Haversine comme fallback pour routes non définies.
    """
    if r1 == r2:
        return 0
    if r1 in dist_matrix and r2 in dist_matrix[r1]:
        return dist_matrix[r1][r2]
    if r2 in dist_matrix and r1 in dist_matrix[r2]:
        return dist_matrix[r2][r1]
    d = haversine(regions[r1]['lat'], regions[r1]['lng'], regions[r2]['lat'], regions[r2]['lng'])
    return d if d > 0 else 999


def build_matrix(distances):
    """
    Construit une matrice de distances complète pour toutes les paires de régions.
    Assure que toutes les entrées ont une valeur (évite les None).
    """
    matrix = {}
    for r1 in all_regions:
        matrix[r1] = {}
        for r2 in all_regions:
            d = get_distance(r1, r2, distances)
            matrix[r1][r2] = d if d > 0 else 999
    return matrix


# Construction des matrices complètes (national et autoroute)
road_matrix_national = build_matrix(distances_national)
road_matrix_autoroute = build_matrix(distances_autoroute)


# =============================================================================
# ALGORITHMES DE ROUTAGE
# =============================================================================

def dijkstra(start: str, end: str, matrix: Dict[str, Dict[str, float]]) -> tuple:
    """
    Algorithme de Dijkstra - Plus court chemin.
    Complexité: O(V²) où V = nombre de régions.
    Trouve le chemin le plus court entre deux régions.
    """
    dist: Dict[str, float] = {r: 9999.0 for r in all_regions}
    prev: Dict[str, Union[str, None]] = {r: None for r in all_regions}
    dist[start] = 0.0
    unvisited: set = set(all_regions)

    while unvisited:
        current = min(unvisited, key=lambda x: dist[x])
        if current == end or dist[current] >= 9999:
            break
        unvisited.remove(current)

        for neighbor in all_regions:
            if neighbor in unvisited:
                edge_dist = matrix[current].get(neighbor, 9999)
                if 0 < edge_dist < 9999:
                    new_dist = dist[current] + edge_dist
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        prev[neighbor] = current

    path = []
    current = end
    while current and prev[current]:
        path.insert(0, current)
        current = prev[current]
    if path and path[0] != start:
        path.insert(0, start)

    if not path or path[0] != start:
        return [start], 0

    return path, round(dist[end]) if dist[end] < 9999 else 0


def bellman_ford(start: str, end: str, matrix: Dict[str, Dict[str, float]]) -> tuple:
    """
    Algorithme de Bellman-Ford - Plus court chemin avec support poids négatifs.
    Complexité: O(V*E) où V = régions, E = arêtes.
    Utile pour des scénarios avec coûts variables.
    """
    dist: Dict[str, float] = {r: float('inf') for r in all_regions}
    prev: Dict[str, Union[str, None]] = {r: None for r in all_regions}
    dist[start] = 0.0

    for _ in range(len(all_regions) - 1):
        for u in all_regions:
            for v in all_regions:
                if matrix[u][v] < 9999:
                    if dist[u] + matrix[u][v] < dist[v]:
                        dist[v] = dist[u] + matrix[u][v]
                        prev[v] = u

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


def calculate_path_distance(path, matrix):
    """Calcule la distance totale d'un parcours en additionnant les segments."""
    total = 0
    for i in range(len(path) - 1):
        if matrix[path[i]][path[i+1]] < 9999:
            total += matrix[path[i]][path[i+1]]
    return total


# =============================================================================
# ALGORITHME TSP (PROBLÈME DU VENDEUR AMBULANT)
# =============================================================================

def tsp_nearest_neighbor(matrix, start):
    """
    Phase 1: Algorithme Nearest Neighbor - Solution initiale pour le TSP.
    Complexité: O(n²) où n = nombre de régions.
    Construit une solution greedy en visitant le voisin le plus proche.
    """
    visited = {start}
    path = [start]
    current = start
    unvisited = set(all_regions) - {start}

    while unvisited:
        candidates = [(x, matrix[current][x]) for x in unvisited if 0 < matrix[current][x] < 9999]
        if not candidates:
            candidates = [(x, matrix[x][current]) for x in unvisited if 0 < matrix[x][current] < 9999]
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


def two_opt_optimize(path, matrix, max_iterations=300):
    """
    Phase 2: 2-opt Local Search Optimization.
    Complexité: O(n² × itérations).
    Améliore la solution en inversant des segments pour réduire la distance totale.
    """
    if len(path) < 4:
        return path
    
    improved = True
    iteration = 0
    best_path = path[:-1].copy()
    
    while improved and iteration < max_iterations:
        improved = False
        iteration += 1
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
            if improved:
                break
    
    best_path.append(best_path[0])
    return best_path


def two_phase_tsp(matrix, start):
    """
    Algorithme TSP en deux phases pour circuit touristique optimal:
    - Phase 1: Nearest Neighbor (solution initiale greedy)
    - Phase 2: 2-opt (optimisation locale pour améliorer la solution)
    Retourne le chemin optimisé et la distance totale.
    """
    initial_path = tsp_nearest_neighbor(matrix, start)
    optimized_path = two_opt_optimize(initial_path, matrix)
    total_distance = calculate_path_distance(optimized_path, matrix)
    
    return optimized_path, round(total_distance)


def format_time(hours):
    """Convertit les heures décimales en format lisible (ex: 2h 30min)."""
    h = int(hours)
    m = int((hours - h) * 60)
    if h > 0:
        return f"{h}h {m}min"
    return f"{m}min"


# =============================================================================
# ROUTES Flask
# =============================================================================

@app.route('/')
def index():
    """Page principale - Affiche la carte et les contrôles."""
    return render_template('index.html', regions=regions)


@app.route('/api/regions')
def get_regions():
    """API REST - Retourne toutes les données des régions au format JSON."""
    return jsonify(regions)


@app.route('/api/dijkstra')
def api_dijkstra():
    """
    API Dijkstra - Calcule le plus court chemin entre départ et destination.
    Paramètres GET: start (clé région), destination (clé région)
    Retourne: path[], distance, time pour routes nationales et autoroute.
    """
    destination = request.args.get('destination')
    start = request.args.get('start', 'dakar')
    
    if not destination or start not in all_regions or destination not in all_regions:
        return jsonify({"error": "Paramètres invalides"}), 400
    
    path_national, dist_national = dijkstra(start, destination, road_matrix_national)
    path_autoroute, dist_autoroute = dijkstra(start, destination, road_matrix_autoroute)
    
    # Vitesses moyennes réelles au Sénégal (km/h)
    # Routes nationales: 60 km/h (moyenne avecTraffic, état des routes)
    # Autoroute: 100 km/h (limitée à 110 mais circulation)
    speed_national = 60
    speed_autoroute = 100
    
    return jsonify({
        "national": {
            "path": path_national,
            "distance": dist_national,
            "time": format_time(dist_national / speed_national)
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / speed_autoroute)
        }
    })


@app.route('/api/bellman')
def api_bellman():
    """
    API Bellman-Ford - Calcule le plus court chemin avec algorithme Bellman-Ford.
    Paramètres GET: start, destination
    Retourne: path[], distance, time pour les deux types de routes.
    """
    destination = request.args.get('destination')
    start = request.args.get('start', 'dakar')
    
    if not destination or start not in all_regions or destination not in all_regions:
        return jsonify({"error": "Paramètres invalides"}), 400
    
    path_national, dist_national = bellman_ford(start, destination, road_matrix_national)
    path_autoroute, dist_autoroute = bellman_ford(start, destination, road_matrix_autoroute)
    
    speed_national = 60
    speed_autoroute = 100
    
    return jsonify({
        "algorithm": "Bellman-Ford",
        "national": {
            "path": path_national,
            "distance": dist_national,
            "time": format_time(dist_national / speed_national)
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / speed_autoroute)
        }
    })


@app.route('/api/tsp')
def api_tsp():
    """
    API TSP - Calcule un circuit touristique passant par toutes les régions.
    Paramètre GET: start (région de départ)
    Retourne: chemin optimisé visiting toutes les régions + distance totale.
    """
    start = request.args.get('start', 'dakar')
    
    if start not in all_regions:
        return jsonify({"error": "Point de départ invalide"}), 400
    
    path_national, dist_national = two_phase_tsp(road_matrix_national, start)
    path_autoroute, dist_autoroute = two_phase_tsp(road_matrix_autoroute, start)
    
    speed_national = 60
    speed_autoroute = 100
    
    return jsonify({
        "algorithm": "Two-Phase TSP (Nearest Neighbor + 2-opt)",
        "national": {
            "path": path_national,
            "distance": dist_national,
            "time": format_time(dist_national / speed_national)
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / speed_autoroute)
        }
    })


if __name__ == '__main__':
    # Démarrage du serveur Flask en mode debug
    # Accessible sur http://localhost:5000
    app.run(debug=True)