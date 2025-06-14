import re
from datetime import datetime

    
# function who test the username and the user_first_name.
def validate_name(nom):
    if not nom.strip():
        return "Error : name cannot be empty."
    if any(char.isdigit() for char in nom):
        return "Error : name cannot contain digits."
    if any(not char.isalpha() and char != " " and char != "-" for char in nom):
        return "Error : name can only contain letters, space and dashes."
    if len(nom) < 2:
        return "Error : name must at least contain 2 characters."
    # return f"name successfully registered."
# Test name.


# function who test the birthddate.
def validate_birthdate(date_str):
    # Vérifier le format (JJ-MM-AAAA ou JJ/MM/AAAA)
    if not re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', date_str):
        return "Erreur : Format invalide, utilisez JJ-MM-AAAA ou JJ/MM/AAAA."
    # Séparer la date
    separateur = "-" if "-" in date_str else "/"
    jour, mois, annee = map(int, date_str.split(separateur))

    # Vérification des valeurs
    if jour < 1 or jour > 31:
        return "Erreur : Jour invalide."
    if mois < 1 or mois > 12:
        return "Erreur : Mois invalide."
    if annee < 1900 or annee > datetime.now().year:  # Assurer une année logique
        return "Erreur : Année invalide."

    try:
        datetime(annee, mois, jour)  # Vérification complète
    except ValueError:
        return "Erreur : Cette date n'existe pas."
    # Ajouter une icone (checkbox)
    # return f"birthdate successfully registered."

# Test birthdate

# Function who test the mail-address.
def validate_mail_address(email):
    # Expression régulière pour vérifier un e-mail valide
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(regex, email):
        return "Erreur : Adresse e-mail invalide."
    # return f"mail successfully registered."

# Test mail

# Function who test the user password.

def validate_password(mdp):
    if len(mdp) < 8:
        return "Erreur : Le mot de passe doit contenir au moins 8 caractères."
    if not any(char.isdigit() for char in mdp):
        return "Erreur : Le mot de passe doit contenir au moins un chiffre."
    if not any(char.isupper() for char in mdp):
        return "Erreur : Le mot de passe doit contenir au moins une majuscule."
    if not any(char.islower() for char in mdp):
        return "Erreur : Le mot de passe doit contenir au moins une minuscule."
    if not any(char in "@#$%^&*()-_=+!?" for char in mdp):
        return "Erreur : Le mot de passe doit contenir au moins un caractère spécial."
    if " " in mdp:
        return "Erreur : Le mot de passe ne doit pas contenir d'espaces."
    # return f"password successfully registered."


# Test password

