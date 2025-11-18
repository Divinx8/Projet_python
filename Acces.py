class Acces():
    def __init__(self, cam, telEntree, telSortie, panneau, borne):
        self.maCamera = cam
        self.telEntree = telEntree
        self.telSortie = telSortie
        self.monPanneau = panneau
        self.maBorne = borne
        self.parking = None
    def actionnerCamera(self, client): 
        """Appel les fonctions de Camera pour avoir la hauteur, la longueur et l'immatriculation de la voiture, renvoie une voiture"""
        self.maCamera.capturerHauteur(client.voiture)
        self.maCamera.capturerLongueur(client.voiture)
        self.maCamera.capturerImmat(client.voiture)

        return client.voiture

    def actionnerPanneau(self):
        """Appel afficherNbPlacesDisponibles de Panneau_affichage"""
        self.monPanneau.afficherPlacesDisponibles(self.parking)

    def lancerProcedureEntree(self, client) : 
        """Prend un client et va le rajouter ou non sur une place"""
        voiture = self.actionnerCamera(client)
        if (voiture == None) :
            print("Vous n'avez pas de voiture")
        else: 
            donnees = self.maBorne.recupererInfosCarte(client)
            if donnees["EstSuperAbonne"]: #Si le client est superAbonne
                self.telEntree.teleporterVoitureSuperAbonne(voiture)
                return "La place réservée vous a été attribuée"

            #Sinon si le client n'est pas super abonné :
            place = self.parking.recherchePlace(voiture)
            if place == None : #S'il n'y a pas de place disponible 
                return "-------------\nAucune place disponible pour votre véhicule\n-------------"
            
            if donnees["EstAbonne"]:
                self.maBorne.proposerServices(client) #S'il est abonné va lui  proposer et lui faire ses services 
            else:#s'il n'est pas abonné, lui demande son paiement et s'il veut s'abonner
                self.maBorne.proposerTypePaiement() 
                self.maBorne.proposerAbonnements(client, self.parking)
            
            ticket = self.maBorne.delivrerticket(client) #Prend le ticket du client
            ticket+="Place: "+self.parking.getId_place(place.niveau,place.num) +" (Niveau : "+str(place.niveau)+")\n"+"------------------------------------"

            self.telEntree.teleporterVoiture(voiture, place)#Téléporte la voiture

            return ticket








