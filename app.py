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
# graph_data: Routes info with road names
# Structure: {region_depart: {region_arrivee: distance_km}}

GRAPH_DATA = {
    ("dakar", "thies"): {"d_nat": 70, "d_aut": 62, "road_nat": "RN1", "road_aut": "Autoroute de l'Avenir (A1)"},
    ("thies", "dakar"): {"d_nat": 70, "d_aut": 62, "road_nat": "RN1", "road_aut": "Autoroute de l'Avenir (A1)"},
    ("dakar", "kaolack"): {"d_nat": 190, "d_aut": 180, "road_nat": "RN1", "road_aut": "RN1"},
    ("kaolack", "dakar"): {"d_nat": 190, "d_aut": 180, "road_nat": "RN1", "road_aut": "RN1"},
    ("dakar", "saintlouis"): {"d_nat": 264, "d_aut": 250, "road_nat": "RN2", "road_aut": "Autoroute de la Côte (A1)"},
    ("saintlouis", "dakar"): {"d_nat": 264, "d_aut": 250, "road_nat": "RN2", "road_aut": "Autoroute de la Côte (A1)"},
    ("dakar", "louga"): {"d_nat": 200, "d_aut": 190, "road_nat": "RN2", "road_aut": "RN2"},
    ("louga", "dakar"): {"d_nat": 200, "d_aut": 190, "road_nat": "RN2", "road_aut": "RN2"},
    ("dakar", "diourbel"): {"d_nat": 146, "d_aut": 140, "road_nat": "RN3", "road_aut": "RN3"},
    ("diourbel", "dakar"): {"d_nat": 146, "d_aut": 140, "road_nat": "RN3", "road_aut": "RN3"},
    ("dakar", "fatick"): {"d_nat": 155, "d_aut": 145, "road_nat": "RN1", "road_aut": "RN1"},
    ("fatick", "dakar"): {"d_nat": 155, "d_aut": 145, "road_nat": "RN1", "road_aut": "RN1"},
    ("dakar", "ziguinchor"): {"d_nat": 452, "d_aut": 427, "road_nat": "RN4", "road_aut": "RN4"},
    ("ziguinchor", "dakar"): {"d_nat": 452, "d_aut": 427, "road_nat": "RN4", "road_aut": "RN4"},
    ("dakar", "matam"): {"d_nat": 540, "d_aut": 510, "road_nat": "RN2", "road_aut": "RN2"},
    ("matam", "dakar"): {"d_nat": 540, "d_aut": 510, "road_nat": "RN2", "road_aut": "RN2"},
    ("dakar", "tamba"): {"d_nat": 460, "d_aut": 435, "road_nat": "RN1", "road_aut": "RN1"},
    ("tamba", "dakar"): {"d_nat": 460, "d_aut": 435, "road_nat": "RN1", "road_aut": "RN1"},
    ("dakar", "kolda"): {"d_nat": 697, "d_aut": 662, "road_nat": "RN1/RN4", "road_aut": "RN1/RN4"},
    ("kolda", "dakar"): {"d_nat": 697, "d_aut": 662, "road_nat": "RN1/RN4", "road_aut": "RN1/RN4"},
    ("kaolack", "kolda"): {"d_nat": 352, "d_aut": 335, "road_nat": "RN4", "road_aut": "RN4"},
    ("kolda", "kaolack"): {"d_nat": 352, "d_aut": 335, "road_nat": "RN4", "road_aut": "RN4"},
    ("thies", "diourbel"): {"d_nat": 76, "d_aut": 68, "road_nat": "RN3", "road_aut": "Autoroute ILA TOUBA"},
    ("diourbel", "thies"): {"d_nat": 76, "d_aut": 68, "road_nat": "RN3", "road_aut": "Autoroute ILA TOUBA"},
    ("thies", "fatick"): {"d_nat": 62, "d_aut": 58, "road_nat": "RN1", "road_aut": "RN1"},
    ("fatick", "thies"): {"d_nat": 62, "d_aut": 58, "road_nat": "RN1", "road_aut": "RN1"},
    ("thies", "louga"): {"d_nat": 112, "d_aut": 105, "road_nat": "RN2", "road_aut": "RN2"},
    ("louga", "thies"): {"d_nat": 112, "d_aut": 105, "road_nat": "RN2", "road_aut": "RN2"},
    ("thies", "saintlouis"): {"d_nat": 180, "d_aut": 165, "road_nat": "RN2", "road_aut": "Autoroute Thiès-St Louis (Projet)"},
    ("saintlouis", "thies"): {"d_nat": 180, "d_aut": 165, "road_nat": "RN2", "road_aut": "Autoroute Thiès-St Louis (Projet)"},
    ("diourbel", "kaolack"): {"d_nat": 46, "d_aut": 42, "road_nat": "RN3", "road_aut": "RN3"},
    ("kaolack", "diourbel"): {"d_nat": 46, "d_aut": 42, "road_nat": "RN3", "road_aut": "RN3"},
    ("fatick", "kaolack"): {"d_nat": 60, "d_aut": 58, "road_nat": "RN1", "road_aut": "RN1"},
    ("kaolack", "fatick"): {"d_nat": 60, "d_aut": 58, "road_nat": "RN1", "road_aut": "RN1"},
    ("kaolack", "kaffrine"): {"d_nat": 115, "d_aut": 110, "road_nat": "RN1", "road_aut": "RN1"},
    ("kaffrine", "kaolack"): {"d_nat": 115, "d_aut": 110, "road_nat": "RN1", "road_aut": "RN1"},
    ("diourbel", "kaffrine"): {"d_nat": 130, "d_aut": 125, "road_nat": "RN3", "road_aut": "RN3"},
    ("kaffrine", "diourbel"): {"d_nat": 130, "d_aut": 125, "road_nat": "RN3", "road_aut": "RN3"},
    ("kaolack", "ziguinchor"): {"d_nat": 262, "d_aut": 250, "road_nat": "RN4 (Transgambienne)", "road_aut": "RN4"},
    ("ziguinchor", "kaolack"): {"d_nat": 262, "d_aut": 250, "road_nat": "RN4 (Transgambienne)", "road_aut": "RN4"},
    ("kaffrine", "tamba"): {"d_nat": 213, "d_aut": 200, "road_nat": "RN1", "road_aut": "RN1"},
    ("tamba", "kaffrine"): {"d_nat": 213, "d_aut": 200, "road_nat": "RN1", "road_aut": "RN1"},
    ("tamba", "kedougou"): {"d_nat": 233, "d_aut": 220, "road_nat": "RN7", "road_aut": "RN7"},
    ("kedougou", "tamba"): {"d_nat": 233, "d_aut": 220, "road_nat": "RN7", "road_aut": "RN7"},
    ("tamba", "kolda"): {"d_nat": 227, "d_aut": 215, "road_nat": "RN6", "road_aut": "RN6"},
    ("kolda", "tamba"): {"d_nat": 227, "d_aut": 215, "road_nat": "RN6", "road_aut": "RN6"},
    ("kolda", "ziguinchor"): {"d_nat": 148, "d_aut": 140, "road_nat": "RN6", "road_aut": "RN6"},
    ("ziguinchor", "kolda"): {"d_nat": 148, "d_aut": 140, "road_nat": "RN6", "road_aut": "RN6"},
    ("kolda", "sedhiou"): {"d_nat": 90, "d_aut": 82, "road_nat": "RN6", "road_aut": "RN6"},
    ("sedhiou", "kolda"): {"d_nat": 90, "d_aut": 82, "road_nat": "RN6", "road_aut": "RN6"},
    ("sedhiou", "ziguinchor"): {"d_nat": 115, "d_aut": 105, "road_nat": "RN6", "road_aut": "RN6"},
    ("ziguinchor", "sedhiou"): {"d_nat": 115, "d_aut": 105, "road_nat": "RN6", "road_aut": "RN6"},
    ("louga", "saintlouis"): {"d_nat": 68, "d_aut": 62, "road_nat": "RN2", "road_aut": "RN2"},
    ("saintlouis", "louga"): {"d_nat": 68, "d_aut": 62, "road_nat": "RN2", "road_aut": "RN2"},
    ("saintlouis", "matam"): {"d_nat": 424, "d_aut": 400, "road_nat": "RN2", "road_aut": "RN2"},
    ("matam", "saintlouis"): {"d_nat": 424, "d_aut": 400, "road_nat": "RN2", "road_aut": "RN2"},
    ("diourbel", "matam"): {"d_nat": 389, "d_aut": 365, "road_nat": "RN3", "road_aut": "RN3"},
    ("matam", "diourbel"): {"d_nat": 389, "d_aut": 365, "road_nat": "RN3", "road_aut": "RN3"},
    ("dakar", "sedhiou"): {"d_nat": 537, "d_aut": 512, "road_nat": "RN4", "road_aut": "RN4"},
    ("sedhiou", "dakar"): {"d_nat": 537, "d_aut": 512, "road_nat": "RN4", "road_aut": "RN4"},
    ("dakar", "kedougou"): {"d_nat": 700, "d_aut": 665, "road_nat": "RN7", "road_aut": "RN7"},
    ("kedougou", "dakar"): {"d_nat": 700, "d_aut": 665, "road_nat": "RN7", "road_aut": "RN7"},
    ("dakar", "kaffrine"): {"d_nat": 255, "d_aut": 240, "road_nat": "RN1", "road_aut": "RN1"},
    ("kaffrine", "dakar"): {"d_nat": 255, "d_aut": 240, "road_nat": "RN1", "road_aut": "RN1"},
}
# =============================================================================
# MATRICES DE DISTANCES (valeurs Google Maps - routes réelles)
# =============================================================================
# Distances routières en km basées sur Google Maps (route en voiture)
# Ces distances représentent le trajet réel sur route, pas vol d'oiseau

