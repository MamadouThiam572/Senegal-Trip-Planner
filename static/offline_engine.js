const REGIONS_DATA = {
    "dakar": { "name": "Dakar", "capital": "Dakar", "lat": 14.7167, "lng": -17.4671, "info": "Capitale du Sénégal", "tips": "Préférez les taxis officiels", "hebergement": "15000-150000 CFA/nuit", "tourisme": "Île de Gorée" },
    "thies": { "name": "Thiès", "capital": "Thiès", "lat": 14.7941, "lng": -16.9639, "info": "Deuxième ville", "tips": "Visitez les villages artisanaux", "hebergement": "8000-50000 CFA/nuit" },
    "diourbel": { "name": "Diourbel", "capital": "Diourbel", "lat": 14.7167, "lng": -16.2333, "info": "Capitale du Mboss", "tips": "Respectez les lieux saints", "hebergement": "5000-25000 CFA/nuit" },
    "kaolack": { "name": "Kaolack", "capital": "Kaolack", "lat": 14.1500, "lng": -16.0833, "info": "Centre économique", "tips": "Marchandez dans les marchés", "hebergement": "6000-30000 CFA/nuit" },
    "saintlouis": { "name": "Saint-Louis", "capital": "Saint-Louis", "lat": 16.0333, "lng": -16.5000, "info": "Ancienne capitale coloniale", "tips": "Explorez l'architecture coloniale", "hebergement": "10000-80000 CFA/nuit" },
    "louga": { "name": "Louga", "capital": "Louga", "lat": 15.6333, "lng": -15.6333, "info": "Région sahélienne", "tips": "Découvrez la culture peule", "hebergement": "4000-15000 CFA/nuit" },
    "kolda": { "name": "Kolda", "capital": "Kolda", "lat": 12.8833, "lng": -14.9500, "info": "Région verdoyante", "tips": "Préférez la saison sèche", "hebergement": "5000-20000 CFA/nuit" },
    "ziguinchor": { "name": "Ziguinchor", "capital": "Ziguinchor", "lat": 12.5833, "lng": -16.2667, "info": "Capitale du sud", "tips": "Prenez le bateau", "hebergement": "10000-60000 CFA/nuit" },
    "sedhiou": { "name": "Sédhiou", "capital": "Sédhiou", "lat": 12.7167, "lng": -15.1833, "info": "Zone de transition", "tips": "Visitez les villages historiques", "hebergement": "4000-15000 CFA/nuit" },
    "kaffrine": { "name": "Kaffrine", "capital": "Kaffrine", "lat": 14.1000, "lng": -15.4167, "info": "Cœur du pays Serer", "tips": "Découvrez la culture Serer", "hebergement": "3000-10000 CFA/nuit" },
    "kedougou": { "name": "Kédougou", "capital": "Kédougou", "lat": 12.5667, "lng": -12.1833, "info": "Parc National Niokolo-Koba", "tips": "Réservez un guide", "hebergement": "15000-60000 CFA/nuit" },
    "matam": { "name": "Matam", "capital": "Matam", "lat": 15.6667, "lng": -13.2667, "info": "Sur le fleuve Niger", "tips": "Essayez la pirogue", "hebergement": "5000-20000 CFA/nuit" },
    "tamba": { "name": "Tambacounda", "capital": "Tambacounda", "lat": 13.7667, "lng": -13.6667, "info": "Porte du Sahel", "tips": "Prévoyez un 4x4", "hebergement": "6000-25000 CFA/nuit" },
    "fatick": { "name": "Fatick", "capital": "Fatick", "lat": 14.3333, "lng": -16.0833, "info": "Sine-Saloum", "tips": "Visitez l'île de Joal-Fadiouth", "hebergement": "5000-30000 CFA/nuit" }
};

const ROAD_DATA = {
    "dakar": {"lat": 14.7167, "lng": -17.4671},
    "thies": {"lat": 14.7941, "lng": -16.9639},
    "diourbel": {"lat": 14.7167, "lng": -16.2333},
    "kaolack": {"lat": 14.1500, "lng": -16.0833},
    "saintlouis": {"lat": 16.0333, "lng": -16.5000},
    "louga": {"lat": 15.6333, "lng": -15.6333},
    "kolda": {"lat": 12.8833, "lng": -14.9500},
    "ziguinchor": {"lat": 12.5833, "lng": -16.2667},
    "sedhiou": {"lat": 12.7167, "lng": -15.1833},
    "kaffrine": {"lat": 14.1000, "lng": -15.4167},
    "kedougou": {"lat": 12.5667, "lng": -12.1833},
    "matam": {"lat": 15.6667, "lng": -13.2667},
    "tamba": {"lat": 13.7667, "lng": -13.6667},
    "fatick": {"lat": 14.3333, "lng": -16.0833}
};

