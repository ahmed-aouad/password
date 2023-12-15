import hashlib
import json
import random

def generer_random_password():
    lettre = "abcdefghijklmnopqrstuvwxy"
    lettre_M = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nombre = "0123456789"
    speciale = "!@#$%^&*"

    password_c = ( 
    random.choice(lettre) +
    random.choice(lettre_M) +
    random.choice(nombre) +
    random.choice (speciale)+
    ''.join(random.choice(lettre + lettre_M + nombre + speciale) for _ in range(8))
    )
    
    # 
    password_list = list(password_c)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password
    
   

def hash_password(password):
     # Fonction pour hacher le mot de passe en utilisant l'algorithme SHA-256
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return hashed_password

def load_passwords(filename="mdp.json"):
    try:
      # Charger les mots de passe depuis le fichier JSON   
        with open(filename,"r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        # En cas de fichier non trouvé, initialiser une liste vide
        passwords = []
    return passwords

def save_passwords(passwords, filename="mdp.json"):
     # Enregistrer les mots de passe dans un fichier JSON 
    with open(filename, "w") as file:
        json.dump(passwords, file, indent=4)

def is_password_strong():
    hashed_passwords = load_passwords()

    while True: 
        # Boucle pour permettre à l'utilisateur d'essayer plusieurs mots de passe
        password_choice = input("Veuillez entrer g pour générer aléatoire : ") 

        if password_choice.lower() == "g":
            password = generer_random_password()
            print("Votre mot de passe généré aléatoirement est: ", password)

        else:
            password = password_choice    

        if len(password) < 8:
            print("Votre mot de passe doit contenir au moins huit caractères.")
        elif not any(c.isupper() for c in password):
            print("Votre mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(c.islower() for c in password):
            print("Votre mot de passe doit contenir au moins une lettre minuscule.")
        elif not any(c.isdigit() for c in password):
            print("Votre mot de passe doit contenir au moins un chiffre.")
        elif not any(c in "!@#$%^&*" for c in password):
            print("Votre mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)")
        else:
            hashed_password = hash_password(password)
            print("Mot de passe haché :", hashed_password)
            
            save_option = input("Voulez-vous enregistrer ce mot de passe dans le fichier (Oui/Non) : ")
            if save_option.lower() == "oui":
                hashed_passwords.append(hashed_password)  
                save_passwords(hashed_passwords)  
                print("Mot de passe enregistré dans le fichier.")
            
            show_option = input("Voulez-vous afficher la liste des mots de passe hachés? (Oui/Non) ")
            if show_option.lower() == "oui":
                print("Liste des mots de passe hachés :", hashed_passwords)
                
        retry_option = input("Voulez-vous essayer un autre mot de passe (Oui/Non) : ")
        # Sortir de la boucle si l'utilisateur ne souhaite pas essayer un autre mot de passe
        if retry_option.lower() != "oui":
            break

# Appeler la fonction principale pour exécuter le programme
is_password_strong()