distances_national = {
    "dakar": {"thies": 70, "diourbel": 146, "kaolack": 190, "fatick": 155, "saintlouis": 264, "louga": 200, "kolda": 697, "ziguinchor": 452, "sedhiou": 537, "kaffrine": 255, "kedougou": 700, "matam": 540, "tamba": 460},
    "thies": {"dakar": 70, "diourbel": 76, "kaolack": 120, "fatick": 62, "saintlouis": 180, "louga": 112, "kolda": 547, "ziguinchor": 467, "sedhiou": 552, "kaffrine": 205, "kedougou": 630, "matam": 470, "tamba": 390},
    "diourbel": {"dakar": 146, "thies": 76, "kaolack": 46, "fatick": 106, "saintlouis": 232, "louga": 168, "kolda": 573, "ziguinchor": 493, "sedhiou": 578, "kaffrine": 130, "kedougou": 560, "matam": 389, "tamba": 320},
    "kaolack": {"dakar": 190, "thies": 120, "diourbel": 46, "fatick": 60, "kaffrine": 115, "saintlouis": 310, "louga": 278, "kolda": 352, "ziguinchor": 262, "sedhiou": 442, "kedougou": 495, "matam": 475, "tamba": 294},
    "fatick": {"dakar": 155, "thies": 62, "diourbel": 106, "kaolack": 60, "kaffrine": 175, "saintlouis": 248, "louga": 190, "kolda": 499, "ziguinchor": 377, "sedhiou": 467, "kedougou": 535, "matam": 456, "tamba": 318},
    "saintlouis": {"dakar": 264, "thies": 180, "diourbel": 232, "kaolack": 310, "fatick": 248, "louga": 68, "kolda": 762, "ziguinchor": 787, "sedhiou": 877, "kaffrine": 372, "kedougou": 840, "matam": 424, "tamba": 509},
    "louga": {"dakar": 200, "thies": 112, "diourbel": 168, "kaolack": 278, "fatick": 190, "saintlouis": 68, "kolda": 709, "ziguinchor": 734, "sedhiou": 824, "kaffrine": 318, "kedougou": 770, "matam": 353, "tamba": 343},
    "kolda": {"dakar": 697, "thies": 547, "diourbel": 573, "kaolack": 352, "fatick": 499, "saintlouis": 762, "louga": 709, "ziguinchor": 148, "sedhiou": 90, "kaffrine": 467, "kedougou": 417, "matam": 541, "tamba": 227},
    "ziguinchor": {"dakar": 452, "thies": 467, "diourbel": 493, "kaolack": 262, "fatick": 377, "saintlouis": 787, "louga": 734, "kolda": 148, "sedhiou": 115, "kaffrine": 377, "kedougou": 680, "matam": 654, "tamba": 311},
    "sedhiou": {"dakar": 537, "thies": 552, "diourbel": 578, "kaolack": 442, "fatick": 467, "saintlouis": 877, "louga": 824, "kolda": 90, "ziguinchor": 115, "kaffrine": 582, "kedougou": 535, "matam": 631, "tamba": 307},
    "kaffrine": {"dakar": 255, "thies": 205, "diourbel": 130, "kaolack": 115, "fatick": 175, "saintlouis": 372, "louga": 318, "kolda": 467, "ziguinchor": 377, "sedhiou": 582, "kedougou": 440, "matam": 475, "tamba": 213},
    "kedougou": {"dakar": 700, "thies": 630, "diourbel": 560, "kaolack": 495, "fatick": 535, "saintlouis": 840, "louga": 770, "kolda": 417, "ziguinchor": 680, "sedhiou": 535, "kaffrine": 440, "matam": 530, "tamba": 233},
    "matam": {"dakar": 540, "thies": 470, "diourbel": 389, "kaolack": 475, "fatick": 456, "saintlouis": 424, "louga": 353, "kolda": 541, "ziguinchor": 654, "sedhiou": 631, "kaffrine": 475, "kedougou": 530, "tamba": 251},
    "tamba": {"dakar": 460, "thies": 390, "diourbel": 320, "kaolack": 294, "fatick": 318, "saintlouis": 509, "louga": 343, "kolda": 227, "ziguinchor": 311, "sedhiou": 307, "kaffrine": 213, "kedougou": 233, "matam": 251}
}

