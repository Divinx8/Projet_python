class Voiturier:
    """
    Représente un voiturier dans le système DreamPark.

    Un voiturier est une personne chargée de prendre en charge
    les véhicules des clients pour les garer ou les livrer.

    Attributs
    ---------
    num_voiturier : int | str
        Identifiant (numéro) du voiturier.
    """

    def __init__(self, numVoiturier):
        """
        Initialise un nouveau voiturier.

        Parameters
        ----------
        numVoiturier : int | str
            Numéro ou identifiant du voiturier.
        """
        self._num_voiturier = numVoiturier

    def livrerVoiture(self, v, date, heure):
        """
        Livre une voiture à une date et une heure données.

        Pour l'instant, cette méthode ne fait que décrire l'action.
        Plus tard, elle pourra :
        - créer un objet Livraison,
        - mettre à jour un rapport,
        - changer l'état de la voiture (par exemple : 'en cours de livraison' -> 'livrée').

        Parameters
        ----------
        v :
            Véhicule à livrer (objet Voiture ou similaire).
        date :
            Date prévue ou réelle de la livraison.
        heure :
            Heure prévue ou réelle de la livraison.
        """
        # Partie simple pour l'instant : on pourrait juste afficher / tracer l'action
        # ou bien laisser pass si on ne veut pas encore de logique.
        # print(f"Voiturier {self._num_voiturier} livre la voiture {v} le {date} à {heure}.")
        pass

    def getnumVoiturier(self):
        """
        Retourne le numéro du voiturier.

        Returns
        -------
        int | str
            Numéro (identifiant) du voiturier.
        """
        return self._num_voiturier

    def setnumVoiturier(self, numvoiturier):
        """
        Modifie le numéro du voiturier.

        Parameters
        ----------
        numvoiturier : int | str
            Nouveau numéro du voiturier.
        """
        self._num_voiturier = numvoiturier

    def __repr__(self):
        """Représentation textuelle utile pour le débogage."""
        return f"<Voiturier #{self._num_voiturier}>"
