Projet FastAPI et Traefik (déploiement local)


L’objectif de ce projet est de :
Créer une API simple avec FastAPI (Python)
Mettre cette API dans un conteneur Docker
Ajouter Traefik comme proxy d’entrée pour rediriger les connexions HTTP
Lancer le tout avec Docker Compose
Tester l’infrastructure en local.

Architecture du projet

Le projet est basé sur deux conteneurs :
[Client] ---> [Traefik :80] ---> [FastAPI :8000]

Structure des fichiers :

fastapi-traefik-local/
│
├── app/
│   ├── main.py               → Code FastAPI
│   ├── requirements.txt      → Dépendances Python
│   └── Dockerfile            → Image Docker de l’application
│
├── traefik/
│   └── traefik.yml           → Configuration de Traefik (facultatif)
│
├── docker-compose.yml        → Fichier principal pour lancer les services
└── README.md                 → Documentation du projet

Technologies utilisées

Python 3.10
FastAPI
Uvicorn
Docker
Docker Compose
Traefik v2.10
Ubuntu (machine virtuelle locale)

Code FastAPI (main.py)
from fastapi import FastAPI
app = FastAPI(title="Mon API FastAPI")

@app.get("/")
def home():
    return {"message": "Bienvenue sur mon API FastAPI"}

@app.get("/connexion")
def connexion():
    return {"message": "Connexion réussie"}

Le Dockerfile

FROM python:3.10-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

Le docker-compose.yml

version: "3.8"

services:
  traefik:
    image: traefik:v2.10
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
    ports:
      - "80:80"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - web

  fastapi:
    build: ./app
    container_name: fastapi_app
    ports:
      - "8000:8000"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.fastapi.rule=PathPrefix(`/`)"
      - "traefik.http.routers.fastapi.entrypoints=web"
      - "traefik.http.services.fastapi.loadbalancer.server.port=8000"
    networks:
      - web

networks:
  web:
    driver: bridge

Les commandes principales  

- Lancer l'application :
docker compose up -d --build

- Vérifier que les conteneurs tournent : 
docker ps

- Tester l'API :
curl http://127.0.0.1/
curl http://127.0.0.1/connexion

Résultat attendu :
{"message":"Bienvenue sur mon API FastAPI"}
{"message":"Connexion réussie"}

- Arrêter les conteneurs :
docker compose down
 
Sécurité

Les services sont isolés dans des conteneurs Docker.
Traefik sert de point d’entrée unique pour gérer le trafic.
Il est possible d’ajouter plus tard un certificat HTTPS pour sécuriser les échanges.

Conclusion

Ce projet m’a permis de :

Créer une API avec FastAPI
Apprendre à utiliser Docker et Docker Compose
Mettre en place un proxy Traefik
Déployer une architecture simple en micro-services.
((déploiement sur le cloud (AWS,))
