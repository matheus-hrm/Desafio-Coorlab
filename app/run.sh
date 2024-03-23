#!/bin/bash
gnome-terminal --window -- bash -c "./run.sh"
# abre duas abas do terminal em uma janela e as mantem rodando infinitamente
gnome-terminal --tab -- bash -c "sleep 2s; cd api; pip install -r requirements.txt; python3 -m uvicorn main:app --reload --port 3000; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 2s; cd frontend;npm install;npm run dev; exec bash -i"



