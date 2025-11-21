from Service import Service


class Maintenance(Service):
    """
    Représente un service de maintenance effectué sur un véhicule.

    La maintenance peut correspondre, par exemple, à une révision,
    une réparation, un contrôle technique interne, etc.

    Attributs supplémentaires (éventuels)
    ------------------------------------
    type_maintenance : str | None
        Type de maintenance réalisée (\"révision\", \"réparation\", etc.).
    """

    def __init__(self, date_demande, date_service, rapport, type_maintenance=None):
        """
        Initialise un service de maintenance.

        Parameters
        ----------
        date_demande :
            Date de la demande de maintenance.
        date_service :
            Date prévue ou réalisée de la maintenance.
        rapport :
            Rapport ou commentaire associé à la maintenance.
        type_maintenance :
            Type de maintenance (optionnel pour l'instant).
        """
        super().__init__(date_demande, date_service, rapport)
        self._type_maintenance = type_maintenance

    def effectuerMaintenance(self):
        """
        Effectue la maintenance.

        Pour l'instant (début de projet), on se contente de marquer
        dans le rapport que la maintenance a été effectuée.

        Plus tard, cette méthode pourra :
        - changer un état du véhicule (\"en maintenance\" -> \"disponible\"),
        - mettre à jour un historique,
        - déclencher d'autres actions dans le système.
        """
       
        self._rapport = (self._rapport or "") + " | Maintenance effectuée."

    def gettypeMaintenance(self):
        """Retourne le type de maintenance (si défini)."""
        return self._type_maintenance

    def settypeMaintenance(self, type_maintenance):
        """Modifie le type de maintenance."""
        self._type_maintenance = type_maintenance

    def __repr__(self):
        """Représentation textuelle utile pour le débogage."""
        return (f"<Maintenance demande={self._date_demande}, "
                f"service={self._date_service}, "
                f"type={self._type_maintenance}, "
                f"rapport={repr(self._rapport)}>")
