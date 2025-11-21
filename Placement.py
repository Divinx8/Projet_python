from Voiture import Voiture
from Place import Place

class Placement:
    def __init__(self, voiture, place, dateDebut):
        self.voiture = voiture      # Objet de type Voiture
        self.place = place          # Objet de type Place
        self.dateDebut = dateDebut
        self.dateFin = None
        self.estEnCours = True
    
    # Getters
    def getVoiture(self):
        return self.voiture
    
    def getPlace(self):
        return self.place
    
    def getDateDebut(self):
        return self.dateDebut
    
    def getDateFin(self):
        return self.dateFin
    
    def getEstEnCours(self):
        return self.estEnCours
    
    # Méthodes
    def partirPlace(self, dF):
        """Termine le placement en enregistrant la date de sortie"""
        self.dateFin = dF
        self.estEnCours = False