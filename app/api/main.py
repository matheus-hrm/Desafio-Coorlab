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

@app.get("/")
def get_root():
    return {}

@app.get("/{city}")
def get_city(city : str):
    city = city if city != "São Paulo" else "SÃ£o Paulo"
    routes = [route for route in data["transport"] if route["city"] == city]
    if routes:
        return routes
    else:
        raise HTTPException(status_code=404, detail=f"City {city} not found")
