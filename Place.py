import Placement
class Place:
    def __init__(self, numero , niveau , longueur, hauteur):
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur 
        self.hauteur = hauteur
        self.estLibre = True
        self.placement = None
#getteurs
        
    def getNumero(self): 
        return self.numero
    
    def getNiveau(self):
        return self.niveau
    
    def getLongueur(self):
        return self.longueur 
    
    def getHauteur(self):
        return self.hauteur
    
    def getEstlibre(self) :
        return self.estLibre
    
    def getPlacement(self):
        return self.placement
    
#methodes
    def addPlacement(self, p):
        """Ajoute un placement à cette place"""
        if not self.estLibre:
            print("Erreur : la place est déjà occupée")
            return False
        self.placement = p
        self.estLibre = False
        return True
    
    
    