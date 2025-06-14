import random
from cryptography.fernet import Fernet
# liste_lettre_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o','p' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# liste_lettre_max = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# liste_caractere = ['&','!','%', '~','@', '§','$']

# liste_mot_de_passe = []

# while len(liste_mot_de_passe) < 8 :
#     liste_mot_de_passe.append((liste_lettre_min[random.randint(0, len(liste_lettre_min)-1)]))
    # print(liste_lettre_min[random.randint(0, len(liste_lettre_min)-1)])
    # print(liste_lettre_max[random.randint(0, len(liste_lettre_min)-1)])
    # print(liste_caractere[random.randint(0, len(liste_lettre_min)-1)])

text = '1234'

# with open ('mot de passe.txt', 'w') as file:
#     file.write(text)

from cryptography.fernet import Fernet

# Générer une clé de chiffrement
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Chiffrer le texte
encrypted_text = cipher_suite.encrypt(text.encode())

# Stocker la clé séparément et en toute sécurité
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Stocker le texte chiffré
with open('mot_de_passe_secure.txt', 'wb') as file:
    file.write(encrypted_text)

# Déchiffrer.

# Recréer la même instance avec la même clé
# cipher_suite = Fernet(key)

# # Déchiffrer
# decrypted_bytes = cipher_suite.decrypt(encrypted_text)

# # Convertir en texte lisible
# original_text = decrypted_bytes.decode()

# print("Texte déchiffré :", original_text)
