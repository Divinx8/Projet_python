"""
Module Place
Définit la classe Place qui représente une place de stationnement
dans le parking DreamPark.
"""
import pydoc

class Place :
    """
    Represent une place de Parking
    Attributs :
        numero (int):
            Identifiant unique de la place.
        niveau (int):
            Niveau / étage du parking (0 = rez-de-chaussée, 1 = niveau 1, etc.).
        longueur_max (float):
            Longueur maximale acceptée pour un véhicule (en mètres).
        hauteur_max (float):
            Hauteur maximale acceptée pour un véhicule (en mètres).
        voiture (Voiture | None):
            Référence vers la voiture actuellement garée sur la place,
            ou None si la place est libre.
    """
    def __init__(Self,numero,niveau,longueur_max,hauteur_max):
        """
        Initialise une nouvelle place de parking.
         Args:
            numero (int): identifiant unique de la place (doit être positif).
            niveau (int): niveau / étage du parking.
            longueur_max (float): longueur maximale acceptée (en mètres).
            hauteur_max (float): hauteur maximale acceptée (en mètres).
        """