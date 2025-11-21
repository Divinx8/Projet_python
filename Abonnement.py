class Abonnement:
    def __init__(self, libelle , prix, estPackgar):
        self.libelle = libelle  # "STANDARD" ou "PREMIUM"
        self.prix = prix
        self.estPackgar = estPackgar
    
    def getLibelle(self):
        return self.libelle
    
    def getPrix(self):
        return self.prix
    
    def getEstPackgar(self):
        return self.estPackgar
    
    def resilier(self):
        self.estPackgar = False