const REGION_NAMES = {
    "dakar": "Dakar", "thies": "Thiès", "diourbel": "Diourbel", "kaolack": "Kaolack",
    "saintlouis": "Saint-Louis", "louga": "Louga", "kolda": "Kolda", "ziguinchor": "Ziguinchor",
    "sedhiou": "Sédhiou", "kaffrine": "Kaffrine", "kedougou": "Kédougou", "matam": "Matam",
    "tamba": "Tambacounda", "fatick": "Fatick"
};

const DISTANCES_NATIONAL = {
    "dakar": {"thies": 46, "fatick": 148, "kaolack": 188, "sedhiou": 280, "kolda": 300, "ziguinchor": 350, "kedougou": 450, "matam": 323, "diourbel": 132, "saintlouis": 179, "louga": 221, "kaffrine": 231, "tamba": 241},
    "thies": {"dakar": 46, "diourbel": 77, "kaolack": 116, "fatick": 75, "kaffrine": 90, "louga": 155, "saintlouis": 146, "sedhiou": 200, "kolda": 220, "ziguinchor": 250, "kedougou": 350},
    "diourbel": {"thies": 77, "kaolack": 85, "saintlouis": 120, "louga": 90, "kaffrine": 65, "sedhiou": 180, "kolda": 200, "ziguinchor": 230, "kedougou": 320, "matam": 200, "tamba": 296},
    "kaolack": {"thies": 116, "diourbel": 85, "fatick": 65, "kaffrine": 58, "sedhiou": 135, "ziguinchor": 205, "tamba": 285, "kolda": 185, "louga": 171, "saintlouis": 214},
    "saintlouis": {"diourbel": 120, "louga": 85, "matam": 180, "fatick": 194, "kaolack": 214, "kaffrine": 244},
    "louga": {"saintlouis": 85, "diourbel": 90, "matam": 110, "thies": 155, "fatick": 152, "kaffrine": 172, "tamba": 296},
    "kolda": {"ziguinchor": 105, "sedhiou": 65, "tamba": 145, "kaolack": 185, "kaffrine": 144, "fatick": 202},
    "ziguinchor": {"kolda": 105, "sedhiou": 85, "kaffrine": 192, "fatick": 195},
    "sedhiou": {"kaolack": 135, "kolda": 65, "ziguinchor": 85, "fatick": 115, "kaffrine": 155, "tamba": 201},
    "kaffrine": {"thies": 90, "diourbel": 65, "kaolack": 58, "tamba": 105, "fatick": 78, "matam": 289},
    "kedougou": {"tamba": 185, "kolda": 305, "matam": 280},
    "matam": {"saintlouis": 180, "louga": 110, "tamba": 160, "kedougou": 280},
    "tamba": {"kaffrine": 105, "matam": 160, "kolda": 145, "kedougou": 185, "kaolack": 285},
    "fatick": {"kaolack": 65, "kaffrine": 78, "sedhiou": 115, "thies": 75, "louga": 152, "ziguinchor": 195, "kolda": 202}
};

const DISTANCES_AUTOROUTE = {
    "dakar": {"thies": 42, "fatick": 140, "kaolack": 175, "sedhiou": 260, "kolda": 280, "ziguinchor": 320, "kedougou": 420, "matam": 305, "diourbel": 125, "saintlouis": 170, "louga": 210, "kaffrine": 220, "tamba": 228},
    "thies": {"dakar": 42, "diourbel": 72, "kaolack": 110, "fatick": 68, "kaffrine": 85, "louga": 148, "saintlouis": 140, "sedhiou": 185, "kolda": 205, "ziguinchor": 235, "kedougou": 330},
    "diourbel": {"thies": 72, "kaolack": 80, "saintlouis": 115, "louga": 85, "kaffrine": 60, "sedhiou": 165, "kolda": 185, "ziguinchor": 215, "kedougou": 300, "matam": 185, "tamba": 280},
    "kaolack": {"thies": 110, "diourbel": 80, "fatick": 58, "kaffrine": 55, "sedhiou": 125, "ziguinchor": 192, "tamba": 268, "kolda": 172, "louga": 162, "saintlouis": 202},
    "saintlouis": {"diourbel": 115, "louga": 78, "matam": 170, "fatick": 185, "kaolack": 202, "kaffrine": 232},
    "louga": {"saintlouis": 78, "diourbel": 85, "matam": 105, "thies": 148, "fatick": 145, "kaffrine": 165, "tamba": 280},
    "kolda": {"ziguinchor": 98, "sedhiou": 58, "tamba": 135, "kaolack": 172, "kaffrine": 135, "fatick": 192},
    "ziguinchor": {"kolda": 98, "sedhiou": 75, "kaffrine": 182, "fatick": 185},
    "sedhiou": {"kaolack": 125, "kolda": 58, "ziguinchor": 75, "fatick": 105, "kaffrine": 145, "tamba": 190},
    "kaffrine": {"thies": 85, "diourbel": 60, "kaolack": 55, "tamba": 95, "fatick": 70, "matam": 275},
    "kedougou": {"tamba": 172, "kolda": 288, "matam": 260},
    "matam": {"saintlouis": 170, "louga": 105, "tamba": 150, "kedougou": 260},
    "tamba": {"kaffrine": 95, "matam": 150, "kolda": 135, "kedougou": 172, "kaolack": 268},
    "fatick": {"kaolack": 58, "kaffrine": 70, "sedhiou": 105, "thies": 68, "louga": 145, "ziguinchor": 185, "kolda": 192}
};

