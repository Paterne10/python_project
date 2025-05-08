print("Bienvenue sur notre plateforme d'achat d'unités en ligne.")
class Client:
    
    def __init__(self, nom:str, mot_de_passe: str, telephone:int, mail:str, numero_compteur:int = 0):
        self.nom = nom
        self.mot_de_passe = mot_de_passe
        self.telephone = telephone
        self.mail = mail
        self.numero_compteur = numero_compteur
        if self.numero_compteur == 0:
            self.enregistrer_numero_compteur()
        self.afficher_informations_clients()
        self.acheter_unite()

    def enregistrer_numero_compteur(self):
        self.numero_compteur = input('Enregistrer votre No. de compteur: ')
    
    def afficher_menu(self):
        print('SEEG')
        print('1. MOBILEDAN')
        print('2. MOBILEFACTURE')
    
    def acheter_unite(self):
        self.afficher_menu()
        choix_utilisateur = input('Reply: ')
        if choix_utilisateur == '1':
            self.menu_mobile_edan()
        else:
            print("Ce service n'est pas encore disponible.")
    
    def menu_mobile_edan(self):
        print('1. Inscription')
        print('2. Modification')
        print('3. Paiement')
        choix_utilisateur = input('Reply: ')
        if choix_utilisateur == '3':
            self.menu_paiement()
    
    def menu_paiement(self):
        print('1. Mon numéro')
        print('2. Autre numéro')
        choix_utilisateur = input('Reply: ')
        if choix_utilisateur == '1':
            numero_compteur = input('Entrer numéro de compteur: ')
            return numero_compteur


    def afficher_informations_clients(self):
        print(f'nom: {self.nom}')
        print(f'Contact: {self.telephone}')
        print(f'mot de passe: {self.mot_de_passe}')
        print(f'mail: {self.mail}')
        print(f'no. de compteur: {self.numero_compteur}')

    

              

# Last point: Partie transaction.
        pass

# Si le numéro de compteur est enregistré dans le dictionnaire avec  les informations du client.
#     Enregistre la transaction.
client = Client('Paterne','066868778', 'zambopaterne9@gmail.com', 'Boulangerie23')

# ({'Nom':nom, 'mot_de_passe': mot_de_passe, 'telephone': telephone, 'mail':mail, 'numeo_de_compteur':numero_de_compteur})
