class Slika:
    broj_slika = 0
    def __init__(self, naziv, visina, sirina, status):
        self.naziv = naziv
        self.visina = visina
        self.sirina = sirina
        self.status = status

        Slika.broj_slika += 1

    def printaj(self):
        return '{} {} {} {}'.format(self.naziv,self.visina,self.sirina,self.status)
    def __nonzero__(self,status):
        if self.status == True:
            return "Ima autora"
        else:
            return "Nema autora"

    @classmethod
    def ispis(cls,string):
        lista = string.split()
        return cls(lista[0], lista[1],lista[2], lista[3])
    @staticmethod
    def razlika_u_povrsini(prva,druga):
        p1= prva.visina * prva.sirina
        p2 = druga.visina * druga.sirina
        return abs(p1 -p2)

    def povecaj_visinu_promjeni_naziv(self, visina2, novi_naziv ):
        self.visina = self.visina + visina2
        self.naziv = novi_naziv

    def __str__(self):
        return f"Naziv:{self.naziv},Visina: {self.visina}, Sirina: {self.sirina}, Status: {self.status} "

    def __lt__(self, druga):
        p1 = self.visina * self.sirina
        p2 = druga.visina * druga.sirina

        if p1 < p2:
            return True
        else:
            return False







prva_slika = Slika("Stvaranje Adama", 100, 200, True)
druga_slika = Slika("Zvjezdana Noc", 400, 300, False)

print(str(prva_slika))
print(str(druga_slika))

if prva_slika < druga_slika:
    print("Manja je prva!")

vrijednost = Slika.razlika_u_povrsini(prva_slika,druga_slika)
print(vrijednost)

Slika.povecaj_visinu_promjeni_naziv(7, "Tratincice")
print(str(druga_slika))

