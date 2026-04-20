from flask import Flask, render_template, jsonify, request
import math

app = Flask(__name__)

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
        "security": "Zone calme, respectez les us etcoutumes locaux.",
        "hebergement": "Hôtel La Résidence. Budget: 8000-50000 CFA/nuit.",
        "tourisme": " artisanat du tissu, villages traditionnels."
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
        "tips": "Prenez le bateau pour les îles de lSaloum.",
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

all_regions = list(regions.keys())

distances_national = {
    "dakar": {"thies": 46, "fatick": 148, "kaolack": 188},
    "thies": {"dakar": 46, "diourbel": 77, "kaolack": 116, "fatick": 75, "kaffrine": 90, "louga": 155, "saintlouis": 146},
    "diourbel": {"thies": 77, "kaolack": 85, "saintlouis": 120, "louga": 90, "kaffrine": 65},
    "kaolack": {"thies": 116, "diourbel": 85, "fatick": 65, "kaffrine": 58, "sedhiou": 135, "ziguinchor": 205, "tamba": 285, "kolda": 185},
    "saintlouis": {"diourbel": 120, "louga": 85, "matam": 180},
    "louga": {"saintlouis": 85, "diourbel": 90, "matam": 110, "thies": 155},
    "kolda": {"ziguinchor": 105, "sedhiou": 65, "tamba": 145, "kaolack": 185},
    "ziguinchor": {"kolda": 105, "sedhiou": 85},
    "sedhiou": {"kaolack": 135, "kolda": 65, "ziguinchor": 85, "fatick": 115},
    "kaffrine": {"thies": 90, "diourbel": 65, "kaolack": 58, "tamba": 105, "fatick": 78},
    "kedougou": {"tamba": 185, "kolda": 305},
    "matam": {"saintlouis": 180, "louga": 110, "tamba": 160},
    "tamba": {"kaffrine": 105, "matam": 160, "kolda": 145, "kedougou": 185, "kaolack": 285},
    "fatick": {"kaolack": 65, "kaffrine": 78, "sedhiou": 115, "thies": 75}
}

distances_autoroute = {
    "dakar": {"thies": 42, "fatick": 140, "kaolack": 175},
    "thies": {"dakar": 42, "diourbel": 72, "kaolack": 110, "fatick": 68, "kaffrine": 85, "louga": 148, "saintlouis": 140},
    "diourbel": {"thies": 72, "kaolack": 80, "saintlouis": 115, "louga": 85, "kaffrine": 60},
    "kaolack": {"thies": 110, "diourbel": 80, "fatick": 58, "kaffrine": 55, "sedhiou": 125, "ziguinchor": 192, "tamba": 268, "kolda": 172},
    "saintlouis": {"diourbel": 115, "louga": 78, "matam": 170},
    "louga": {"saintlouis": 78, "diourbel": 85, "matam": 105, "thies": 148},
    "kolda": {"ziguinchor": 98, "sedhiou": 58, "tamba": 135, "kaolack": 172},
    "ziguinchor": {"kolda": 98, "sedhiou": 75},
    "sedhiou": {"kaolack": 125, "kolda": 58, "ziguinchor": 75, "fatick": 105},
    "kaffrine": {"thies": 85, "diourbel": 60, "kaolack": 55, "tamba": 95, "fatick": 70},
    "kedougou": {"tamba": 172, "kolda": 288},
    "matam": {"saintlouis": 170, "louga": 105, "tamba": 150},
    "tamba": {"kaffrine": 95, "matam": 150, "kolda": 135, "kedougou": 172, "kaolack": 268},
    "fatick": {"kaolack": 58, "kaffrine": 70, "sedhiou": 105, "thies": 68}
}


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.asin(math.sqrt(a))


def get_distance(r1, r2, dist_matrix):
    if r1 == r2:
        return 0
    if r1 in dist_matrix and r2 in dist_matrix[r1]:
        return dist_matrix[r1][r2]
    if r2 in dist_matrix and r1 in dist_matrix[r2]:
        return dist_matrix[r2][r1]
    d = haversine(regions[r1]['lat'], regions[r1]['lng'], regions[r2]['lat'], regions[r2]['lng'])
    return d if d > 0 else 999


def build_matrix(distances):
    matrix = {}
    for r1 in all_regions:
        matrix[r1] = {}
        for r2 in all_regions:
            d = get_distance(r1, r2, distances)
            matrix[r1][r2] = d if d > 0 else 999
    return matrix


road_matrix_national = build_matrix(distances_national)
road_matrix_autoroute = build_matrix(distances_autoroute)


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


@app.route('/')
def index():
    return render_template('index.html', regions=regions)


@app.route('/api/regions')
def get_regions():
    return jsonify(regions)


def format_time(hours):
    h = int(hours)
    m = int((hours - h) * 60)
    if h > 0:
        return f"{h}h {m}min"
    return f"{m}min"


@app.route('/api/dijkstra')
def api_dijkstra():
    destination = request.args.get('destination')
    start = request.args.get('start', 'dakar')
    
    if not destination or start not in all_regions or destination not in all_regions:
        return jsonify({"error": "Paramètres invalides"}), 400
    
    path_national, dist_national = dijkstra(start, destination, road_matrix_national)
    path_autoroute, dist_autoroute = dijkstra(start, destination, road_matrix_autoroute)
    
    speed_national = 80
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


def calculate_path_distance(path, matrix):
    """Calculate total distance of a path."""
    total = 0
    for i in range(len(path) - 1):
        if matrix[path[i]][path[i+1]] < 9999:
            total += matrix[path[i]][path[i+1]]
    return total


def tsp_nearest_neighbor(matrix, start):
    """
    Phase 1: Nearest Neighbor Algorithm.
    Generates initial solution by always visiting the nearest unvisited city.
    
    Algorithm:
    1. Start from given city
    2. Repeatedly visit the nearest unvisited city
    3. Return to start when all cities visited
    
    Time Complexity: O(n²) where n = number of cities
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
    Improves initial solution by removing crossing edges.
    
    Algorithm:
    1. Remove two edges (i,i+1) and (j,j+1)
    2. Reconnect in opposite order to form new path
    3. Repeat until no improvement found
    
    Time Complexity: O(n² * iterations)
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
    Two-Phase TSP Algorithm:
    - Phase 1: Nearest Neighbor (initial solution)
    - Phase 2: 2-opt (optimization)
    
    Returns optimized path and total distance.
    """
    initial_path = tsp_nearest_neighbor(matrix, start)
    optimized_path = two_opt_optimize(initial_path, matrix)
    total_distance = calculate_path_distance(optimized_path, matrix)
    
    return optimized_path, round(total_distance)


@app.route('/api/tsp')
def api_tsp():
    """TSP API endpoint - returns optimized circuit visiting all regions."""
    start = request.args.get('start', 'dakar')
    
    if start not in all_regions:
        return jsonify({"error": "Point de départ invalide"}), 400
    
    path_national, dist_national = two_phase_tsp(road_matrix_national, start)
    path_autoroute, dist_autoroute = two_phase_tsp(road_matrix_autoroute, start)
    
    speed_national = 80
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


if __name__ == '__main__':
    app.run(debug=True)
