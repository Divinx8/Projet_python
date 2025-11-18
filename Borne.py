

class Borne_ticket() :
    
    def delivrerticket(self, c):
        """methode faire de livrer un ticket pour un client c"""
        données = self.recupererInfosCarte(c)
        retour = "----------ticket--------------------\n"

        for elt, val in données.items():
            retour += f"{elt} : {val}\n"

        return retour
    

    def proposerServices(self, c): #Ce n'était pas marqué dans le diagramme mais la fonciton doit prendre un client en paramètre
        "Methode permettre de faire de proposer des services au client"
        for nom, action in c.services.items():
            reponse = ""
            while reponse != "oui" or reponse != "non": #Va demander à saisir oui ou non mais rien d'autre
                print("Voulez vous utiliser le service ", nom, "?")
                reponse = input("Entrer oui ou non : ")
            
            if reponse == "oui": 
                action


    def proposerAbonnements(self,c ,p):
        """Methode faire proposer les abonnements du parking p au client c"""
        for abo in p.mesAbonnement :
            reponse = ""
            while reponse != "oui" or reponse != "non": #Va demander à saisir oui ou non mais rien d'autre
                print("Voulez vous un " + abo.libelle + " au prix de " + abo.prix)
                reponse = input("Entrer oui ou non : ")
            
            if reponse == "oui": 
                c.sAbonner(abo)
                return "Votre abonnement a bien été pris en compte" #Permet d'arrêter si l'utilisateur s'abonne
        
        return "Vous ne vous êtes pas abonné"


    def recupererInfosCarte(self,c):
        """methode permettre de faire recuprer les info de carte de client c"""
        #La documentation dit que ça doit renvoyer un string mais ça n'a aucun sens puisque le retour doit contenir plusieurs informations 
        return {"Nom" : c.getNom(), "Adresse" : c.getAdresse(), "EstAbonne" :c.getEstAbonne(), "EstSuperAbonne" : c.getEstSuperAbonne(), "NbFrequentation" : c.getNbFrequentations()}
        

    def proposerTypePaiement(self):
        """cette methode permettre de faire poroposer type de paiement possible"""
        return "Voici la liste des paiements"


