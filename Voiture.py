from datetime import datetime

class Voiture:
    def __init__(self, immatriculation, hauteur, longueur):
        self.immatriculation = immatriculation
        self.hauteur = hauteur
        self.longueur = longueur
        self.estDansParking = bool
    
    def getImmatriculation(self):
        return self.immatriculation
    
    def getHauteur(self):
        return self.hauteur
    
    def getLongueur(self):
        return self.longueur
    
    def getEstDansParking(self):
        return self.estDansParking
