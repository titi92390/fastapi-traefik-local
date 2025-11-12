from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI(title="Mon API FastAPI")

# Route principale : page d'accueil
@app.get("/")
def home():
    return {"message": "Bienvenue sur mon API FastAPI 🚀"}

# Route de test : "connexion"
@app.get("/connexion")
def connexion():
    return {"message": "Connexion réussie"}
