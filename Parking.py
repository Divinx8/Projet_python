"""
Module parking

Définit la classe Parking, responsable de la gestion d'un ensemble
de places de stationnement dans DreamPark.
"""

from place import Place  
import pydoc

class Parking:
    """
    Représente un parking composé de plusieurs places.

    Attributs :
        nom (str):
            Nom ou identifiant du parking (ex. "DreamPark Toulouse").
        places (list[Place]):
            Liste des places gérées par ce parking.

    Rôle de la classe :
        - connaître le nombre total de places ;
        - compter les places disponibles et occupées ;
        - vérifier si le parking est plein ;
        - affecter une place compatible à une voiture ;
        - libérer une place lorsqu'une voiture sort ;
        - fournir des informations utiles pour les statistiques
          (taux d'occupation, etc.).
    """

    def __init__(self, nom, places):
        """
        Initialise un nouveau parking.

        Args:
            nom (str): nom ou identifiant du parking.
            places (list[Place]): liste des places de stationnement.

        Hypothèses (Partie 0) :
            - La liste fournie contient uniquement des instances de Place.
            - La taille de la liste détermine la capacité du parking.
        """
        self.nom = nom
        self.places = places

    def nombre_places_total(self):
        """
        Retourne le nombre total de places gérées par ce parking.

        Returns:
            int: nombre de places.
        """
        return len(self.places)

    def nombre_places_disponibles(self):
        """
        Calcule le nombre de places actuellement disponibles.

        Pour la Partie 0, on se contente de spécifier le comportement
        attendu. L'implémentation détaillée pourra être complétée en Partie 1.

        Returns:
            int: nombre de places libres.
        """
        # Implémentation provisoire (Partie 0) : à adapter en Partie 1.
        return sum(1 for p in self.places if getattr(p, "voiture", None) is None)

    def est_plein(self):
        """
        Indique si le parking est plein.

        Returns:
            bool: True si aucune place n'est disponible, False sinon.
        """
        return self.nombre_places_disponibles() == 0
