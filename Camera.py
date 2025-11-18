class Camera():
    """Pas d'initiateur pour la classe, elle n'est composée que de méthodes"""

    def capturerHauteur(self,voiture):
        """Renvoie la hauteur de la voiture"""
        return voiture.getHauteur()

    def capturerLongueur(self,voiture):
        """Renvoie la longueur de la voiture"""
        return voiture.getLongueur()

    def capturerImmat(self,voiture):
        """Renvoie l'immatriculation de la voiture"""
        return voiture.getImmat()