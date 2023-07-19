# -*- coding: utf-8 -*-
"""
test docstring
"""


class Eleve:
    """
    test docstring
    """

    def __init__(self, code, nom, prenom, naissance, classe):
        """
        test docstring
        """
        self.code = code
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.classe = classe

    def one_public_method(self):
        """
        test docstring
        """
        return 1

    def second_public_method(self):
        """
        test docstring
        """
        return 1


liste_eleves = []


def ajouter():
    """
    test docstring
    """
    eleve_suivant = ""
    while eleve_suivant not in ["FIN", "fin"]:
        nbr_eleves = int(input("quel est le nombre d'élèves à rajouter ? "))

        i = 1
        while i <= len(nbr_eleves):
            code = int(input("Saisir le code "))
            nom = input("saisir le nom ")
            prenom = input("saisir le prénom ")
            naissance = input("saisir la date de naissance ")
            classe = input("saisir la classe ")
            liste_eleves.append(Eleve(code, nom, prenom, naissance, classe))
            eleve_suivant = input("élève suivant ")

            i += 1

    with open("/home/fitec/Bureau/eduserv.txt", "a", encoding="UTF-8") as file:
        for elev in liste_eleves:
            file.write(
                "code : "
                + str(elev.code)
                + " ; "
                + "Nom : "
                + elev.nom
                + " ; "
                + "Prénom : "
                + elev.prenom
                + " ; "
                + "Naissance : "
                + str(elev.naissance)
                + " ; "
                + "Classe : "
                + str(elev.classe)
                + "\n"
            )
