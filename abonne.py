from livre import Livre
from bibliotheque import Bibliotheque

class Abonne:
    num_id = 0
    def __init__(self, nom, livres_empruntes):
        self.nom = nom
        self.livres_empruntes = livres_empruntes
        Abonne.num_id += 1
        self.id = Abonne.num_id
        self.disponible = True
    
    def emprunter_livres(self, bibliotheque, titre):
        livre_dispo = bibliotheque.recherche_livres(titre)
        livre_dispo = [livre for livre in livre_dispo if livre.disponible]
        if livre_dispo:
            emprunt = livre_dispo[0]
            bibliotheque.disponible_livre(livre_dispo)


        
        
          

            



