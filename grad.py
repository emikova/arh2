class Grad:
    def __init__(self, naziv_grada, broj_stanovnika, povrsina, postanski_broj, nadmorska_visina):
        self.naziv_grada = naziv_grada
        self.broj_stanovnika = broj_stanovnika
        self.povrsina = povrsina
        self.postanski_broj = postanski_broj
        self.nadmorska_visina = nadmorska_visina


    def __str__(self):
        return f"{self.naziv_grada} {self.broj_stanovnika} {self.povrsina} {self.postanski_broj} {self.nadmorska_visina}"

    def __nonzero__(self):
        if self.postanski_broj == True:
            return "Grad ima postanski broj!"
        else:
            return "Grad nema postanski broj!"

    def __lt__(self, other):
        return self.povrsina < other.povrsina

    def __le__(self, other):
        return self.povrsina <= other.povrsina

    def __gt__(self, other):
        return self.povrsina > other.povrsina

    def __ge__(self, other):
        return self.povrsina >= other.povrsina

    @classmethod
    def opis(cls, string):
        naziv_grada, broj_stanovnika, povrsina, postanski_broj, nadmorska_visina = string.split(",")
        return cls(naziv_grada, int(broj_stanovnika), float(povrsina), int(postanski_broj), float(nadmorska_visina))

    @staticmethod
    def razlika_u_nadmorskoj_visini(nadmorska_visina1, nadmorska_visina2):
        if nadmorska_visina1 == "" and nadmorska_visina2 == "":
            return "Nadmorska visina se ne moze izracunati!"
        else:
            return abs(nadmorska_visina1-nadmorska_visina2)



    def promjena(self, novi_br_stanovnika, novi_naziv):
        self.naziv_grada = novi_naziv
        self.broj_stanovnika = novi_br_stanovnika



g1 = "Kljajcevo, 3000, 1234, 22222,111"
g2 = "Pirot, 200000, 3456, 123323, 443"
print(Grad.opis(g1))
print(Grad.opis(g2))

grad1 = Grad("Hello", 12345,5678,99,12344)
grad2 = Grad("World", 3223123,531,767,222334)
print(Grad.__lt__(grad1,grad2))
