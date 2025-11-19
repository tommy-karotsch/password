import pwinput
import hashlib
import json
import os

FICHIER = "mots_de_passe.json"

# Charger le fichier ou en créer un vide
if os.path.exists(FICHIER):
    with open(FICHIER, "r") as f:
        data = json.load(f)
else:
    data = {}  # dictionnaire vide


while True: 
    print("1 - Ajouter mot de passe ")
    password = pwinput.pwinput("Veuillez entrer votre mot de passe : ")

    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        continue
    
    if not any(c.isupper() for c in password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        continue
    
    if not any(c.islower() for c in password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        continue
    
    if not any(c.isdigit() for c in password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        continue
    
    if not any(c in "-_.;:!?,£€()[]{}/\\!@#$%^&*" for c in password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        continue

    # Hash en SHA‑256
    password_hache = hashlib.sha256(password.encode()).hexdigest()
    print("Mot de passe valide !")
    print("SHA-256 :", password_hache)

    # Définir une clé unique pour ce mot de passe hashé
    nouvelle_cle = f"mot_de_passe{len(data) + 1}"
    data[nouvelle_cle] = password_hache

    # Sauvegarde dans le fichier JSON
    with open(FICHIER, "w") as f:
        json.dump(data, f, indent=4)

    print("Mot de passe enregistré dans", FICHIER)
    break
