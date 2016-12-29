from resources import (communities)

def populate_routes(app):
    routes = [
        ("/communities", communities)
    ]

    for route in routes:
        app.add_route(route[0], route[1])
        
    
    return None
