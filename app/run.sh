#!/bin/bash

# Abrindo uma nova instância do terminal e navegando até o diretório 'api'
gnome-terminal -- bash -c 'cd api; pip install -r requirements.txt; python -m uvicorn main:app --reload --port 3000'

# Navegando até o diretório 'frontend' na instância atual do terminal
cd frontend

# Instalando as dependências do frontend e executando o servidor de desenvolvimento
npm install
npm run dev
