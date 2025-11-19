import pwinput
import hashlib
import json
import os

FICHIER = "mots_de_passe.json"

# 0 - Charger le fichier ou en créer un vide
if os.path.exists(FICHIER):
    with open(FICHIER, "r") as f:
        data = json.load(f)
else:
    data = {} # Dictionnaire vide

# 0 - Sauvegarder
def sauvegarder():
        with open(FICHIER, "w") as f:
             json.dump(data, f, indent=4)
             print("Mot de passe enregistré dans", FICHIER)

# 1 - Ajouter un mot de passe
def ajouter_un_mot_de_passe():
    while True: 
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
        nouvelle_cle = f"= {len(data) + 1} - password  "
        data[nouvelle_cle] = password_hache

        sauvegarder()
        print("Mot de passe enregistré ")
        break

# 2 - Generateur de mot de passe aléatoire 
def generator_password():
    import random

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = " ()[]{},;:.-_/\\?+*# "
    
    upper, lower, nums, syms = True, True ,True ,True

    all = ""
    
    if upper:
        all += uppercase_letters
        
    if lower:
        all += lowercase_letters
    
    if nums:
        all += digits
    
    if syms: all += symbols
    
    length = 12
    amount = 1
    for x in range(amount):
        password = "".join(random.choices(all, k=length))
        print(password)

# 3 - Afficher les mots de passe enregistrer
def afficher_mots_de_passe():
     if not data:
          print("Aucun mot de passe enregistré. ")
          return
     print("\n--- Liste des mots de passe --- ")
     for cle, valeur in data.items():
          print(f"{cle}: {valeur}")
          print("------------------------------------------------------------------------------------\n")

# 4 - Supprimer un mot de passe 
def supprimer_mots_de_passe():
     if not data:
          print("Aucun mot de passe à supprimer ")
          return
     print("\n--- Liste des mots de passe --- ")
     for cle, valeur in data.items():
          numero = cle.split()[1]
          print(f"{numero} : {valeur} ")
     print("-------------------------\n ")
     
     numero = input("Entrer le numéro du mot de passe à supprimer : ")

     cle_a_supprimer = None
     for cle in data:
          if cle.startswith(f"= {numero} - password "):
               cle_a_supprimer = cle 
               break

     if cle_a_supprimer:
        del data[cle_a_supprimer]
        sauvegarder()
        print("Mot de passe supprimé. ")
     else:
        print("Numéro introuvable. ")

# ----- MENU -----
while True:
     print("\n====== MENU ======= ")
     print("1 -------> Ajouter un mot de passe ")
     print("2 -------> Créé un mot de passe aléatoire ")
     print("3 -------> Supprimer un mot de passe ") 
     print("4 -------> Afficher tous les mots de passe ")
     print("5 -------> Quitter ")
     
     choix = input("Choix : ")
     if choix == "1":
          ajouter_un_mot_de_passe()
     elif choix == "2":
          generator_password()
     elif choix == "3":
          supprimer_mots_de_passe()
     elif choix == "4":
        afficher_mots_de_passe()
     elif choix == "5":
          break
     else:
        print("Choix invalide. ")

