
class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.estAbonne = False
        self.estSuperAbonne = False
        self.nbFrequentation = 0
        self.voitures = []
        self.abonnement = None
    
    # Getters
    def getNom(self):
        return self.nom
    
    def getAdresse(self):
        return self.adresse
    
    def getEstAbonne(self):
        return self.estAbonne
    
    def getEstSuperAbonne(self):
        return self.estSuperAbonne
    
    def getNbFrequentation(self):
        return self.nbFrequentation
    
    def getVoitures(self):
        return self.voitures
    
    def getAbonnement(self):
        return self.abonnement
    
    # Setters
    def setNom(self, nouvN):
        self.nom = nouvN
    
    def setAdresse(self, nouvA):
        self.adresse = nouvA
    
    # Méthodes
    def sAbonner(self, ab):
        self.abonnement = ab
        self.estAbonne = True
        if ab.getType() == "PREMIUM":
            self.estSuperAbonne = True
    
    def seDesabonner(self):
        if self.abonnement:
            self.abonnement.resilier()
        self.estAbonne = False
        self.estSuperAbonne = False
        self.abonnement = None
    
    def nouvelleVoiture(self, imma, hautV, longV):
        voiture = Voiture(imma, hautV, longV)
        self.voitures.append(voiture)
        return voiture
    
    def demanderMaintenance(self, immatriculation):
        if self.estSuperAbonne:
            print(f"Maintenance demandée pour {immatriculation}")
            return True
        else:
            print("Service réservé aux abonnés PREMIUM")
            return False
    
    def demanderLivraison(self, immatriculation, dateLiv, heure, adresseLiv):
        if self.estSuperAbonne:
            print(f"Livraison programmée pour {immatriculation}")
            return True
        else:
            print("Service réservé aux abonnés PREMIUM")
            return False
    
    def demanderEntretien(self, immatriculation):
        return self.demanderMaintenance(immatriculation)
    
    def incrementerFrequentation(self):
        self.nbFrequentation += 1