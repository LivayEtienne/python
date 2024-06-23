from livre import Livre
from bibliotheque import Bibliotheque
from abonne import Abonne

def main():
    bibliotheque = Bibliotheque()
    while True:
        auteur = input("Veillez entrer l'auteur ou 'q' pour quitter:")
        if(auteur == 'q'):
            break

        titre = input("Veillez entrer le titre du livre: ")

        livre = Livre(auteur, titre)
        bibliotheque.ajouter_livre(livre)
    bibliotheque.afficher_livres()
    
    resarch_auteur = input("Entrer l'auteur du livre: ")
    research_titre = input("Entrer le titre du livre: ")

    result = bibliotheque.recherche_livres(resarch_auteur, research_titre)
    for livre in result:
        print(f"ISBN: {livre.isbn}, auteur: {livre.auteur}, titre: {livre.titre}")
    
    resear_dispo = input("Entrer le titre pour verifier si le livre est dispo: ")
    result_dispo = bibliotheque.disponibilite_livre(resear_dispo)
    if(result_dispo):
        print(f"Le livre {resear_dispo} est dispo")
    else:
        print(f"Le livre n'est pas dispo")

main()
