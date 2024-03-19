from fastapi import FastAPI
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
    
@app.get("/")
def home():
    return {}

@app.get("/{city}")
def get_city(city : str):
    routes = [route for route in data["transport"] if route['city'] == city]
    if routes:
        return routes
    else:
        return {"error": "City not found"}