# =============================================================================
# MATRICE AUTOROUTE (routes via autoroute, légèrement plus courtes)
# =============================================================================

distances_autoroute = {
    "dakar": {"thies": 65, "diourbel": 140, "kaolack": 180, "fatick": 145, "saintlouis": 250, "louga": 190, "kolda": 662, "ziguinchor": 427, "sedhiou": 512, "kaffrine": 240, "kedougou": 665, "matam": 510, "tamba": 435},
    "thies": {"dakar": 65, "diourbel": 68, "kaolack": 115, "fatick": 58, "saintlouis": 165, "louga": 105, "kolda": 520, "ziguinchor": 440, "sedhiou": 525, "kaffrine": 190, "kedougou": 600, "matam": 445, "tamba": 370},
    "diourbel": {"dakar": 140, "thies": 68, "kaolack": 42, "fatick": 100, "saintlouis": 218, "louga": 158, "kolda": 545, "ziguinchor": 465, "sedhiou": 550, "kaffrine": 125, "kedougou": 530, "matam": 365, "tamba": 300},
    "kaolack": {"dakar": 180, "thies": 115, "diourbel": 42, "fatick": 58, "kaffrine": 110, "saintlouis": 295, "louga": 262, "kolda": 335, "ziguinchor": 250, "sedhiou": 420, "kedougou": 470, "matam": 450, "tamba": 280},
    "fatick": {"dakar": 145, "thies": 58, "diourbel": 100, "kaolack": 58, "kaffrine": 165, "saintlouis": 235, "louga": 180, "kolda": 475, "ziguinchor": 358, "sedhiou": 445, "kedougou": 510, "matam": 430, "tamba": 300},
    "saintlouis": {"dakar": 250, "thies": 165, "diourbel": 218, "kaolack": 295, "fatick": 235, "louga": 62, "kolda": 725, "ziguinchor": 750, "sedhiou": 840, "kaffrine": 355, "kedougou": 800, "matam": 400, "tamba": 485},
    "louga": {"dakar": 190, "thies": 105, "diourbel": 158, "kaolack": 262, "fatick": 180, "saintlouis": 62, "kolda": 672, "ziguinchor": 697, "sedhiou": 787, "kaffrine": 302, "kedougou": 730, "matam": 335, "tamba": 325},
    "kolda": {"dakar": 662, "thies": 520, "diourbel": 545, "kaolack": 335, "fatick": 475, "saintlouis": 725, "louga": 672, "ziguinchor": 140, "sedhiou": 82, "kaffrine": 445, "kedougou": 395, "matam": 515, "tamba": 215},
    "ziguinchor": {"dakar": 427, "thies": 440, "diourbel": 465, "kaolack": 250, "fatick": 358, "saintlouis": 750, "louga": 697, "kolda": 140, "sedhiou": 105, "kaffrine": 358, "kedougou": 650, "matam": 620, "tamba": 295},
    "sedhiou": {"dakar": 512, "thies": 525, "diourbel": 550, "kaolack": 420, "fatick": 445, "saintlouis": 840, "louga": 787, "kolda": 82, "ziguinchor": 105, "kaffrine": 555, "kedougou": 505, "matam": 595, "tamba": 290},
    "kaffrine": {"dakar": 240, "thies": 190, "diourbel": 125, "kaolack": 110, "fatick": 165, "saintlouis": 355, "louga": 302, "kolda": 445, "ziguinchor": 358, "sedhiou": 555, "kedougou": 420, "matam": 450, "tamba": 200},
    "kedougou": {"dakar": 665, "thies": 600, "diourbel": 530, "kaolack": 470, "fatick": 510, "saintlouis": 800, "louga": 730, "kolda": 395, "ziguinchor": 650, "sedhiou": 505, "kaffrine": 420, "matam": 505, "tamba": 220},
    "matam": {"dakar": 510, "thies": 445, "diourbel": 365, "kaolack": 450, "fatick": 430, "saintlouis": 400, "louga": 335, "kolda": 515, "ziguinchor": 620, "sedhiou": 595, "kaffrine": 450, "kedougou": 505, "tamba": 235},
    "tamba": {"dakar": 435, "thies": 370, "diourbel": 300, "kaolack": 280, "fatick": 300, "saintlouis": 485, "louga": 325, "kolda": 215, "ziguinchor": 295, "sedhiou": 290, "kaffrine": 200, "kedougou": 220, "matam": 235}
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


def get_road_info(r1: str, r2: str) -> dict:
    """Récupère les infos de route (nom route nationale, distance) entre deux régions."""
    key = (r1, r2)
    reverse_key = (r2, r1)
    if key in GRAPH_DATA:
        return GRAPH_DATA[key]
    elif reverse_key in GRAPH_DATA:
        return GRAPH_DATA[reverse_key]
    return {"d_nat": 0, "d_aut": 0, "road_nat": "Route locale", "road_aut": "Route locale"}


def get_path_roads(path: list, matrix_type: str = "national") -> list:
    """Retourne les infos de route pour chaque segment du chemin."""
    roads = []
    key_suffix = "nat" if matrix_type == "national" else "aut"
    for i in range(len(path) - 1):
        info = get_road_info(path[i], path[i + 1])
        dist_val = info.get("d_nat" if matrix_type == "national" else "d_aut", 0)
        road_val = info.get("road_nat" if matrix_type == "national" else "road_aut", "Route locale")
        roads.append({
            "from": path[i],
            "to": path[i + 1],
            "distance": dist_val,
            "road": road_val
        })
    return roads


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
            "time": format_time(dist_national / speed_national),
            "roads": get_path_roads(path_national, "national")
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / speed_autoroute),
            "roads": get_path_roads(path_autoroute, "autoroute")
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
            "time": format_time(dist_national / speed_national),
            "roads": get_path_roads(path_national, "national")
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / speed_autoroute),
            "roads": get_path_roads(path_autoroute, "autoroute")
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
            "time": format_time(dist_national / speed_national),
            "roads": get_path_roads(path_national, "national")
        },
        "autoroute": {
            "path": path_autoroute,
            "distance": dist_autoroute,
            "time": format_time(dist_autoroute / speed_autoroute),
            "roads": get_path_roads(path_autoroute, "autoroute")
        }
    })


if __name__ == '__main__':
    # Démarrage du serveur Flask en mode debug
    # Accessible sur http://localhost:5000
    app.run(debug=True)