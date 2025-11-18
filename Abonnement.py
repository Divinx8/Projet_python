class Abonnement(): 
    def __init__(self, libelle, prix, parkingGaranti):
        """Constructeur de classe, prend un nom, un prix et si oui ou non une place de parking est garantie"""
        self.libelle = libelle
        self.prix = prix
        self.estPackGar = parkingGaranti

    def getLibelle(self):
        """Renvoie le libelle de l'abonnement"""
        return self.libelle
    
    def getPrix(self): 
        """Renvoie le prix de l'abonnement"""
        return self.prix

    def isPackGar(self): 
        """Renvoie si l'abonnement comporte ou non une place de parking dédiée"""
        return self.estPackGar

