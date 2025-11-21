from Client import Client  
from Abonnement import Abonnement

class Contrat:
    def __init__(self, dateDebut, dateFin, client, abonnement):
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.estEnCours = True
        self.client = client  # Instance de Client, pas la classe
        self.abonnement = abonnement
    # Getters et setters 
    def getDateDebut(self):
        return self.dateDebut
    
    def getDateFin(self):
        return self.dateFin
    
    def getEstEnCours(self):
        return self.estEnCours
    
    def getClient(self):
        return self.client
    
    def getLibelle(self):
        return self.abonnement.libelle
    
    # Setters
    def setDateFin(self, dateFin):
        self.dateFin = dateFin
    
    def setClient(self, client):
        self.client = client
    
    # Méthodes
    def rompreContrat(self): 
        self.estEnCours = False
    
    def __str__(self):
        statut = "en cours" if self.estEnCours else "rompu"
        return f"Contrat {self.nom} ({self.dateDebut} - {self.dateFin}) : {statut}"