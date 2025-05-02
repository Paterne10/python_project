# Exercice 2:Crée une classe Livre.
class Livre:
    def __init__(self, titre, auteur, disponible):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible
    
    def afficher_infos(self):
        print('Titre:', self.titre)
        print('Auteur:', self.auteur)

        disponible = 'Non'
        if self.disponible:
            disponible = 'Oui'
        print('Disponible:', disponible )
        print()
        self.emprunter()
    
    def emprunter(self):
        print('Vous avez emprunté le livre' if self.disponible else 'Livre non disponible.')
    
    def rendre(self):
        if self.emprunter():
            print('Merci d\'avoir rendu le livre.')
        
        pass 

livre = Livre('Le manuel', 'Epictète', False)
livre.afficher_infos()
# livre.emprunter()
# livre.afficher_infos()
