"""
Module voiture

Définit la classe Voiture, qui représente un véhicule pouvant être garé
dans le parking DreamPark.
"""


class Voiture:
    """
    Représente un véhicule.

    Attributs :
        immatriculation (str):
            Numéro d'immatriculation du véhicule. Ne doit pas être vide.
        longueur (float):
            Longueur du véhicule en mètres. Doit être strictement positive.
        hauteur (float):
            Hauteur du véhicule en mètres. Doit être strictement positive.

    Rôle de la classe :
        - stocker les caractéristiques physiques du véhicule ;
        - permettre de vérifier la compatibilité avec une Place
          (en fonction des dimensions) ;
        - être identifiée de manière unique par son immatriculation.
    """

    def __init__(self, immatriculation, longueur, hauteur):
        """
        Initialise une nouvelle voiture.

        Pour la Partie 0, on définit la signature et la signification
        des paramètres. Les contrôles de validité (immatriculation vide,
        dimensions négatives, etc.) seront implémentés en Partie 1.

        Args:
            immatriculation (str): numéro d'immatriculation du véhicule.
            longueur (float): longueur du véhicule en mètres.
            hauteur (float): hauteur du véhicule en mètres.
        """
        self.immatriculation = immatriculation
        self.longueur = longueur
        self.hauteur = hauteur

    def __eq__(self, other):
        """
        Deux voitures sont considérées comme égales si elles ont
        la même immatriculation.

        Args:
            other (Voiture): autre voiture avec laquelle comparer.

        Returns:
            bool: True si les immatriculations sont identiques, False sinon.

        Note:
            Le comportement détaillé (gestion de None, type différent, etc.)
            pourra être précisé en Partie 1.
        """
        if not isinstance(other, Voiture):
            return False
        return self.immatriculation == other.immatriculation
