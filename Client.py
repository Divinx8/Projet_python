import Voiture 
import Abonnement
import Contrat
import Maintenance
import Entretien
import Livraison
from datetime import * 

class Client():
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.estAbonne = False
        self.estSuperAbonne = False
        self.nbFrequentations = 0 
        self.voiture = None 
        self.abonnement = None
        self.services = {} #Prend un dictionnaire qui comportera les actions octroyés s'il est abonné 
        
        
    def getNom(self):
        """Récupère le nom du client"""
        return self.nom

    
    def getAdresse(self):
        """Récupère l'adresse du client"""
        return self.adresse

    
    def getEstAbonne(self):
        """Renvoie si le client est abonné ou non"""
        return self.estAbonne

    
    def getEstSuperAbonne(self):
        """Renvoie si le client est super abonné ou non"""
        return self.estSuperAbonne

    
    def getNbFrequentations(self):
        """Renvoie le nombre de fréquentation d'un client"""
        return self.nbFrequentations

    def setAdresse(self, nvAdr):
        """Modification de l'adresse du client """
        self.adresse = nvAdr 

    def sAbonner(self, abo : Abonnement): 
        """Le client s'abonne à un des deux abonnements proposés et va utiliser addContrat d'Abonnement"""
        self.abonnement = abo 
        if(abo.getLibelle() == "superAbonnement"):
            self.estSuperAbonne = True
        else: 
            self.estAbonne = True
            self.services = {"maintenance" : Maintenance(), "entretien" : Entretien(), "livraison" : Livraison()} #Si l'utilisateur s'abonne alors il a des services qui lui sont proposés 
        contrat = Contrat(date.today(), self, abo)
        abo.addContrat(contrat)

    def nouvelleVoiture(self, imma, hautV, longV):
        """Prend immatriculation (string), la hauteur (float) et la longueur (float) de la voiture pour créer une voiture qui lui appartient, il ne peut en avoir qu'une, sinon elle est remplacée"""
        self.voiture = Voiture(imma, hautV, longV)

    def seDesabonner(self):#A implémenter plus tard
        """Change estAbonné et estSuperAbonne en false et appelle la méthode rompreContrat de la classe Contrat"""
        pass

    def demanderMaintenance(self):#A implémenter plus tard
        """Va faire appel à effectuerMaintenance() de la classe Maintenance"""
        pass

    def demanderLivraison(self, date, heure, adresseLiv):#A implémenter plus tard
        """Prend une date, une heure et une adresse et va faire appel à effectuerLivraison de la classe Livraison """
        pass

    def demanderEntretien(self):#A implémenter plus tard
        """Va faire appel à effectuerEntretien de la classe Entretien"""
        pass

    def entrerParking(self, acces):
        """Prend un accès et va faire appel à lancerProcedureEntree de la classe Acces puis retourner un string"""
        print(acces.lancerProcedureEntree(self))
            
        
