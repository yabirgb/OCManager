from resources import (thing)

def populate_routes(app):
    routes = [
        ("/hello", thing)
    ]

    for route in routes:
        app.add_route(route[0], route[1])
        
    
    return None
