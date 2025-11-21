"""
Module service
Définit la classe Service, utilisée pour représenter un service
(réparation, entretien, livraison, etc.) associé à une voiture.
"""
class Service:
    """
    Représente un service effectué pour un véhicule.

    Attributs
    ---------
    date_demande : str | date
        Date à laquelle le service a été demandé.
    date_service : str | date | None
        Date prévue ou réalisée du service.
    rapport : str | None
        Rapport ou commentaire sur le service (compte-rendu, observations...).

    Auteur : Beni IRAKOZE & [Nom de ton binôme]
    """

    def __init__(self, date_demande, date_service, rapport):
        """
        Initialise un nouveau service.

        Parameters
        ----------
        date_demande :
            Date de la demande de service.
        date_service :
            Date prévue ou réalisée du service.
        rapport :
            Rapport ou commentaire associé au service.
        """
        self._date_demande = date_demande
        self._date_service = date_service
        self._rapport = rapport

    # --- Getters ---

    def get_date_demande(self):
        """Retourne la date de demande du service."""
        return self._date_demande

    def get_date_service(self):
        """Retourne la date de réalisation (ou prévue) du service."""
        return self._date_service

    def get_rapport(self):
        """Retourne le rapport associé au service."""
        return self._rapport

    # --- Setters ---

    def set_date_demande(self, date_demande):
        """Modifie la date de demande du service."""
        self._date_demande = date_demande

    def set_date_service(self, date_service):
        """Modifie la date de réalisation (ou prévue) du service."""
        self._date_service = date_service

    def set_rapport(self, rapport):
        """Modifie le rapport associé au service."""
        self._rapport = rapport

    def __repr__(self):
        """Représentation textuelle utile pour le débogage."""
        return (f"<Service demande={self._date_demande}, "
                f"service={self._date_service}, "
                f"rapport={repr(self._rapport)}>")
