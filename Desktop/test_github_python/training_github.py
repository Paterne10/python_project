# Exercice 2:Crée une classe Livre.
class Livre:
    def __init__(self, titre, auteur, disponible):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible
    
    def afficher_infos(self):
        print('Titre:', self.titre)
        print('Auteur:', self.auteur)

        disponible = 'oui' if self.disponible else 'Non'   
        print('Disponible:', disponible )
        print()
        self.emprunter()
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print('Vous avez emprunté le livre')
        else:
            print('Livre non disponible.')  
    
    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print('Merci d\'avoir rendu le livre.')
        else:
            print('Ce livre est déja disponible.')
        
        pass 

# Création d'une instance (objet) de la classe Livre.
# livre = Livre('Le manuel', 'Epictète', True).afficher_infos()

# Exercice 3: Gérer une liste d'élèves

class Eleve:
    def __init__(self, name:str, age:int, classe_level:str):
        self.name = name
        self.age = age
        self.classe_level = classe_level

    def afficher(self):
        print(f"My name is {self.name}, i'm {self.age} and i'm in {self.classe_level}.")        
        pass

# main programm.
# On crée une liste des objets.
# eleves = [Eleve('Paterne', 25, '3e'),
#           Eleve('Ghost', 24, '4e'),
#           Eleve('Price', 20, '5e')
#           ]
# On parcours la liste d'objets et à chaque objet on applique la methode afficher().
# for eleve in eleves:
#     eleve.afficher()

# Exercice 4: Banque- Gestion d'un compte

class CompteBancaire:

    def __init__(self,titulaire:str, solde:int = 0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer_montant(self):
        print('Effectuer un depot sur votre compte.'.capitalize())

        depot = int(input('Entrer le montant: '))
        self.solde += depot  

    def retirer(self):   
        print("Retirer de l'argent".capitalize())  

        montant_a_retitrer = int(input('Entrer le montant que vous souhaitez retirer: '))  
        if montant_a_retitrer >= self.solde:
            self.solde - montant_a_retitrer
        else:
            print('Fonds insufissants.')

    def afficher_solde(self):
        print(f'Titulaire du compte: {self.titulaire}')  
        print(f'solde actuel {self.solde}')          
        pass
# Last point : Revoir la methode retirer.
personne = CompteBancaire('Paterne')

personne.deposer_montant()
personne.retirer()
personne.afficher_solde()
