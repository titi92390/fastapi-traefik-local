# Projet FastAPI + Traefik (local)

Ce petit projet a été fait dans le cadre de ma formation **DataScientest - DevOps**.

Le but est de faire tourner une application **FastAPI** dans **Docker**, avec **Traefik** comme point d’entrée (proxy).

---

## 1. Objectif

- Créer une API simple avec FastAPI  
- La faire tourner dans un conteneur Docker  
- Ajouter Traefik pour gérer les connexions (micro-services)  
- Tester le tout en local

---

## 2. Structure du projet

fastapi-traefik-local/
│
├── app/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── traefik/
│ └── traefik.yml
│
├── docker-compose.yml
└── README.md

---

## 3. Installation et lancement

### Étape 1 : Cloner le projet

```bash
git clone https://github.com/titi92390/fastapi-traefik-local.git
cd fastapi-traefik-local
