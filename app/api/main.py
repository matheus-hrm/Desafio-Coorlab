from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
with open('data.json') as f:
    data = json.load(f)
    
def convert_price_to_number(price):
    return float(price.replace("R$", "").replace(",", "."))

def convert_duration_to_number(duration):
    return int(duration.replace("h", ""))

def sort_routes_fastest(route):
    duration = convert_duration_to_number(route["duration"])
    price_confort = -convert_price_to_number(route["price_confort"])  
    return (duration, price_confort)

def get_fastest_route(routes):
    if routes:
        return min(routes, key=sort_routes_fastest)
    else:
        return None

def sort_routes_cheapest(route):
    price_econ = convert_price_to_number(route["price_econ"])
    duration = convert_duration_to_number(route["duration"])  
    return (price_econ, duration)

def get_cheapest_route(routes):
    if routes:
        return min(routes, key=sort_routes_cheapest)
    else:
        return None
@app.get("/")
def get_root():
    return {}

@app.get("/{city}")
def get_city(city : str):
    routes = [route for route in data["transport"] if route["city"] == city]
    cheapest_route = get_cheapest_route(routes)
    fastest_route = get_fastest_route(routes)
    if routes:
        if cheapest_route == fastest_route:
            return {"cheapest_route": cheapest_route, "fastest_route": "Same as cheapest"}
        else:
            return {"cheapest_route": cheapest_route, "fastest_route": fastest_route}
    else:
        raise HTTPException(status_code=404, detail=f"City {city} not found")