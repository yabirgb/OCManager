from resources import (thing, communities)

def populate_routes(app):
    routes = [
        ("/hello", thing),
        ("/communities", communities)
    ]

    for route in routes:
        app.add_route(route[0], route[1])
        
    
    return None