function dijkstraClient(start, end, distMatrix) {
    const regions = Object.keys(ROAD_DATA);
    const dist = {};
    const prev = {};
    const unvisited = new Set(regions);
    
    regions.forEach(r => dist[r] = r === start ? 0 : 9999);
    
    while (unvisited.size > 0) {
        let current = null;
        let minDist = 9999;
        for (const r of unvisited) {
            if (dist[r] < minDist) {
                minDist = dist[r];
                current = r;
            }
        }
        
        if (!current || current === end || dist[current] >= 9999) break;
        unvisited.delete(current);
        
        const neighbors = distMatrix[current] || {};
        for (const [r, d] of Object.entries(neighbors)) {
            if (unvisited.has(r) && d > 0) {
                const newDist = dist[current] + d;
                if (newDist < dist[r]) {
                    dist[r] = newDist;
                    prev[r] = current;
                }
            }
        }
    }
    
    const path = [];
    let current = end;
    while (current && prev[current]) {
        path.unshift(current);
        current = prev[current];
    }
    if (path[0] !== start) path.unshift(start);
    
    return { path: path.length > 0 ? path : [start], distance: dist[end] || 0 };
}

function formatTimeNational(hours) {
    const h = Math.floor(hours);
    const m = Math.round((hours - h) * 60);
    return h > 0 ? `${h}h ${m}min` : `${m}min`;
}

function calculateRouteClient(start, dest) {
    const natResult = dijkstraClient(start, dest, DISTANCES_NATIONAL);
    const autResult = dijkstraClient(start, dest, DISTANCES_AUTOROUTE);
    
    return {
        "national": {
            "path": natResult.path,
            "distance": natResult.distance,
            "time": formatTimeNational(natResult.distance / 80)
        },
        "autoroute": {
            "path": autResult.path,
            "distance": autResult.distance,
            "time": formatTimeNational(autResult.distance / 100)
        }
    };
}

window.ROAD_DATA = ROAD_DATA;
window.REGION_NAMES = REGION_NAMES;
window.REGIONS_DATA = REGIONS_DATA;
window.dijkstraClient = dijkstraClient;
window.calculateRouteClient = calculateRouteClient;

function calculateTSPClient(start) {
    const allRegions = Object.keys(ROAD_DATA);
    const unvisited = new Set(allRegions);
    unvisited.delete(start);
    
    const path = [start];
    let current = start;
    
    while (unvisited.size > 0) {
        let nearest = null;
        let minDist = 9999;
        const dist = DISTANCES_NATIONAL[current] || {};
        
        for (const [r, d] of Object.entries(dist)) {
            if (unvisited.has(r) && d > 0 && d < minDist) {
                minDist = d;
                nearest = r;
            }
        }
        
        if (!nearest) {
            for (const r of unvisited) {
                const d = getHaversineDistance(current, ROAD_DATA[r]);
                if (d > 0 && d < minDist) {
                    minDist = d;
                    nearest = r;
                }
            }
        }
        
        if (!nearest) break;
        path.push(nearest);
        unvisited.delete(nearest);
        current = nearest;
    }
    
    path.push(start);
    
    let totalDist = 0;
    for (let i = 0; i < path.length - 1; i++) {
        const d = DISTANCES_NATIONAL[path[i]][path[i+1]] || 0;
        totalDist += d > 0 ? d : getHaversineDistance(ROAD_DATA[path[i]], ROAD_DATA[path[i+1]]);
    }
    
    return {
        "national": { "path": path, "distance": totalDist, "time": formatTimeNational(totalDist / 80) },
        "autoroute": { "path": path, "distance": Math.round(totalDist * 0.9), "time": formatTimeNational((totalDist * 0.9) / 100) }
    };
}

function getHaversineDistance(from, to) {
    const R = 6371;
    const dLat = (to.lat - from.lat) * Math.PI / 180;
    const dLon = (to.lng - from.lng) * Math.PI / 180;
    const a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.cos(from.lat * Math.PI / 180) * Math.cos(to.lat * Math.PI / 180) * Math.sin(dLon/2) * Math.sin(dLon/2);
    return R * 2 * Math.asin(Math.sqrt(a));
}

window.calculateTSPClient = calculateTSPClient;