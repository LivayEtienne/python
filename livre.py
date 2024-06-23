class Livre:
    num_isbn = 0
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        Livre.num_isbn += 1
        self.isbn = Livre.num_isbn
        self.disponible = True

    def aff(self):
        return (f"ISBN: {self.isbn}, auteur: {self.auteur}, titre: {self.titre}")
    