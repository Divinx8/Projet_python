from Service import Service

class Livraison(Service):
    """
    Représente un service de livraison de véhicule réalisé par un voiturier.

    Une livraison est un type particulier de Service où un voiturier
    va chercher la voiture à une place (ou dans un parking) pour la
    livrer à un endroit demandé par le client (domicile, cinéma, etc.).

    Attributs supplémentaires
    -------------------------
    voiturier : object | None
        Le voiturier chargé de la livraison. Il pourra être
        remplacé plus tard par une vraie classe Voiturier.
    """

    def __init__(self, date_demande, date_service, rapport, voiturier=None):
        """
        Initialise un service de livraison.

        Parameters
        ----------
        date_demande :
            Date de la demande de livraison.
        date_service :
            Date prévue ou réalisée de la livraison.
        rapport :
            Rapport associé à la livraison (compte-rendu, remarques, etc.).
        voiturier :
            Voiturier chargé de la livraison (optionnel au départ).
        """
        super().__init__(date_demande, date_service, rapport)
        self._voiturier = voiturier

    def effectuerLivraison(self, voiturier=None):
        """
        Effectue la livraison avec un voiturier donné.

        Pour l'instant (Partie 0 / début du projet), on se contente de
        :
        - enregistrer le voiturier s'il est fourni,
        - et éventuellement marquer dans le rapport que la livraison est effectuée.

        Parameters
        ----------
        voiturier :
            Voiturier chargé de la livraison. S'il est None, on utilise
            celui déjà associé à l'objet.

        Raises
        ------
        ValueError
            Si aucun voiturier n'est défini pour effectuer la livraison.
        """
        if voiturier is not None:
            self._voiturier = voiturier

        if self._voiturier is None:
            raise ValueError("Aucun voiturier défini pour effectuer la livraison.")

        self._rapport = (self._rapport or "") + " | Livraison effectuée."

    def getvoiturier(self):
        """
        Retourne le voiturier chargé de la livraison.

        Returns
        -------
        object | None
            Le voiturier associé à cette livraison, ou None s'il n'est pas défini.
        """
        return self._voiturier

    def setvoiturier(self, voiturier):
        """
        Modifie le voiturier chargé de la livraison.

        Parameters
        ----------
        voiturier :
            Nouveau voiturier à associer à cette livraison.
        """
        self._voiturier = voiturier

    def __repr__(self):
        """
        Représentation textuelle utile pour le débogage.
        """
        return (f"<Livraison demande={self._date_demande}, "
                f"service={self._date_service}, "
                f"voiturier={self._voiturier}, "
                f"rapport={repr(self._rapport)}>")
