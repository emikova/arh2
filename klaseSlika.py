import math
class Slika:
    broj_slika = 0
    def __init__(self, naziv, visina, sirina, status):
        self.naziv = naziv
        self.visina = visina
        self.sirina = sirina
        self.status = status
        Slika.broj_slika += 1

    def __nonzero__(self, status):
        if self.status == True:
            return "Slika ima autora!"
        else:
            return "Slika nema autora!"

    @classmethod
    def __str__(self, cls):
        return f"Naziv: {cls.naziv}, Visina: {cls.visina}, Sirina: {cls.sirina}, Status: {cls.__nonzero__(cls.status)}"

    @staticmethod
    def razlika_u_povrsini(prva,druga):
        razlika = prva - druga
        return abs(razlika)

    def zamijeni(self, nova_visina, novi_naziv):
        self.visina = nova_visina
        self.naziv = novi_naziv


    def dijagonala(self, visina, sirina):
        v = pow(self.visina,2)
        s = pow(self.sirina, 2)
        zbir = v + s
        return math.sqrt(zbir)



slika1 = Slika("Smece", 12,10,True)
print(Slika.__str__(slika1))
slika2 = Slika("Papir", 20, 4, False)
print(Slika.__str__(slika2))
print(Slika.razlika_u_povrsini(slika1.visina * slika1.sirina, slika2.visina * slika2.sirina))
slika3 = Slika("Hello", 34, 5, True)
print(Slika.__str__(slika3))
Slika.zamijeni(slika1, 45, "Kanta")
print(Slika.__str__(slika1))

print(Slika.broj_slika)


lista =[]
print(Slika.dijagonala(slika1, slika1.visina, slika1.sirina))
lista.append(Slika.dijagonala(slika1,slika1.visina,slika1.sirina))
lista.append(Slika.dijagonala(slika2, slika2.visina, slika2.sirina))
lista.append(Slika.dijagonala(slika3, slika3.visina, slika3.sirina))
print(sorted(lista))

#У класи Слика дефинисати све потребно да би се нека листа слика могла
#сортирати merge сортом. Једна слика је мања од друге ако јој је дијагонала мања.
