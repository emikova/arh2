class Hotel:
    def __init__(self, broj_sobe, standard, cijena, opis, status):
        self.broj_sobe = broj_sobe
        self.standard = standard
        self.cijena = cijena
        self.opis = opis
        self.status = status

    def useli_stanare(self, status, opis):
        self.status = "Zauzeta"
        if self.opis == "Slobodna":
            return True
        else:
            return False


soba1 = Hotel(12,"A", 124, "Slobodna", "Slobodna")
print(Hotel.useli_stanare(soba1,soba1.status,soba1.opis))