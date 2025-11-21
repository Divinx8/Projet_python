from Service import Service


class Entretien(Service):
    """
    Représente un service d'entretien effectué sur un véhicule.

    Exemple : nettoyage intérieur, lavage, contrôle simple, etc.

    Attributs supplémentaires
    -------------------------
    type_entretien : str | None
        Type d'entretien ("lavage", "nettoyage intérieur", etc.).
    """

    def __init__(self, date_demande, date_service=None, rapport=None, type_entretien=None):
        """
        Initialise un service d'entretien.

        Parameters
        ----------
        date_demande :
            Date de la demande d'entretien.
        date_service :
            Date prévue ou réalisée de l'entretien.
        rapport :
            Rapport ou commentaire associé à l'entretien.
        type_entretien :
            Type d'entretien (optionnel).
        """
        super().__init__(date_demande, date_service, rapport)
        self._type_entretien = type_entretien

    def effectuerEntretien(self):
        """
        Effectue l'entretien.

        Pour l'instant, on se contente d'ajouter une mention dans le rapport.
        Plus tard, on pourra mettre à jour l'état du véhicule, l'historique, etc.
        """
        self._rapport = (self._rapport or "") + " | Entretien effectué."

    def gettypeEntretien(self):
        """Retourne le type d'entretien (si défini)."""
        return self._type_entretien

    def settypeEntretien(self, type_entretien):
        """Modifie le type d'entretien."""
        self._type_entretien = type_entretien

    def __repr__(self):
        """Représentation textuelle utile pour le débogage."""
        return (
            f"<Entretien demande={self._date_demande}, "
            f"service={self._date_service}, "
            f"type={self._type_entretien}, "
            f"rapport={repr(self._rapport)}>"
        )
