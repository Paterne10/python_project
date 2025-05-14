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
# -----------------------------------------------------------------------------------
# Exercice 4: Banque- Gestion d'un compte
from colorama import Fore, Back, Style

class CompteBancaire:
    MONNAIE = 'FCFA'
    def __init__(self,titulaire:str, solde:int = 0):
        self.titulaire = titulaire
        self.solde = solde

    def menu(self):
        print('Compte actif:', Fore.GREEN + self.titulaire + Fore.RESET)
        print('*'*10 ,'Menu','*'*10)

        print("1. Afficher le solde")
        print("2. Déposer de l'argent.")
        print("3. Retirer de l'argent.")
        print("4. Quitter.")


    def choix_client(self):
        while True:
            self.menu()
            choix_utilisateur = self.test_entree_choix_client('Répondre : ')
            
            if choix_utilisateur == 4 :
                break
       
            if choix_utilisateur == 1:
                self.afficher_solde()

            elif choix_utilisateur == 2:
                self.deposer()

            elif choix_utilisateur == 3:
                self.retirer() 
            print()


    def deposer(self):
        print('EFFECTUER UN DEPOT SUR VOTRE COMPTE.')

        depot = CompteBancaire.obtenir_une_valeur_numerique('Entrer le montant que vous souhaitez déposer dans votre compte (0. Acceuil): ')
        if depot == 0:
        #    self.menu()
           return
        else:                   
            self.solde += depot
            print(f'Vous avez effectué un dépôt {depot} {CompteBancaire.MONNAIE} sur votre compte. Votre solde est désormais de {self.solde} {CompteBancaire.MONNAIE}')
         
    def retirer(self):   
        print("RETIRER DE L'ARGENT.") 

        montant_a_retirer = CompteBancaire.obtenir_une_valeur_numerique('Entrer le montant que vous souhaitez retirer (0. Acceuil): ')

        if montant_a_retirer == 0:
            # self.menu()
            return

        elif montant_a_retirer <= self.solde:
            self.solde -= montant_a_retirer
            print(f'Vous avez recu {montant_a_retirer} {self.MONNAIE} en cash.')
            print(f'Votre nouveau solde est de : {self.solde} {self.MONNAIE}' )

        else:
            print('Fonds insufisants.')

    def afficher_solde(self):
        print(f'Titulaire du compte: {self.titulaire}')  
        print(f'solde actuel {self.solde} {self.MONNAIE}')  

# Methodes qui testent et récupèrent les entrées des utilisateurs.

    @staticmethod
    def obtenir_une_valeur_numerique(prompt):
        while True:
            a = input(prompt)
            if not a :
                print("L'entrée ne peut pas etre vide.")
                continue
            try:
                a_int = int(a)
            except ValueError:
                print("Le montant doit etre valide. ")
                continue

            if a_int < 0:
                print("Le montant ne peut pas etre négatif.")
                continue

            return a_int 
        
    @staticmethod   
    def test_entree_choix_client(prompt):

        while True :
            a = input(prompt)

            try:
                a_int = int(a)
               
            except ValueError:
                print('Vous devez rentrer un choix valide')
                continue

            if  a_int == 4 :
               return 4               
           
            if not 1  <=  a_int <=  4:
                print('Vous devez choisir une des options du menu (1-4).')
                continue

            return a_int
    
            
# Créer une liste de comptes pour plusieurs clients.
comptes = [   
    CompteBancaire('Loubassou', 50000),
    CompteBancaire('Paterne')
]

# La fonction qui test et récupère l'entrée (choix) de l'utilisateur.
def demander_choix_compte_utilisateur():
    while True:
        choix_compte_client = input('Répondre (0 pour quitter): ')

        if choix_compte_client == '':
            print("L'entrée ne peut pas etre vide.")
            continue
        try:
            choix_compte_client_int = int(choix_compte_client)
            if choix_compte_client_int == 0:
                return 0
            
            if 1  <= choix_compte_client_int <= len(comptes) :           
                break
            print(f'Vous devez choisir une des options du menu ({1}-{len(comptes)})')

        except ValueError:
            print('Vous devez rentrez un choix valide.')
    return choix_compte_client_int

# La fonction qui affiche la liste des comptes.
def afficher_liste_comptes(comptes):
    print("Selectionnez un compte.")
    for i , compte in enumerate(comptes, start= 1):
        print(f'{i}. {compte.titulaire}')



# programme principal.    
while True: 
    afficher_liste_comptes(comptes)
    compte = demander_choix_compte_utilisateur()

    if compte == 0:
        break

    compte_choisi = comptes[compte - 1]
    compte_choisi.choix_client()

    reponse = input('Voulez-vous changez de compte ? (o/n): ').lower()
    if reponse == 'n':
        print("Merci d'avoir utilisé notre service.")
        break


# Accueuil:
#     Choix des comptes
# Menu
#     Choix des actions: Afficher les infos, etc... (0. Acceuil, 00. Précédent)  

# Actions (deposer de l'argent, Retirer de l'argent)  
    # deposer de l'argent(0. Acceuil, 00. Précédent)
#             
# Last point: Menu interactif(Possibilité de revenir à l'écran de connexion).
            
# Constat : 
    # J'ai deux méthodes qui font à peu près la meme chose. (test_entree_choix_client() et obtenir_une_valeur_numerique() )
    # Je dois créer une ou des fonctions qui retournent directement une valueur positive entière(Entre un interval)

# point d'améliorations:
    # Somme minimum et maximun à retirer.