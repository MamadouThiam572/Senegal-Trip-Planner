const APP_CACHE = 'senegal-trip-v3';
const TILE_CACHE = 'tiles-v3';

const APP_ASSETS = [
    '/static/offline_routes.js',
    '/static/offline_engine.js',
    '/static/manifest.json',
    '/static/icon-192.png',
    '/static/icon-512.png'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(APP_CACHE).then(cache => {
            return cache.addAll(APP_ASSETS);
        })
    );
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.filter(k => k !== APP_CACHE && k !== TILE_CACHE)
                    .map(k => caches.delete(k))
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', event => {
    const url = new URL(event.request.url);
    
    if (url.host.includes('openstreetmap') || url.host.includes('tile')) {
        event.respondWith(
            caches.open(TILE_CACHE).then(cache => {
                return cache.match(event.request).then(response => {
                    if (response) return response;
                    
                    return fetch(event.request).then(networkResponse => {
                        if (networkResponse.ok) {
                            cache.put(event.request, networkResponse.clone());
                        }
                        return networkResponse;
                    }).catch(() => new Response('', { status: 503 }));
                });
            })
        );
        return;
    }
    
    if (url.hostname === '127.0.0.1' || url.hostname === 'localhost') {
        event.respondWith(
            fetch(event.request).catch(() => {
                return caches.match(event.request).then(response => {
                    if (response) return response;
                    return caches.match('/static/offline_engine.js');
                });
            })
        );
        return;
    }
    
    if (url.host.includes('project-osrm')) {
        event.respondWith(
            fetch(event.request).catch(() => {
                return new Response(JSON.stringify({
                    code: 'Offline',
                    routes: [{ geometry: { coordinates: [] }}]
                }), { status: 200 });
            })
        );
    }
});