class Bibliotheque:
    
    def __init__(self):
        self.livres = []

    def ajouter_livres(self, livre):
         self.livres.append(livre)
    
    def afficher_livres(self):
        for livre in self.livres:
            print(f"{livre.auteur}, {livre.titre}")

    def recherche_livre(self, titre):
        result = []
        for livre in self.livres:
            if titre.lower() in livre.titre.lower():
                result.append(livre)
        return result