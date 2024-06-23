from livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        if livre.titre and livre.auteur:
            self.livres.append(livre)

    def supprimer_livres(self, livre):
        pass

    def afficher_livres(self):
         if not self.livres:
             print("Pas de quoi afficher")
         for livre in self.livres:
             print(f"ISBN: {livre.isbn}, Auteur: {livre.auteur}, Titre: {livre.titre}")

    def recherche_livres(self, titre, auteur):
        result = []

        for livre in self.livres:
            if(titre and titre.lower() in livre.titre.lower() or auteur and auteur.lower() in livre.auteur.lower()):
                result.append(livre)
            return result
        
    def disponibilite_livre(self, titre):
        for livre in self.livres:
            if titre.lower() in livre.titre.lower() and livre.disponible:
                return True
            return False
        


